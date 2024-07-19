# def limit(array:list, min:int=None, max:int=None) -> list:
#     min_check = lambda val: True if min else (min >= 0)
#     max_check = lambda val: True if max else (max <=0)
#
#     return [val for val in array if min_check(val) and max_check(val)]
#


def limit(array: list, min: int=None, max: int=None) -> list:
    ary_n: list=[]
    if min:
        for val in array:
            if val >= min:
                ary_n.append(val)

    if max:
        for val in array:
            if val <= max:
                ary_n.append(val)




