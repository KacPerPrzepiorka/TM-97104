import xml.etree.ElementTree as ET
import glob
import json
import os

def check_accessibility(path):
    gaps = []
    ns = '{http://schemas.android.com/apk/res/android}'
    files = glob.glob(path + "/**/*.xml", recursive=True)

    for file in files:
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_text = elem.get(f'{ns}text')
                node_desc = elem.get(f'{ns}contentDescription')
                node_id = elem.get(f'{ns}id', 'no-id')

                # Luka: Jest tekst, ale nie ma opisu (contentDescription)
                if node_text and not node_desc:
                    gaps.append({
                        "file": os.path.basename(file),
                        "id": node_id.split('/')[-1],
                        "text": node_text,
                        "issue": "Brak atrybutu contentDescription"
                    })
        except Exception:
            continue

    # Zapis do pliku JSON
    with open('a11y_report.json', 'w', encoding='utf-8') as f:
        json.dump(gaps, f, indent=4, ensure_ascii=False)

    print(f"Analiza A11y zakonczona. Znaleziono {len(gaps)} luk. Raport zapisano w a11y_report.json")

if __name__ == "__main__":
    check_accessibility("../Artefakt02/decompiled_apk/res/layout")