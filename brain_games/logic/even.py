import random


def gen_even():
    gen_quest = random.randint(1,100)
    if gen_quest % 2 == 0:
        gen_answer = 'yes'
    else:
        gen_answer = 'no'
    return gen_quest, gen_answer
    
    
    
        



