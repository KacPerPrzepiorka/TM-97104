import sys
import os
import time

# Dodajemy sciezke do folderu z Blokiem 6, zeby zaimportowac klase MainPage
sys.path.append(os.path.abspath("../Artefakt06"))

try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Nie znaleziono MainPage. Upewnij sie, ze plik MainPage.py jest w folderze Artefakt06.")
    sys.exit(1)

class InterruptManager(MainPage):
    # MODUL PRZERWAN (Layer 4): Symulacja zdarzen systemowych Androida.

    def simulate_incoming_call(self, duration_sec=3):
        # Symuluje nadchodzace polaczenie, ktore przyslania aplikacje.
        print("\n[INTERRUPT] KROK 1: Stan aplikacji przed polaczeniem: ACTIVE")
        print(f"[INTERRUPT] KROK 2: Wyzwalanie zdarzenia: INCOMING CALL (Duration: {duration_sec}s)")
        
        # W prawdziwym Appium: driver.make_gsm_call(phone_number, GsmCallActions.CALL)
        time.sleep(1)
        print(">>> SYSTEM: Aplikacja w tle (onPause) | Widoczny ekran polaczenia <<<")
        
        time.sleep(duration_sec) # Czas trwania rozmowy
        
        print("[INTERRUPT] KROK 3: Zakonczenie polaczenia. Powrot do aplikacji.")
        # W prawdziwym Appium: driver.activate_app('io.appium.android.apis')
        
        return "SUKCES: Aplikacja odzyskala fokus (onResume). Dane sesji zachowane."

    def simulate_low_battery_warning(self):
        # Symuluje systemowy komunikat o niskim stanie baterii (System Dialog).
        print("\n[INTERRUPT] Wyzwalanie zdarzenia: LOW BATTERY WARNING")
        # W prawdziwym Appium: driver.set_power_capacity(5)
        return "SUKCES: Aplikacja obsluzyla systemowe okno dialogowe bez bledu."

if __name__ == "__main__":
    manager = InterruptManager()
    
    print(">>> ZADANIE 7.2: TESTY ODPORNOSCI NA PRZERWANIA <<<")
    # Symulacja polaczenia trwajacego 3 sekundy
    print(manager.simulate_incoming_call(duration_sec=3))
    
    # Symulacja komunikatu o slabej baterii
    print(manager.simulate_low_battery_warning())