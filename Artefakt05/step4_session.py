import json

def build_session():
    caps_path = '51_caps.json'
    selectors_path = '53_selectors.json'

    try:
        # Wczytywanie Capsow
        with open(caps_path, 'r', encoding='utf-8') as f:
            caps_data = json.load(f)
        
        # Wczytywanie Selektorow
        with open(selectors_path, 'r', encoding='utf-8') as f:
            ui_map = json.load(f)
    except FileNotFoundError as e:
        print(f"Blad: Nie znaleziono pliku {e.filename}. Czy poprzednie skrypty na pewno go wygenerowaly?")
        return

    # INTELIGENTNE POBIERANIE DANYCH (Obsluga roznych formatow JSON)
    app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
    app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
    dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")
    
    # Liczba zaladowanych elementow UI
    ui_elements_count = len(ui_map.get("selectors", {}))

    # WERYFIKACJA INTEGRACJI
    if not app_pkg or not app_act:
        status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
    else:
        status_msg = "READY TO CONNECT"

    # Formatowanie eleganckiego raportu z gotowosci
    report = (
        ">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTOW (STABLE BUILD) <<<\n"
        "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===\n"
        "Target App\n"
        f"  Main Activity: {app_act}\n"
        f"  Package      : {app_pkg}\n"
        "Device\n"
        f"  Name         : {dev_name}\n"
        "UI Elements\n"
        f"  Loaded       : {ui_elements_count} loaded\n"
        "Status\n"
        f"  Connection   : {status_msg}"
    )

    print(report)

    # Zapis logu polaczenia
    with open('54_session.log', 'w', encoding='utf-8') as f:
        f.write(report)

if __name__ == "__main__":
    build_session()