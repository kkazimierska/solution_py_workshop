#Napisz funkcję `element`, która przyjmuje dwa argumenty, listę oraz
#numer indeksu (integer) i zwraca element listy znajdujący się pod podanym indeksem.

def element(nr_index, lista):
    int(nr_index)
    print(lista[nr_index])

lista_1 = ['element0', 'element1', 'element2']
element(1, lista_1)

#Napisz funkcję `ostatni_element`, która jako argument przyjmuje
#listę i zwraca jej ostatni element.  Użyj w niej funkcji `element`.

def ostatni_element1(lista):
    return element(-1, lista)
    
ostatni_element1(lista_1)

#inaczej
def ostatni_element2(lista):
    nr_index = len(lista)-1
    def element(nr_index, lista):
        int(nr_index)
    print(lista[nr_index])

ostatni_element2(lista_1)

# Napisz funkcję, która jako argument przyjmuje listę i dodaje na jej końcu taki sam element jaki jest na samym jej początku.

lista_2 = ['A', 'B', 'C', 'D', 'E', 'F']

def dodaje_element(lista):
    nowy_element = lista[0]
    lista.append(nowy_element)
    print(lista)

dodaje_element(lista_2)

#Napisz funkcję, która usuwa z listy dwa ostatnie elementy, po czym dodaje do niej ten element, który na samym początku był ostatni.

def zmiana_elementow(lista):
    x = lista.pop()
    lista.pop()
    lista.append(x)
    print(lista)

zmiana_elementow(lista_2)

#Sprawdź co się stanie jeżeli spróbujemy usunąć element, którego nie ma na liście.
#lista_2.remove('Z') # variable not in list

#Napisz funkcję, która przyjmuje dwa argumenty: listę oraz dowolny inny obiekt.  Funkcja powinna usunąć z listy pierwsze wystąpienie tego
#obiektu, a następnie dodać go na końcu listy.  Funkcja powinna zwrócić liczbę wystąpień tego elementu na liście.

def zliczanie(lista, x):
    lista.remove(x)
    lista.append(x)
    liczba_wystąpien = lista.count(x)
    print("Liczba występień zmiennej x:", liczba_wystąpien)

zliczanie(lista_2,'A')

#Sprawdź co się stanie jeżeli spróbujemy pobrać indeks elementu, którego nie ma na liście.
#lista_2.index('Z') # variable not in list

# Napisz funkcję, która jako argument przyjmuje listę i wypisuje na ekran element o największej wartości oraz liczbę wystąpień tego elementu na liście.

lista_3 = [0,1,2,3,4,5,6]

def zliczanie2(lista):
    x = max(lista)
    print("Liczba wystąpień wartości max. równej", x, ":", lista.count(x))

zliczanie2(lista_3)

#Napisz funkcję, która jako argument przyjmie listę, posortuje ją, a następnie zwróci jej ostatni element.  (W ten sposób otrzymamy własną wersję funkcji `max`!)

def max_listy(lista):
    posortowana_lista = sorted(lista)
    print(posortowana_lista[-1])

max_listy(lista_3)

#Zobacz co się stanie, jeżeli indeks początkowy będzie liczbą ujemną, lub jeżeli indeks końcowy będzie większy niż długość listy.
#lista_3[8] #list out of range
#lista_3[-8] #list out of range
#lista[-1] #ostatni element
