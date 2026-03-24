import xml.etree.ElementTree as ET
import os

def audit_manifest():
    print(">>> ZADANIE 8.1: AUDYT BEZPIECZENSTWA MANIFESTU (SAST) <<<")
    
    # Korzystamy z pliku, ktory zdekodowalismy w Bloku 2
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    
    if not os.path.exists(manifest_path):
        print(f"BLAD: Nie znaleziono pliku {manifest_path}. Upewnij sie, ze sciezka jest poprawna.")
        return

    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()
    except Exception as e:
        print(f"BLAD parsowania XML: {e}")
        return
        
    android_namespace = '{http://schemas.android.com/apk/res/android}'
    
    print("\n--- WYNIKI SKANOWANIA ---")
    
    # 1. Sprawdzanie trybu debugowania (Krytyczna luka, jesli true na produkcji)
    application = root.find('application')
    if application is not None:
        debuggable = application.attrib.get(f'{android_namespace}debuggable', 'false')
        if debuggable.lower() == 'true':
            print("[HIGH RISK] Aplikacja ma wlaczony tryb debugowania (android:debuggable=\"true\")!")
        else:
            print("[PASSED] Tryb debugowania jest wylaczony.")
    
    # 2. Sprawdzanie wyeksportowanych aktywnosci (Narazenie na Intent Spoofing)
    exported_count = 0
    for activity in root.findall('.//activity'):
        exported = activity.attrib.get(f'{android_namespace}exported')
        if exported == 'true':
            exported_count += 1
            
    print(f"[INFO] Znaleziono {exported_count} wyeksportowanych aktywnosci (android:exported=\"true\").")
    if exported_count > 0:
        print("[WARNING] Wyeksportowane aktywnosci moga byc narazone na ataki zewnetrzne.")
        
    # Zapis logu z audytu
    with open("81_manifest_report.log", "w", encoding="utf-8") as f:
        f.write("=== RAPORT Z AUDYTU MANIFESTU ===\n")
        f.write(f"Debuggable: {debuggable}\n")
        f.write(f"Exported Activities: {exported_count}\n")
        f.write("Status: WYMAGA WERYFIKACJI INZYNIERSKIEJ\n")
        
    print("\n[OK] Raport z weryfikacji zapisany do pliku: 81_manifest_report.log")

if __name__ == "__main__":
    audit_manifest()