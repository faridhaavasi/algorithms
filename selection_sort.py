'''
    big o (n**2)
'''
from random import randint as rint

lenght = 10

_list = [rint(1, 100) for i in range(lenght)]

for i in range(len(_list)):
    min = i
    for j in range(i+1, len(_list)):
        if _list[min] > _list[j]:
            _list[min] ,_list[j] = _list[j], _list[min]  

print(_list)