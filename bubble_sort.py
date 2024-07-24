'''
big o(n**2)
'''

def bubble_sort(l: list) -> list:
    
    for i in range(len(l)):

        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[i], l[j+1] = l[j+1], l[i]
    return l 
           