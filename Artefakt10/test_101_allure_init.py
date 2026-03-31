import pytest
import allure

@allure.feature("10.1: Inicjalizacja Allure")
def test_success_case():
    with allure.step("Krok 1: Uruchomienie aplikacji"):
        pass
    with allure.step("Krok 2: Logowanie poprawnymi danymi"):
        pass
    with allure.step("Krok 3: Weryfikacja udanego logowania"):
        assert True, "Test zakonczony sukcesem"

@allure.feature("10.1: Inicjalizacja Allure")
def test_failure_case():
    with allure.step("Krok 1: Otwarcie modulu platnosci"):
        pass
    with allure.step("Krok 2: Wprowadzenie danych karty"):
        pass
    with allure.step("Krok 3: Oczekiwany blad odrzucenia transakcji"):
        assert False, "Wymuszony blad dla celow wygenerowania czerwonego wykresu w Allure"