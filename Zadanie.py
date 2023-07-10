from operator import itemgetter, attrgetter
import re
import datetime
import pandas as pd

# ZADANIE 1--------------------------------------------------------------

def f_title (text):
    print("Wpisz tekst:")
    text = input()
    if type(text) is str:
        Text = text.title()
        print(Text)
    else:
        return None

text = ''
#f_title(text)

# ZADANIE 2--------------------------------------------------------------
#Napisz funkcję `grupuj`, która będzie grupowała słowniki według wartości
#dla wybranego klucza.

owoce = [
     {'nazwa': 'jabłko', 'kolor': 'czerwony'},
     {'nazwa': 'banan', 'kolor': 'żółty'},
     {'nazwa': 'cytryna', 'kolor': 'żółty'},
     {'nazwa': 'gruszka', 'kolor': 'zielony'},
     {'nazwa': 'truskawka', 'kolor': 'czerwony'}
 ]

def grupuj(list_of_dics, key):
    df = pd.DataFrame(list_of_dics)
    df_sorted = df.groupby(key)
    print(df_sorted.sum())

#def grupuj2(list_of_dics, key):
#    for i in list_of_dics:
#        for key, value in i:
#            list_of_dics.sort(key = key)
                    
grupuj(owoce, 'kolor')        
#grupuj2(owoce, 'kolor')

# ZADANIE 3--------------------------------------------------------------

#Napisz funkcję `delta_compression`, która jako argument przyjmuje
#**posortowaną** listę liczb całkowitych i zwróci tę samą listę
#skompresowaną następującym algorytmem:

#1. Pierwszy element listy wyjściowej jest taki sam jak pierwszy
#   element listy wejściowej.
#2. Każdy następny element listy wyjściowej jest równy różnicy między
#   odpowiadającym mu elementem listy wejściowej a elementem
#   poprzedzającym go, czyli `WY[i] = WE[i] - WE[i-1]`.

def delta_compression (list_of_numbs):
    new_list_of_numbs = sorted(list_of_numbs)
    new_list_of_numbs[0] = list_of_numbs[0]
    s = len(list_of_numbs) 
    print(s)
    for r in range(1,s):
        new_list_of_numbs[r] = list_of_numbs[r]-list_of_numbs[r-1]
    print(new_list_of_numbs)

list_of_numbs = [5, 7, 11, 21, 28, 39]
delta_compression(list_of_numbs)    

# ZADANIE 4--------------------------------------------------------------

#Napisz funkcję `grupuj_i_licz`, która jako argument przyjmie listę
#dwuelementowych krotek, gdzie pierwszy element to data (instancja
#`datetime.date`), a drugi to liczba całkowita, i obliczy sumy tych liczb
#dla każdego miesiąca jaki występuje wśród tych dat. Funkcja powinna zwrócić
#słownik, gdzie kluczami będą krotki `(rok, miesiąc)`, a wartościami sumy
#liczb.

x = [
    (datetime.date(2015, 1, 29), 10),
    (datetime.date(2015, 1, 30), 12),
    (datetime.date(2015, 1, 31), 10),
    (datetime.date(2015, 2, 1), 9),
    (datetime.date(2015, 2, 2), 9)
]

df_x = pd.DataFrame(x)
print(df_x)

def grupuj_i_licz(tuple_2el): #lista dwuelementowych krotek
    df_x = pd.DataFrame(tuple_2el)
    df_x.groupby(pd.Grouper(key = '0',freq='M')).sum()

#grupuj_i_licz(df_x) - DO OMÓWIENIA

# ZADANIE 5--------------------------------------------------------------
#Napisz funkcję `tnij`, która przyjmie dwa argumenty: tekst oraz liczbę.
#Funkcja powinna zwrócić tekst pocięty na fragmenty (listę), każdy
#o długości takiej jak liczba podana w argumencie. Ostatni fragment może
#być krótszy niż wymagana długość.

def tnij(text, numb = None):
    if numb <= len(text):
        list_a = []
        for letters in text:
            list_a.extend(letters)
            cut_list = list_a[0:numb]
        print(cut_list)
    else:
        print("Number given is higher than the number of letters in sentence")

tnij('monikon', 3)

# ZADANIE 6--------------------------------------------------------------

#Napisz funkcję, która jako argument przyjmie dowolny tekst i zwróci
#słownik, którego kluczami będą wszystkie słowa z tego tekstu, a wartościami
#będą liczby wystąpień tych słów w tekście. Funkcja powinna być obojętna
#na wielkość liter (czyli 'Kot' i 'kot' mają być traktowane jako jedno
#słowo) i powinna ignorować znaki interpunkcyjne.

def return_dic(text):
    dic = {}
    words = text.split()
    for word in words:
        dic.setdefault(word, text.count(word))
    print(dic)

text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer sollicitudin ultricies eros, vitae eleifend ipsum sodales ut. Pellentesque libero ipsum, euismod eget volutpat nec, hendrerit vel turpis."
return_dic(text1)