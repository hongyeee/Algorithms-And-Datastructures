from copy import deepcopy
from lib2to3.pgen2.token import RIGHTSHIFTEQUAL


def merge_sort(values, first, last):
    
    '''[5]'''
    if first < last:
        middle = int((first + last) / 2)
        merge_sort(values, first, middle)
        merge_sort(values, middle + 1, last)
        merge(values, first, middle, middle + 1, last)

def merge(values, leftFirst, leftLast, rightFirst, rightLast):

    '''[6]'''
    temp = []
    savefirst = deepcopy(leftFirst)

    while leftFirst <= leftLast and rightFirst <= rightLast:
        if values[leftFirst] < values[rightFirst]:
            temp.append(values[leftFirst])
            leftFirst += 1
        else:
            temp.append(values[rightFirst])
            rightFirst += 1
    
    while leftFirst <= leftLast:
        temp.append(values[leftFirst])
        leftFirst += 1
    
    while rightFirst <= rightLast:
        temp.append(values[rightFirst])
        rightFirst += 1

    for i in range(0, rightLast -savefirst + 1, 1):
        values[savefirst+i] = temp[i]

