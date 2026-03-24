import sys
import os
import time

# Dodajemy sciezke do folderu z Blokiem 6
sys.path.append(os.path.abspath("../Artefakt06"))

try:
    from MainPage import MainPage
except ImportError:
    print("BLAD: Nie znaleziono MainPage.")
    sys.exit(1)

class SyncManager(MainPage):
    # MODUL SYNCHRONIZACJI (Layer 4): Inteligentne czekanie na UI.

    def wait_for_element_and_click(self, business_key, timeout=10):
        # Symulacja profesjonalnego Explicit Wait (WebDriverWait).
        selector = self.get_selector(business_key)
        
        if not selector:
            print(f"OSTRZEZENIE: Brak klucza '{business_key}' w mapie selektorow!")
            return f"BLAD: Brak klucza '{business_key}' w mapie!"
            
        print(f"[SYNC] Rozpoczynam oczekiwanie na: {selector} (max {timeout}s)")
        
        # Symulacja petli sprawdzajacej obecnosc elementu (Polling)
        start_time = time.time()
        
        # W rzeczywistym Appium: element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(...))
        time.sleep(1.5) # Symulacja opoznienia ladowania aplikacji
        
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        
        return f"SUKCES: Element '{selector}' odnaleziony i klikniety po {duration}s."

if __name__ == "__main__":
    manager = SyncManager()
    
    print(">>> ZADANIE 7.4: TESTY SYNCHRONIZACJI DYNAMICZNEJ <<<")
    
    # Symulacja poprawnego znalezienia elementu
    print(manager.wait_for_element_and_click("ADD", timeout=10))
    
    # Symulacja bledu (szukanie nieistniejacego elementu)
    print(manager.wait_for_element_and_click("NON_EXISTENT_BUTTON", timeout=10))