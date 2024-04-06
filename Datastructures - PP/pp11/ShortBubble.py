
def short_bubble(values, numValues):
    '''[10]'''
    current = 0
    sorted = False
    while current < numValues -1 and not sorted:
        bubble_up(values, current, numValues -1, sorted)
        current += 1

def bubble_up(values, startIndex, endIndex, sort):
    '''[11]'''
    sort = True
    for i in range(endIndex, startIndex, -1):
        if values[i] < values[i-1]:
            values[i], values[i-1] = values[i-1], values[i]
            sort = False