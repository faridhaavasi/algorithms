#python 3
#bubble dsort algoritm

_list = [5,8,4,2,1,3,6]

lenght = len(_list)

for i in range(lenght-1):
    for j in range(lenght-i-1):
        if _list[j] > _list[j+1]:
            _list[j] , _list[j+1] = _list[j+1] , _list[j]
print(_list)            