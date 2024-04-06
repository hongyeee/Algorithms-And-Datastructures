
def bubble_sort(values):
    """[1]"""
    current  = 0
    length = len(values) -1
    while current < length:
        for i in range(length, current, -1):
            if values[i]<values[i-1]:
                values[i], values[i-1] = values[i-1], values[i]
        current += 1





