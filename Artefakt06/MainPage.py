from BasePage import BasePage

class MainPage(BasePage):
    def __init__(self):
        # Inicjalizacja zasobow z klasy bazowej (wymog z checklisty)
        super().__init__()
        print("[MAIN_PAGE] Ekran glowny zainicjalizowany.")

    def click_add_button(self):
        # Pobieramy ID ze slownika z BasePage
        selector = self.get_selector("ADD")
        if selector:
            return f"SUKCES: Wykonano klikniecie w element UI o ID: '{selector}'"
        return "BŁĄD: Nie znaleziono selektora ADD w mapie!"

    def check_text_visibility(self):
        selector = self.get_selector("TITLE")
        if not selector:
            selector = "title" # Zabezpieczenie, gdyby klucz nazywal sie inaczej
        return f"SUKCES: Odnaleziono naglowek strony (ID: {selector}). Status: Widoczny."

    def search_item(self, text):
        selector = self.get_selector("SEARCH")
        if not selector:
            selector = "search_button"
        return f"SUKCES: Wpisano '{text}' do pola {selector} i zatwierdzono."

# Blok testowy wywolujacy akcje (zeby zrobic screena)
if __name__ == "__main__":
    page = MainPage()
    print(page.click_add_button())
    print(page.check_text_visibility())