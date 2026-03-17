import json

def run_final_assertion():
    print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")
    print("FEEDBACK DLA TWORCOW APLIKACJI")
    
    # Wczytanie danych z poprzednich zadan
    try:
        with open('51_caps.json', 'r', encoding='utf-8') as f:
            caps = json.load(f)
        with open('53_selectors.json', 'r', encoding='utf-8') as f:
            ui_map = json.load(f)
    except Exception as e:
        print("Blad wczytywania plikow:", e)
        return

    current_pkg = caps.get("appPackage") or caps.get("appium:appPackage")
    
    report_lines = []
    report_lines.append(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")
    report_lines.append("FEEDBACK DLA TWORCOW APLIKACJI")

    # 1. Weryfikacja Pakietu
    if current_pkg == "io.appium.android.apis":
        msg1 = f"[ZGODNY] Identyfikacja Aplikacji: Pakiet {current_pkg} poprawnie zmapowany."
    else:
        msg1 = f"[DO POPRAWY] Niezgodnosc pakietu. Wykryto {current_pkg}, sprawdz konfiguracje manifestu."
    
    print(msg1)
    report_lines.append(msg1)

    # 2. Weryfikacja Dostepnosci Elementow UI
    target_element = "ACCESSIBILITY"
    if target_element in ui_map.get("selectors", {}):
        msg2 = f"[ZGODNY] Dostepnosc UI: Element '{target_element}' jest dostepny w layoutach."
    else:
        available_keys = list(ui_map.get("selectors", {}).keys())[:3]
        msg2 = f"[INFORMACJA] Dostepnosc UI: Nie odnaleziono ID '{target_element}'. Sugestia: Zweryfikuj czy element nie zmienil nazwy na jedna z dostepnych: {available_keys}."
    
    print(msg2)
    report_lines.append(msg2)
    
    msg3 = "[INFO] Blok 5 zakonczony. Raport opisowy gotowy: 55_result.xml"
    print(msg3)
    report_lines.append(msg3)

    # Zapis do pliku XML (jako tekstowy log)
    with open('55_result.xml', 'w', encoding='utf-8') as f:
        f.write("\n".join(report_lines))

if __name__ == "__main__":
    run_final_assertion()