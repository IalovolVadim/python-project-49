import random

LOW_BOARD = 1
UP_BOARD = 100


def gen_calc():
    num_one = random.randint(LOW_BOARD,UP_BOARD)
    num_two = random.randint(LOW_BOARD,UP_BOARD)
    sign = random.choice('+-*')
    match sign:
        case '+':
            gen_quest = str(num_one) + ' + ' + str(num_two)
            gen_answ = num_one + num_two
        case '-':
            gen_quest = str(num_one) + ' - ' + str(num_two)
            gen_answ = num_one - num_two  
        case '*':
            gen_quest = str(num_one) + ' * ' + str(num_two)
            gen_answ = num_one * num_two
    return gen_quest, gen_answ    







