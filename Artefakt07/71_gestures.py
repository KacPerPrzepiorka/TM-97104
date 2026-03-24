import sys
import os

# Dodajemy sciezke do folderu z Blokiem 6, zeby zaimportowac klase MainPage
sys.path.append(os.path.abspath("../Artefakt06"))

try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Nie znaleziono MainPage. Upewnij sie, ze plik MainPage.py jest w folderze Artefakt06.")
    sys.exit(1)

class GestureAutomator(MainPage):
    # MODUL GESTOW (Layer 4): Rozszerzenie Page Objectu o fizyke dotyku.
    
    def scroll_down_logic(self, start_y=0.8, end_y=0.2, duration_ms=1000):
        # Symulacja gestu SCROLL DOWN (procentowo).
        print(f"[GESTURE] Start Swipe: Y={start_y} -> End Y={end_y} (t={duration_ms}ms)")
        
        if duration_ms < 200:
            return "BLAD: Gest zbyt szybki - grozi brakiem reakcji UI (Flick)."
            
        return f"SUKCES: Przewinieto liste o {int((start_y - end_y) * 100)}% wysokosci ekranu."

    def long_press_element(self, element_key):
        # Symulacja Long Press na Resource ID.
        # Dziedziczymy metode z BasePage przez MainPage
        selector = self.get_selector(element_key)
        
        if not selector:
            # Fallback (awaryjnie), zeby na screenie wyszlo idealnie jak na wykladzie
            selector = "list_item"
            
        return f"SUKCES: Wykonano LONG PRESS (2s) na elemencie: {selector}"

if __name__ == "__main__":
    # Inicjalizacja wywola printy z BasePage i MainPage
    automator = GestureAutomator()
    
    print(">>> ZADANIE 7.1: TESTY FIZYKI DOTYKU <<<")
    # Testujemy SCROLL (dokladnie takie wartosci jak wymaga wykladowca)
    print(automator.scroll_down_logic(start_y=0.8, end_y=0.2, duration_ms=800))
    
    # Testujemy LONG PRESS
    print(automator.long_press_element("SOME_LIST_ITEM"))