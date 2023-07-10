import math 
import datetime
import random

#Napisz funkcję, która zwróci wartość pola powierzchni koła
#o zadanym promieniu (według wzoru `PI * r^2`, gdzie `r` to promień).

def pole_kola(r):
    pole_kola = (math.pi) * (r ** 2)
    print(pole_kola)

pole_kola(1)

#Napisz funkcję, która przyjmuje dwie daty jako argumenty.
#Jeżeli druga data jest mniejsza od pierwszej, funkcja powinna zwrócić
#`None`.  W przeciwnym wypadku funkcja powinna zwrócić liczbę sekund
#dzielącą obie daty.  Zwróć uwagę, że różnica może być większa niż jedna
#doba.  W takim wypadku liczbę dni należy zamienić na sekundy.


def time_differenvce (date_a, date_b):
    if date_a > date_b:
        return None
    else: 
        in_days = date_b - date_a
        in_seconds = in_days.total_seconds()
        print("Liczba sekund pomiędzy datami:", in_seconds)
      

date_random = datetime.datetime(2023,5,10,23,15,0)
date_today = datetime.datetime.today()

time_differenvce(date_random, date_today)

#Napisz funkcję, która przyjmie jako argument dowolną sekwencję
#i zwróci *krotkę* z trzema losowo wybranymi z niej elementami.

def return_tuple(sequence):
    random_tuple=()
    element1 = random.choice(sequence)
    element2 = random.choice(sequence)
    element3 = random.choice(sequence)
    random_tuple = (element1, element2, element3)
    print(random_tuple)


sequence1 = ('a', 'but', 'c', 100, 2, 3)
return_tuple(sequence1)