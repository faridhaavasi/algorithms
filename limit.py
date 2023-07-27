'''
Write a function that takes a sorted list and
shows the lowest and highest number and its limit 
based on the example.

example:
[1,2,3,4,5]
min = 3
max = none
output:[1,2,3]
max = 3
min = 0
output:[4,5]
'''

def limit(arry:list, min=None, max=None):
    if max is not None:
        if max in arry:
            max_index = arry.index(max)
            return arry[max_index+1:]
    if min is not None:
        if min in arry:
            min_index = arry.index(min)
            return arry[:min_index+1]
    if min and min:
        min_index = arry.index(min)
        max_index  = arry.index(max)
        return arry[min_index:min_index]


