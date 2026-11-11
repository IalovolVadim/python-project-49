import random 


def gen_calc():
    num_one = random.randint(1,100)
    num_two = random.randint(1,100)
    sign = random.choice('+-*')
    gen_quest, gen_answ = ('', 0)
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







