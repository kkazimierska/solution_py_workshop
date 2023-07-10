#Napisz funkcję, która przyjmie listę jako argument i wypisze wszystkie jej elementy przy użyciu pętli `while`.

def print_elements(list):
    a=0
    while a < len(list):
        a=a+1
        print(list[a-1])

list1=[]
list1 = ['iko', 1, 'azor', 2]
print_elements(list1)

