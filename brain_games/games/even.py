import random

LOW_BOARD = 1
UP_BOARD = 100


def gen_even():
    gen_quest = random.randint(LOW_BOARD, UP_BOARD)
    if gen_quest % 2 == 0:
        gen_answer = 'yes'
    else:
        gen_answer = 'no'
    return gen_quest, gen_answer
    
    
    
        



