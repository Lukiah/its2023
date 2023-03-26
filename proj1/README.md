# Testování a dynamická analýza
### akademický rok 2022/2023
### zpracoval: Lukáš Zedek (xzedek03)
## Projekt - část 1.
## Návrh testovací sady pro regresní testy webové aplikace

### Testovací sady
* page_basic.feature
* page_advanced.feature
* user_actions.feature
* admin_actions.feature
* shopping_cart.feature

### page_basic sada
Obsahuje 5 testovacích scénářů, zaměřených na velmi základní funkcionality aplikace. Konkrétně:
* Načtení aplikace
* Změna zobrazované měny
* Navigace strukturou
* Vyhledávání produktů
* Zobrazení detailů produktu

### page_advanced sada
Obsahuje 4 testovací scénaře, které mají za účel ověřit komplikovanější funkce aplikace. Jedná se o:
* Porovnávání produktů
* Přidání produktu do seznamu přání
* Přihlášení odběru novinek
* Využití kontaktního formuláře

### user_actions sada
Obsahuje 5 testovacích scénářů, týkajících se uživatelského účtu a interakcemi s ním, konkrétně tedy:
* Úspěšná registrace
* Neúspěšná registrace
* Úspěšné přihlášení
* Úspěšná změna hesla
* Neúspěšná změna hesla

### admin_actions sada
Obsahuje 6 testovacích scénářů, ověřujících funkce, které jsou přístupné pouze administrátorům. Jsou to:
* Přihlášení jako administrátor
* Zobrazení objednávek zákazníků
* Přidání položky do katalogu
* Změna na položce v katalogu
* Odebrání účtů zákazníka
* Změna stavu objednávky

### shopping_cart sada
Tato testovací sada, obsahující 5 scénářů, kontroluje zejména funkcionalitu košíku a možnost zadat objednávku. Scénaře jsou následující:
* Přidání položky do košíku
* Zobrazení obsahu košíku
* Odebrání položky z košíku
* Funkční stránka "pokladny"
* Úspěšné zadání objednávky

