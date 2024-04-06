from signal import valid_signals


def split(values, first, last):
    '''[4]'''
    temp = values[first]
    item = first
    tf = False
    first += 1
    while first <= last:
        tf = True
        while tf:
            if values[first] > temp:
                tf = False
            else:
                first += 1
                tf = first <= last
        tf = first <= last
        while tf:
            if values[last] <= temp:
                tf = False
            else:
                last -= 1
                tf = first <= last
        if first < last:
            tempitem = values[first]
            values[first] = values[last]
            values[last] = tempitem
            first +=1
            last -= 1
    x = values[item]
    values[item] = values[last]
    values[last] = x
    return last

def quick_sort(values, first, last):
    '''[5]'''
    if first < last:
        temp = split(values, first, last)
        quick_sort(values, first, temp-1)
        quick_sort(values, temp+1, last)

    return values