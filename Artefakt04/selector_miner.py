import xml.etree.ElementTree as ET
import glob
import json
import os

def mine_selectors(path):
    data = []
    count = 0
    # Przeszukuje wszystkie pliki XML w folderze layout
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    data.append({
                        "file": os.path.basename(file),
                        "id": res_id.split('/')[-1],
                        "tag": elem.tag
                    })
                    count += 1
        except Exception:
            pass
            
    # Zapisuje wynik do pliku JSON
    with open('miner_report.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"[OK] Extracted {count} IDs")

# Odwołanie do folderu z rozpakowaną aplikacją z Zadania 2
mine_selectors("../Artefakt02/decompiled_apk/res/layout")