# python 3
# selection sort algoritm

l=[3,4,1,2,7,9,5,0]

for i in range(len(l)-1):
    m = i
    for j in range(i+1, len(l)):
        if l[m] > l[j]:
            m = j

    l[i],l[m] = l[m],l[i]
print(l)            