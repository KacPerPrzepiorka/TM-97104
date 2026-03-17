from MainPage import MainPage

def run_pom_test():
    print(">>> ZADANIE 6.3: TEST SCENARIUSZA W ARCHITEKTURZE POM <<<")

    # Inicjalizacja obiektu strony
    page = MainPage()
    
    print("PRZEBIEG SCENARIUSZA TESTOWEGO")
    
    # Symulacja logiki biznesowej
    step1 = page.check_text_visibility()
    step2 = page.click_add_button()
    step3 = page.search_item("Automatyzacja Mobilna")
    
    # Formatowanie krokow do konsoli
    krok1 = f"KROK 1: {step1}"
    krok2 = f"KROK 2: {step2}"
    krok3 = f"KROK 3: {step3}"
    
    print(krok1)
    print(krok2)
    print(krok3)

    # Zapis logu audytu
    with open("64_pom_audit.log", "w", encoding="utf-8") as f:
        f.write("Test Execution Log:\n")
        f.write(f"{krok1}\n{krok2}\n{krok3}\n")
        
    print("[OK] Scenariusz wykonany. Log audytu zapisany w 64_pom_audit.log")

if __name__ == "__main__":
    run_pom_test()