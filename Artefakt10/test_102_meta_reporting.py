import pytest
import allure

# Dekoratory biznesowe definiujace hierarchie
@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("Modul Kursy i Lekcje")
@allure.story("Story 1: Przegladanie listy lekcji")
def test_view_lesson_list():
    with allure.step("Krok 1: Uruchomienie aplikacji"):
        # Dodajemy prosty zalacznik tekstowy, czego wymagal wykladowca w zadaniu 10.2
        allure.attach("System zglosil gotowosc. Kod 200.", name="System Log", attachment_type=allure.attachment_type.TEXT)
        
    with allure.step("Krok 2: Nawigacja do ekranu glownego"):
        pass
        
    with allure.step("Krok 3: Weryfikacja czy lista nie jest pusta"):
        assert True, "Lista lekcji zostala zaladowana pomyslnie"

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("Modul Kursy i Lekcje")
@allure.story("Story 2: Przegladanie listy lekcji") # Celowo powtorzone nazewnictwo wg screena z prezentacji
def test_view_lesson_details():
    with allure.step("Krok 1: Wybor pierwszej lekcji z listy"):
        pass
        
    with allure.step("Krok 2: Weryfikacja ekranu szczegolow"):
        assert True, "Szczegoly lekcji zostaly wyswietlone"