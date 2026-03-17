import json
import os

class BasePage:
    # Wskazujemy ścieżkę do pliku z poprzedniego bloku
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        try:
            with open(selectors_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.selectors = data.get("selectors", {})
        except FileNotFoundError:
            print(f"Błąd: Nie znaleziono pliku {selectors_file}. Upewnij się, że Artefakt05 jest zrobiony.")
            self.selectors = {}

    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)


if __name__ == "__main__":
    page = BasePage()
    element_count = len(page.selectors)
    
    # Przykładowy klucz do weryfikacji
    test_key = "ADD"
    verified_value = page.get_selector(test_key)
    
    print(f"[BASE_PAGE] Pomyslnie zainicjalizowano mape: {element_count} elementow.")
    print(f"Weryfikacja klucza '{test_key}': {verified_value}")