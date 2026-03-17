import xml.etree.ElementTree as ET

def analyze_manifest():
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    
    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku AndroidManifest.xml.")
        return

    # Pobieramy nazwę paczki [cite: 670]
    package = root.attrib.get('package')
    
    # Wyciągamy aktywności (Activities) [cite: 674, 675, 676]
    activities = [elem.attrib.get('{http://schemas.android.com/apk/res/android}name') for elem in root.findall('.//activity')]
    
    # Wyciągamy uprawnienia (Permissions) [cite: 671, 672, 673]
    permissions = [elem.attrib.get('{http://schemas.android.com/apk/res/android}name') for elem in root.findall('uses-permission')]
    
    # Formatowanie raportu
    report_lines = [
        "=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===",
        f"Pakiet główny: {package}",
        f"Liczba Activity: {len(activities)}",
        "",
        "Kluczowe Uprawnienia (Co aplikacja chce robić?):"
    ]
    
    for perm in permissions:
        if perm:
            report_lines.append(f"- {perm}")

    report_lines.append("")
    report_lines.append("[OK] Sukces! Artefakt zapisany jako: 52_inspection.log")

    full_report = "\n".join(report_lines)
    
    # Wyświetlenie w konsoli (wymagane do screena) [cite: 651]
    print(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POŁĄCZENIE Z ARTEFAKTEM 02) <<<")
    print(full_report)
    
    # Zapis do pliku
    with open('52_inspection.log', 'w', encoding='utf-8') as f:
        f.write(full_report)

if __name__ == "__main__":
    analyze_manifest()