from Copy import *


if __name__ == '__main__':


    stack1 = StackType()
    stack2 = StackType()

    stack1.push('1')
    stack1.push('2')
    stack1.push('3')
    print(stack1)


    stack2.copy(stack1)
    print(stack2)

    print()

    stack2.pop()
    stack2.push('7')


    print(stack1)
    print(stack2)

    
