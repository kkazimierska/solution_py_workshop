'Monika Birgiel - Marszał'.lower()
'Ełk'
'27 sierpnia 2023'.strip()
'Biegnąca z wilkami'.title()

'Zwróć uwagę, że litera `a` jest na pozycji `0`, więc litera `r` tak naprawdę jest nie dwudziestą trzecią, ale dwudziestą czwartą literąalfabetu.  Ten przykład pokazuje jak ważne jest poprawne interpretowanie informacji zwracanych przez programy.'.find('ale')

'Wybierz kilka paragrafów (2 lub więcej) z tej strony i dla każdego z nich: skopiuj jego treść i użyj jej do zdefiniowania stringa, a następnie wywołaj na nim metodę `find` żeby sprawdzić, czy znajdujesię w nim łańcuch `ale`.'.find('ale')

'Monika Birgiel - M'.replace('Monika', 'Marek')

'Skopiuj treść któregoś z paragrafów na tej stronie, użyjgo do zdefiniowania stringa i wywołując na nim metodę `count` sprawdźile razy występują w nim następujące ciągi znaków: ` i `, `string` oraz`na`.'.count(' i ')
'Skopiuj treść któregoś z paragrafów na tej stronie, użyjgo do zdefiniowania stringa i wywołując na nim metodę `count` sprawdźile razy występują w nim następujące ciągi znaków: ` i `, `string` oraz`na`.'.count(' string ')
'Skopiuj treść któregoś z paragrafów na tej stronie, użyjgo do zdefiniowania stringa i wywołując na nim metodę `count` sprawdźile razy występują w nim następujące ciągi znaków: ` i `, `string` oraz`na`.'.count(' na ')

len('Monika Birgiel')
len('')