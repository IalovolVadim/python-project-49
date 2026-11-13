import random

LOW_BOARD = 0
UP_BOARD = 100


def gen_prime():
    number = random.randint(LOW_BOARD, UP_BOARD)
    gen_quest = number
    gen_answer = None
    div = 2
    if number > 1:
        while div < round(number**0.5) + 1:
            if number % div != 0:
                div += 1
            else: 
                gen_answer = 'no'
                break
        if not gen_answer:
            gen_answer = 'yes'
    else:
        gen_answer = 'no'
    return gen_quest, gen_answer 
    
