def factorial(number):
    '''[3]'''
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
