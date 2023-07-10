#Napisz funkcję, która jako argument przyjmuje listę i zwróci również listę, na której znajdą się wszystkie elementy z argumentu,
#z wyjątkiem wartości równych `None`.

def show_list(list):
    for element in list:
        if element is None:
            pass
        else:
            print(element)

list1=[]
list1 = ['iko', 1, 'azor', None, 2]

show_list(list1)