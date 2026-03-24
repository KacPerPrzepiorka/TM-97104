import os
import xml.etree.ElementTree as ET

def scan_for_secrets():
    print(">>> ZADANIE 8.2: SKANER WYCIEKOW DANYCH I SEKRETOW (SAST) <<<")
    
    # Sciezka do zdekodowanych zasobow z Bloku 2
    strings_path = "../Artefakt02/decompiled_apk/res/values/strings.xml"
    
    if not os.path.exists(strings_path):
        print(f"BLAD: Nie znaleziono pliku {strings_path}.")
        return
        
    # Lista slow kluczowych, ktorych szukamy (potencjalne luki)
    sensitive_keywords = ['password', 'secret', 'api', 'token', 'credential', 'key']
    found_secrets = []
    
    try:
        tree = ET.parse(strings_path)
        root = tree.getroot()
        
        # Przeszukujemy wszystkie tagi <string>
        for string_elem in root.findall('string'):
            name = string_elem.attrib.get('name', '').lower()
            
            # Sprawdzamy, czy nazwa zmiennej zawiera "niebezpieczne" slowo
            if any(keyword in name for keyword in sensitive_keywords):
                found_secrets.append(name)
                
    except Exception as e:
        print(f"BLAD parsowania XML: {e}")
        return
        
    print("\n--- WYNIKI SKANOWANIA SEKRETOW ---")
    if found_secrets:
        print(f"[WARNING] Znaleziono {len(found_secrets)} potencjalnych wyciekow danych (Hardcoded Secrets)!")
        # Wypisujemy tylko nazwy zmiennych (bez wartosci - dobra praktyka security)
        for name in found_secrets[:5]: # Pokazujemy max 5 dla czytelnosci
            print(f" - Wykryto podejrzany klucz: '{name}'")
        if len(found_secrets) > 5:
            print(f" - ...oraz {len(found_secrets) - 5} innych.")
    else:
        print("[PASSED] Nie znaleziono zaszytych hasel w strings.xml.")
        
    # Zapis logu z audytu
    with open("82_secrets_report.log", "w", encoding="utf-8") as f:
        f.write("=== RAPORT ZE SKANOWANIA SEKRETOW ===\n")
        f.write(f"Zidentyfikowane potencjalne wycieki: {len(found_secrets)}\n")
        for name in found_secrets:
            f.write(f"Zagrozenie: {name}\n")
            
    print("\n[OK] Raport zapisany do pliku: 82_secrets_report.log")

if __name__ == "__main__":
    scan_for_secrets()