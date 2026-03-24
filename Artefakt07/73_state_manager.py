import sys
import os
import datetime

# Dodajemy sciezke do folderu z Blokiem 6, zeby zaimportowac klase MainPage
sys.path.append(os.path.abspath("../Artefakt06"))

try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Nie znaleziono MainPage. Upewnij sie, ze plik MainPage.py jest w folderze Artefakt06.")
    sys.exit(1)

class DeviceStateManager(MainPage):
    # MODUL ZARZADZANIA STANEM (Layer 4): Obsluga fizycznych zmian urzadzenia.

    def __init__(self):
        super().__init__()
        self.log_file = "73_state.log"

    def _log_event(self, event_name, detail):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {event_name.upper()}: {detail}\n")

    def toggle_screen_orientation(self, target="LANDSCAPE"):
        # Symuluje obrot urzadzenia.
        print(f"[DEVICE] Zmiana orientacji na: {target}")
        
        # W Appium to byloby np: driver.orientation = "LANDSCAPE"
        detail = f"Ekran obrocony do {target}. Weryfikacja przerysowania layoutu..."
        self._log_event("orientation", detail)
        
        return f"SUKCES: Orientacja zmieniona na {target}."

    def simulate_power_connection(self, is_connected=True):
        # Zarzadzanie stanem zasilania (wazne dla procesow w tle).
        state = "CONNECTED" if is_connected else "DISCONNECTED"
        print(f"[DEVICE] Zasilanie: {state}")
        
        # W Appium np: driver.set_power_capacity(100) lub driver.set_power_ac(True)
        self._log_event("power_state", f"Zasilanie zewnetrzne: {state}")
        
        return f"SUKCES: Stan zasilania ustawiony na {state}."

if __name__ == "__main__":
    manager = DeviceStateManager()
    
    print(">>> ZADANIE 7.3: ZARZADZANIE FIZYCZNYM STANEM URZADZENIA <<<")
    
    # Test obrotu (Round-trip)
    print(manager.toggle_screen_orientation("LANDSCAPE"))
    print(manager.toggle_screen_orientation("PORTRAIT"))
    
    # Test zasilania
    print(manager.simulate_power_connection(True))
    
    print("[OK] Zmiany zapisane w: 73_state.log")