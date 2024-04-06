def insertion_sort(values):
    
    '''[4]'''
    for i in range(0, len(values), 1):
        current = i
        finished = False
        search = (current != 0)
        while search and not finished:
            if values[current] < values[current-1]:
                values[current], values[current-1] = values[current-1], values[current]
                current -= 1
                search = (current != 0)
            else:
                finished = True
