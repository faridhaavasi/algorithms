'''
Define a function that receives a list of a target and
determines which house the target is in the list

'''

# O(1)

def show(list:list, target:int):
    for i in list:
        if i == target:
            return list.index(i)
        
