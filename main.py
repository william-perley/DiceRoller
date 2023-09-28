# This python code will roll dice for D&D
# The first input will be the number of side for the dice to roll
# The second number will have you input the number of dice total to roll

import random

total = 0

if __name__ == '__main__':
    while 1 == 1:
        print('To exit, type -1')
        print('What sided die are you rolling?')
        sidedDie = int(input())
        if sidedDie == -1:
            exit()
        print('How many dice are you rolling?')
        numberOfDice = int(input())
        if numberOfDice == -1:
            exit()
        # print('Sided die is {} and Number of dice is {}'.format(sidedDie, numberOfDice))
        for die in range(numberOfDice):
            rolledDice = random.randint(1, sidedDie)
            print(rolledDice)
            total += rolledDice
        print('\nTotal is {}\n'.format(total))
        total = 0
