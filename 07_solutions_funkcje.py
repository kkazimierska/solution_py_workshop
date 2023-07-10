#Napisz funkcję, która przyjmuje argument rok_urodzenia`, 
#wypisuje tekst `Masz X lat`, gdzie `X` to wiek w roku 2017, oraz zwraca ten wiek.exit()


def rok_urodzenia(rok_urodzenia):
    x = 2017 - rok_urodzenia
    print("Masz ", x, " lat")

rok_urodzenia(1989)

#Zobacz co się stanie, jeżeli liczba argumentów metody `format` będzie mniejsza niż liczba wystąpień `{}` w stringu

#'Liczba wystąpień {} w stringu jest właśnie taka i wynosi {}'.format('wąsów')
#indeks zastąpień 1 poza zakresem tupla argumentów pozycyjnych ;) / Replacement index 1 out of range for positional args tuple