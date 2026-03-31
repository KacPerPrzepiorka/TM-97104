import pytest
import allure

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("10.3: Dowody wizualne (Zalaczniki)")
@allure.story("#1 Test ze zrzutem ekranu (Symulacja)")
def test_screenshot_on_fail():
    
    with allure.step("Krok 1: Proba klikniecia w przycisk 'Zapisz'"):
        try:
            # Symulacja bledu, jakby elementu UI nie bylo na ekranie
            raise Exception("ElementNotVisibleException")
            
        except Exception as e:
            # ZALACZNIK 1: Zrzut ekranu (wysylamy "puste" dane PNG dla symulacji)
            allure.attach(
                b"Fake image data", 
                name="Screenshot_Error_01", 
                attachment_type=allure.attachment_type.PNG
            )
            
            # ZALACZNIK 2: Odpowiedz z API / Log tekstowy
            allure.attach(
                "Tresc bledu: Serwer zwrocil timeout podczas proby zapisu.", 
                name="API_Response", 
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Wymuszamy ostateczne oblanie testu (na czerwono), zeby wyswietlic logi
            pytest.fail(f"Test padl, ale mamy dowody! Log:\n{e}")