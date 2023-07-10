#Napisz funkcję, która jako argument przyjmie listę liczb i wpisze na ekran wartość każdej z nich podniesioną do kwadratu.
lista_liczb1 = [0,1,2,3]
nowa_lista_liczb = []

def kwadrat(lista_liczb):
    for liczba in lista_liczb:
        wynik = liczba**2
        nowa_lista_liczb.append(wynik)
    print(nowa_lista_liczb)
    
kwadrat(lista_liczb1)

# Napisz funkcję, który przyjmie listę stringów i zwróci nową listę, na której znajdą się wszystkie te stringi pisane wielkimi literami
#(użyj metody `upper`).

lista=['a','b','c']

def up_the_letter(lista):
    for letters in lista:
        print(letters.upper())
up_the_letter(lista)

#Napisz funkcję, która jako argument przyjmie string i wypisze każdą jego literę wraz z liczbą wystąpień tej 
# litery w stringu (użyj metody`count`).

def count_letters(text):
    str(text)
    for letters in text:
        no_of_letters = text.count(letters)
        print(letters, '-', no_of_letters)

text = 'aaa bbb ccc'
count_letters(text)

#Napisz funkcję, która jako argument przyjmuje string i wypisuje wszystkie jego słowa, każde w osobnej linijce.

def show_words(text):
    words = text.split(' ')
    for word in words:
        print(word)

show_words(text)

#Napisz funkcję, która jako argument przyjmuje string i wypisuje wszystkie jego słowa, każde w osobnej linijce.
