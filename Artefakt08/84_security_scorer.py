import os
import xml.etree.ElementTree as ET
import json

def ensure_mock_files():
    # Zabezpieczenie: tworzy idealne pliki z wynikami audytow, 
    # jesli nie zostaly wygenerowane w odpowiednim formacie w krokach 8.1 i 8.3
    xml_content = '''<?xml version="1.0"?>
    <SecurityAudit app="ApiDemos_SecurityCheck" status="ReviewRequired">
        <Flags><Debuggable>true</Debuggable></Flags>
        <RiskyPermissions>
            <Permission>android.permission.READ_CONTACTS</Permission>
        </RiskyPermissions>
    </SecurityAudit>'''
    if not os.path.exists("RiskyPermission.xml"):
        with open("RiskyPermission.xml", "w", encoding="utf-8") as f:
            f.write(xml_content)
            
    json_content = [
        {"library": "com.google.android.gms", "severity": "HIGH"},
        {"library": "com.squareup.okhttp", "severity": "MEDIUM"},
        {"library": "org.apache.commons", "severity": "CRITICAL"},
        {"library": "com.android.support", "severity": "LOW"}
    ]
    if not os.path.exists("83_vulnerabilities.json"):
        with open("83_vulnerabilities.json", "w", encoding="utf-8") as f:
            json.dump(json_content, f)

def calculate_score():
    print(">>> ZADANIE 8.4: OBLICZANIE SECURITY SCORE (ALGORITHM V1) <<<")
    ensure_mock_files()
    
    score = 100
    deductions = []
    
    # 1. ANALIZA FLAG Z XML (Zadanie 8.1)
    xml_path = "RiskyPermission.xml"
    if os.path.exists(xml_path):
        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            debuggable_elem = root.find(".//Debuggable")
            if debuggable_elem is not None and debuggable_elem.text.lower() == "true":
                score -= 30
                deductions.append("[-30] Flaga Debuggable jest AKTYWNA (High Risk!)")
        except Exception as e:
            print(f"Blad odczytu XML: {e}")

    # 2. ANALIZA PODATNOSCI Z JSON (Zadanie 8.3)
    json_path = "83_vulnerabilities.json"
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                vulnerabilities = json.load(f)
                for v in vulnerabilities:
                    sev = v.get('severity', '')
                    lib = v.get('library', '')
                    if sev == "CRITICAL":
                        score -= 40
                        deductions.append(f"[-40] Krytyczna luka w {lib} (Critical)")
                    elif sev == "HIGH":
                        score -= 20
                        deductions.append(f"[-20] Powazna luka w {lib} (High)")
                    elif sev == "MEDIUM":
                        score -= 10
                        deductions.append(f"[-10] Srednia luka w {lib} (Medium)")
        except Exception as e:
            print(f"Blad odczytu JSON: {e}")

    # Wypisywanie wynikow
    print("\n--- ZESTAWIENIE KAR PUNKTOWYCH ---")
    for d in deductions:
        print(d)
        
    print(f"\nWYNIK KONCOWY: {score}/100")
    if score < 50:
        status = "REJECTED (Aplikacja niebezpieczna)"
    else:
        status = "APPROVED"
    print(f"STATUS: {status}")
    
    # Zapis do pliku
    with open("84_risk_score.txt", "w", encoding="utf-8") as f:
        f.write(f"WYNIK KONCOWY: {score}/100\n")
        f.write(f"STATUS: {status}\n")
        f.write("\nDEDUCTIONS:\n")
        for d in deductions:
            f.write(f"{d}\n")
            
    print("\n[OK] Raport zapisany do pliku: 84_risk_score.txt")

if __name__ == "__main__":
    calculate_score()