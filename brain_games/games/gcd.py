import random

LOW_BOARD = 1
UP_BOARD = 100


def gen_gcd():
    num_one = random.randint(LOW_BOARD,UP_BOARD)
    num_two = random.randint(LOW_BOARD,UP_BOARD)
    num_min, num_max = min(num_one,num_two), max(num_one,num_two)
    both_divs = []
    for char in range(1, num_min + 1):
        if num_min % char == 0 and num_max % char == 0:
            both_divs.append(char)
    max_div = both_divs[-1]
    return f'{num_one} {num_two}', max_div
    