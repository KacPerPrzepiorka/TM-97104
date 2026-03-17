import xml.etree.ElementTree as ET
import json

def get_caps():
    # Ścieżka do manifestu z Artefaktu 02
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    
    try:
        tree = ET.parse(manifest_path)
        root = tree.getroot()
    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku AndroidManifest.xml. Upewnij się, że Artefakt02 jest poprawnie wykonany.")
        return

    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    # Pobieranie paczki
    package = root.attrib.get('package')
    main_activity = None

    # Szukanie aktywności z intent-filter MAIN
    for activity in root.findall('.//activity'):
        for intent in activity.findall('.//intent-filter'):
            action = intent.find('.//action[@android:name="android.intent.action.MAIN"]', ns)
            if action is not None:
                main_activity = activity.attrib.get('{http://schemas.android.com/apk/res/android}name')
                break
        if main_activity:
            break

    # Tworzenie obiektu Capabilities
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": package,
        "appActivity": main_activity,
        "deviceName": "emulator-5554",
        "noReset": True
    }

    # Zapis do pliku JSON
    with open('51_caps.json', 'w', encoding='utf-8') as f:
        json.dump(capabilities, f, indent=4)
    
    print(f"Sukces! Wykryto: {package} / {main_activity}")

if __name__ == "__main__":
    get_caps()