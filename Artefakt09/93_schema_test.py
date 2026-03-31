import requests
from jsonschema import validate, ValidationError

def test_schema_validation():
    print(">>> ZADANIE 9.3: WALIDACJA STRUKTURY JSON (KONTRAKT) <<<")
    
    # DEFINICJA SCHEMATU (Nasz "odlew" danych)
    expected_schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title"] 
    }
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        
        # Walidacja (Serce testu)
        validate(instance=data, schema=expected_schema)
        
        print("[SUCCESS] Kontrakt zachowany. Struktura JSON jest poprawna.")
        print(f"[DEBUG] Zweryfikowano pola dla obiektu ID: {data.get('id')}")
        
    except ValidationError as e:
        print(f"[ERROR] Walidacja schematu nie powiodla sie! Zly typ danych: {e.message}")
    except Exception as e:
        print(f"[FATAL] Blad polaczenia z API: {e}")

if __name__ == "__main__":
    test_schema_validation()