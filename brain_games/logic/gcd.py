import random 


def gen_gcd():
    num_one = random.randint(1,100)
    num_two = random.randint(1,100)
    num_min, num_max = min(num_one,num_two), max(num_one,num_two)
    both_divs = []
    for char in range(1, num_min + 1):
        if num_min % char ==0 and num_max % char == 0:
            both_divs.append(char)
    max_div = both_divs[-1]
    return f'{num_one} {num_two}', max_div
    