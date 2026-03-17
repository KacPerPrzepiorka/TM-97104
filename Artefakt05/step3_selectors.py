import os
import xml.etree.ElementTree as ET
import json
import glob

def build_ui_map():
    layout_dir = "../Artefakt02/decompiled_apk/res/layout"
    ui_map = {"selectors": {}}
    count = 0

    # Przeszukuje folder layout w poszukiwaniu plików XML
    for file_path in glob.glob(layout_dir + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Szukamy wszystkich elementów z atrybutem id
            for element in root.iter():
                res_id = element.attrib.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    # Oczyszczamy ID (np. @id/button -> button)
                    clean_id = res_id.split('/')[-1]
                    # Tworzymy nazwę biznesową (wielkie litery)
                    business_name = clean_id.upper()
                    
                    # Dodajemy do słownika tylko unikalne klucze
                    if business_name not in ui_map["selectors"]:
                        ui_map["selectors"][business_name] = clean_id
                        count += 1
        except Exception:
            continue

    # Zapisujemy do pliku 53_selectors.json
    with open('53_selectors.json', 'w', encoding='utf-8') as f:
        json.dump(ui_map, f, indent=4)

    print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTOROW (UI MAPPING) <<<")
    print(f"[OK] Zmapowano {count} unikalnych elementow UI.")
    print("Artefakt zapisany: 53_selectors.json")

if __name__ == "__main__":
    build_ui_map()