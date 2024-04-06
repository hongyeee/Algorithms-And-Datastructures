
def selection_sort(values):

    '''[9]'''
    end = len(values)
    for i in range(0, end, 1):
        for j in range(i+1, end, 1):
            if values[j] < values[i]:
                values[i], values[j] = values[j], values[i]
        