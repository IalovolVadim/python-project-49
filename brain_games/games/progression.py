import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START_NUMBER = 1
MAX_START_NUMBER = 100
MIN_STEP = 1
MAX_STEP = 10


def gen_progression():
    len_pr = random.randint(MIN_LENGTH, MAX_LENGTH)
    mystery_index = random.randint(0, len_pr - 1)
    start_num = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    finish_num = start_num + step * (len_pr - 1)
    collection_pr = [num for num in range(start_num, finish_num + 1, step)]
    gen_answer = collection_pr[mystery_index]
    for i in range (len_pr):
        if i != mystery_index:
            collection_pr[i] = str(collection_pr[i])
        else:
            collection_pr[i] = '..'
    gen_quest = ' '.join(collection_pr)
    return gen_quest, gen_answer

    