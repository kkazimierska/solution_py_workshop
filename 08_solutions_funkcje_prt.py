#Zdefiniuj funkcję o nazwie `pole_kola`, która przyjmuje argument promien` i zwraca wartość równania `3.14 * (promien ** 2)`.  Wywołaj ją
#w oknie trybu interaktywnego.

def pole_kola(promien):
    wynik = 3.14*(promien**2)
    print(wynik)

pole_kola(3.45)

#Wywołaj funkcję `pole_kola` bez argumentu: `pole_kola()`. Czy rozumiesz treść wyjątku jaki został rzucony?

#pole_kola() #funkcji pole_kola() brakuje jednego argumentu pozycyjnego pn. promien

#Wywołaj funkcję `pole_kola` z dwoma argumentami: `pole_kola(2, 3)` Porównaj treść wyjątku do błędu z poprzedniego zadania.

#pole_kola(1, 3) # funkcja pole_kola() przyjmuje 1 argument pozycyjny, a wskazano dwa

#Napisz funkcję `cena_brutto`, która przyjmuje argumenty `cena_netto` oraz `vat` i zwraca wartość brutto obliczoną według wzoru
#`netto * (1 + vat)`.

def cena_brutto(cena_netto, vat):
    wartosc_brutto = cena_netto * (1+vat)
    print(wartosc_brutto)

vat = 0.23
cena_brutto(1.0, vat)
cena_brutto(1.0, 0.23)

#Napisz funkcję `imie_nazwisko`, która przyjmuje argumenty `imie` oraz `nazwisko` i zwraca stringa z imieniem i nazwiskiem oddzielonymi
#spacją.  Upewnij się, że każde słowo w stringu zaczyna się od wielkiej litery (użyj metody `title`).  Następnie napisz funkcję `lubi`,
# z argumentami `imie`, `nazwisko` oraz `co` i wywołana w ten sposób: `lubi('jan', 'kowalski', 'KALAFIORY')` zwróci stringa
# 'Jan Kowalski lubi kalafiory'`.  Pisząc funkcję `lubi` użyj funkcji `imie_nazwisko`.

def imie_nazwisko(imie, nazwisko):
    dane = imie.title() +' ' + nazwisko.title()
    print(dane)

def lubi(imie, nazwisko, co):
    co_lubi = imie.title() + ' ' + nazwisko.title() + ' lubi ' + co
    print(co_lubi)

imie_nazwisko('Johny', 'Bravo')
lubi('Johny', "Bravo", 'siebie')

#Zobacz co się stanie, gdy:
#  przekażesz do funkcji `int` liczbę z częścią ułamkową (float), np. `3.14`
#  przekażesz do `int` stringa, w którym nie ma żadnej liczby
# kiedy przekażesz do `int` stringa, w którym są zarówno litery jak i cyfry, np. `Ala ma 2 koty`.
int(2.34567) # zaokrągla liczbę do liczby całkowitej, ale zawsze do dołu (float>int)
int('ana') #niewłaściwy znak dla intiger z bazą 10: 'ana'
int('Ala ma 2 koty i 3 psy') #j.w.
int('Ala ma 2 koty') # j.w.

#Zobacz jak zachowa się funkcja `float`, gdy wywołasz ją z: integerem, stringiem z samymi literami, stringiem z samymi cyframi.
float(3) #zmiana na float - zmiennoprzecinkowy 3.0
float('ana') #nie może przetworzyć stringa na float
float('23344546') #string będący ciągiem cyfr przetwarza na float