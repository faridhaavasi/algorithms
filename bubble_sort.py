'''
big o(n**2)
'''

def bubble_sort(l: list) -> list:
    
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l 
           

