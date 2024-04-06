from copy import deepcopy


def split(values, first, last):
    '''[7]'''
    savefirst = deepcopy(first)
    temp = deepcopy(values[savefirst])
    while first <= last:
        first += 1
        correct = True
        while correct:
            if values[first] > temp:
                correct = False
            else:
                first += 1
                correct = (first <= last)
        correct = (first <= last)
        while correct:
            if values[last] <= temp:
                correct = False
            else:
                last -= 1
                correct = (first <= last)
        if first < last:
            values[first], values[last] = values[last], values[first]
            first += 1
            last -= 1
    values[savefirst], values[last] = values[last], values[savefirst]
    return last
    
def quick_sort(values, first, last):
    '''[8]'''
    if first < last:
        point = split(values, first, last)
        quick_sort(values, first, point-1)
        quick_sort(values, point+1, last)
