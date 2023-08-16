#python 3
#inserition sort

_list = [5,8,4,2,1,3,6]

lit = []
for i in _list:
    for j in range(len(lit)):
        if i<lit[j]:
            lit.insert(j,i)
            break
    else:
        lit.append(i)

print(lit)                
