"""
    to determine whether the number is odd or even :)
"""
import random

'''
code for num 0 to 10
'''
# data

num = []
for number in range(0, 11):
    num.append(number)

# collecting data

'''
ore is getting input (odd or even) from user
in_num is getting number (0 - 10) input  from the user 
a_num is random number selected by module 'random'
'''

# from user
ore = input("'O' odd or 'E' even -> ")
in_num = int(input('Enter a number from 0 to 10 -> '))
ore = ore[:1]
# from random
a_num = random.choice(num)
print(f'computer chose ->{a_num} ')

# Formula

'''
total is the sum of user and computer value
formula is to find the total value is even or not
'''

total = a_num + in_num
print(f'Total -> {total}')
formula = total % 2

# The Brain

"""
It finds weather This is 'odd' or 'even'
    formula = value
    
    Engine will return True or false
        True means Even
        False means Odd
"""


def Engine(value):
    if value == 0:
        return True
    else:
        return False


'''
Win Engine
    if the Engine = Formula 
        then it is even
    else 
        it is odd
'''


def WinEngine():
    if Engine(value=formula):
        print('The number is Even')
        if ore == 'e':
            print('You Won')
        else:
            print('You Lost')

    else:
        print('The number is Odd')
        if ore == 'o':
            print('You Won')
        else:
            print('You lost')


# result
'''
It shows the result
'''

Engine(value=formula)
WinEngine()
