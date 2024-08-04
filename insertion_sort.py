def insertion_sort(_list):
    new_list = []
    for i in _list:
        for j in range(len(new_list)):
            if new_list[j]>i:
                new_list.insert(j,i)
                break
        else:
            new_list.append(i)
    return new_list