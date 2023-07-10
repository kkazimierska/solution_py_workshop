#Napisz funkcję, która przyjmuje argumenty `element` i `lista` i jeżeli dany element znajduje się na liście, to zwraca jego pozycję
#(użyj metody `index`), w przeciwnym wypadku zwraca `-1`.

def check_list(element, list):
    el_pos = list.index(element)
    for element in list:
        element is list
        if True:
            print("present on the list in position", el_pos)
        else:
            print("do not exist in the list")
    
element1 = 'bread'
list1 = ['cocumber', 'tomatoe', 'onion', 'bread']

check_list(element1, list1)

#Napisz funkcję `iloraz`, która przyjmuje argumenty `dzielna` i `dzielnik`. Jeżeli dzielnik jest różny od zera, funkcja powinna zwrócić
#wynik dzielenia.  W przeciwnym wypadku powinna wypisać komunikat o błędzie.

def iloraz(dzielna, dzielnik):
    if dzielnik != 0:
        wynik = dzielna/dzielnik
        print(wynik)
    else:
        print("Nie dziel przez zero")

iloraz(10,0)

#Napisz funkcję, która porównuje dwie liczby.  Jako argumenty powinna przyjmować liczby `a` i `b`.  Jeżeli `a` jest większe od `b`
#powinna zwrócić 1, jeżeli liczby są równe `0`, a jeżeli `a` jest mniejsze od `b`, `-1`.  Dodatkowo, w zależności od wyniku porównania, funkcja
#powinna wypisać jeden z komunikatów: `a < b`, `a == b` lub `a > b`.

def compare(a,b):
    float(a)
    float(b)
    if a > b:
        print('a > b')
        return 1
    elif a + b == 0:
        print('a == b')
        return 0
    elif a < b:
        print('a < b')
        return -1
        
compare(0,9)

#Dla każdego z następujących typów odszukaj wartość, dla której funkcja `bool` zwróci `True` i taką dla której zwróci `False`: string,
#krotka, integer, float.

int()

def checking_if(complexlist):
    for part in complexlist:
        if type(part) is int:
            print(part, '- is an integer')
        elif type(part) is str:
            print(part, '-is a string')
        elif type(part) is tuple:
            print(part, '-is a tuple')
        elif type(part) is float:
            print(part, '- is a float')
        else:
            print(part, 'is none of known')


complexlist1 = ['ana', 1, ('krotka', 'stokrotka', 'tokrotka'), 3.14]
checking_if(complexlist1)
    
#Napisz funkcję, która jako argument przyjmie listę i zwróci `True` jeżeli wszystkie elementy na tej liście są prawdziwe, albo `False` jeżeli
# przynajmniej jeden element nie jest prawdziwy.

def checkinglist (list):
    for element in list:
       if element == element:
           print('ok')
       else:
           print('not ok')


checkinglist(complexlist1)