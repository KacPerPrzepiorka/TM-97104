# RAPORT Z AUDYTU BEZPIECZEŃSTWA: APIDEMOS
**Data:** 24.03.2026
**Audytor:** Kacper Przepiórka (97104)
**Projekt:** ApiDemos Security Audit

## 1. OCENA KOŃCOWA (SECURITY SCORE)
**WYNIK:** 0/100
**STATUS:** 🔴 REJECTED

## 2. KLUCZOWE OBSZARY RYZYKA

### A. Konfiguracja Systemowa (Zadanie 8.1)
**Problem:** Włączona flaga `android:debuggable="true"` oraz wyeksportowane aktywności.
**Wpływ:** Umożliwia atakującym podpięcie debuggera, swobodną inżynierię wsteczną w czasie rzeczywistym oraz ataki typu Intent Spoofing.

### B. Wycieki Danych (Zadanie 8.2)
**Problem:** Obecność twardo zakodowanych sekretów (Hardcoded Secrets) w pliku `strings.xml` (np. `password`).
**Wpływ:** Ryzyko nieautoryzowanego dostępu do usług, baz danych lub przejęcia kont użytkowników przez osoby trzecie.

### C. Biblioteki Zewnętrzne (Zadanie 8.3)
**Problem:** Użycie starych bibliotek z lukami CVE (np. RCE w `org.apache.commons`).
**Wpływ:** Krytyczne zagrożenie zdalnym wykonaniem kodu (RCE), co może prowadzić do całkowitego przejęcia kontroli nad aplikacją.

## 3. MAPA DROGOWA NAPRAWCZA (REMEDIATION)
1. **[PRIORYTET 1]:** Natychmiastowa zmiana wartości na `android:debuggable="false"` dla środowisk produkcyjnych.
2. **[PRIORYTET 1]:** Pilna aktualizacja "dziurawych" bibliotek zewnętrznych do ich najnowszych, bezpiecznych wersji.
3. **[PRIORYTET 2]:** Usunięcie wszystkich twardo zakodowanych haseł i tokenów z zasobów projektowych (przeniesienie ich np. do zewnętrznych, zabezpieczonych systemów typu Vault).

## WNIOSKI KOŃCOWE
Aplikacja ApiDemos w obecnej formie stanowi krytyczne zagrożenie i kategorycznie nie może zostać dopuszczona do wdrożenia (Release). Oczekiwane jest natychmiastowe wdrożenie mapy naprawczej przez zespół deweloperski.