
def reheap_down(elements, root, bottom):
    '''[2]'''
    left = root *2+1
    right = root*2+2
    if left <= bottom:
        if left == bottom:
            max = left
        else:
            if elements[left] <= elements[right]:
                max = right
            else:
                max = left
        if elements[root] < elements [max]:
            elements[root], elements[max] = elements[max], elements[root]
            reheap_down(elements, max, bottom)



def heap_sort(values, numValues):

    '''[3]'''
    for i in range(int(numValues/2)-1, -1, -1):
        reheap_down(values, i, numValues-1)
    
    for i in range(numValues-1, 0, -1):
        values[0], values[i] = values[i], values[0]
        reheap_down(values, 0, i-1)
