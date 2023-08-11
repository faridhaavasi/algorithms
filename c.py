l = [1,5,6,7,9,12,2,5,6,8]
m=0
for i, v in enumerate(l):
    if i:
        if v > m:
            m = v

print(m)
    