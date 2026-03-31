import requests

def test_create_resource():
    print(">>> ZADANIE 9.2: TEST TWORZENIA ZASOBU (POST) <<<")
    
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"[INFO] Wysylanie zadania POST do: {url}")
    
    # Dane, ktore wysylamy (Payload w formacie JSON)
    new_post = {
        "title": "Test Mobilny Blok 9",
        "body": "Automatyzacja API jest szybsza niz UI",
        "userId": 1
    }
    
    # Informujemy serwer, ze wysylamy mu JSON-a
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }
    
    try:
        # Zauwaz, ze tutaj uzywamy .post(), a nie .get()!
        response = requests.post(url, json=new_post, headers=headers)
        
        status = response.status_code
        result_data = response.json()
        
        print(f"[DEBUG] Status Code: {status}")
        print(f"[DEBUG] Server Response: {result_data}")
        
        # 201 oznacza "Created" (Zasob utworzony pomyślnie)
        if status == 201:
            print(f"[SUCCESS] Zasob stworzony pomyslnie! ID nowego obiektu: {result_data.get('id')}")
        else:
            print(f"[ERROR] Serwer nie utworzyl zasobu. Status: {status}")
            
    except Exception as e:
        print(f"[FATAL] Blad polaczenia z API: {e}")

if __name__ == "__main__":
    test_create_resource()