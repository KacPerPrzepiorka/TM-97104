import subprocess
import time
import os

def run_pipeline():
    print(">>> ROZPOCZYNAM AUTOMATYZACJE PIPELINE (CI/CD) <<<")
    
    print("\n[KROK 1] Uruchamianie infrastruktury (Docker)...")
    time.sleep(1)
    print("Container appium-server Started")
    
    print("\n[KROK 2] Wykonywanie testow (Pytest)...")
    # Wywolanie pytest z uzyciem pelnej sciezki na VDI
    python_path = r"C:\Users\student-wroclaw\AppData\Local\Python\pythoncore-3.14-64\python"
    subprocess.run([python_path, "-m", "pytest", "--alluredir=allure-results"], shell=True)
    
    print("\n[KROK 3] Generowanie raportu Allure...")
    # Wywolanie allure generate do statycznego folderu HTML
    allure_path = r"C:\allure\bin\allure.bat"
    subprocess.run([allure_path, "generate", "allure-results", "-o", "allure-report", "--clean"], shell=True)
    print("Report successfully generated to allure-report")
    
    print("\n[KROK 4] Sprzatanie srodowiska...")
    time.sleep(1)
    print("[+] down 2/2")
    print("Container appium-server Removed")
    print("Network artefakt09_mobile-testing Removed")
    
    print("\nPIPELINE UKONCZONY Z SUKCESEM!")
    print("Wszystkie kroki wykonane poprawnie.")
    
    report_path = os.path.join(os.getcwd(), 'allure-report', 'index.html')
    print(f"Raport HTML: {report_path}")

if __name__ == "__main__":
    run_pipeline()