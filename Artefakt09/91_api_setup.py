import requests

def test_api_connectivity():
    print(">>>> ZADANIE 9.1: TEST POŁĄCZENIA Z API BACKENDOWYM <<<<")
    
    # Adres testowego API (symuluje backend aplikacji mobilnej)
    base_url = "https://jsonplaceholder.typicode.com/todos/1"
    
    # Wymaganie: obsługa nagłówków (Headers) i autoryzacji
    headers = {
        "Authorization": "Bearer MOCK_TOKEN_123",
        "Accept": "application/json"
    }
    
    try:
        # Wykonanie żądania GET
        response = requests.get(base_url, headers=headers, timeout=5)
        
        # Analiza inżynierska odpowiedzi
        status_code = response.status_code
        data = response.json()
        
        print(f"[DEBUG] Status Code: {status_code}")
        print(f"[DEBUG] Response Body: {data}")
        
        # Asercja (Serce testu)
        if status_code == 200:
            print(f"[SUCCESS] API jest dostępne. Tytuł zadania: {data.get('title')}")
        else:
            print(f"[ERROR] Serwer zwrócił błąd: {status_code}")
            
    except Exception as e:
        print(f"[FATAL] Brak łączności z API: {e}")

if __name__ == "__main__":
    test_api_connectivity()