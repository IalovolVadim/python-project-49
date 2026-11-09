from brain_games.cli import welcome_user
import prompt
import random


def part_game(func):
    get_value = func('', None)
    user_answer = prompt.string(f'Question: {get_value}\nYour answer:')
    if not func(user_answer, get_value):
        return 'Correct!'
    else: 
        return f'{user_answer} is wrong answer ;(. Correct answer was {func(user_answer, get_value)}'


def run_game(func, count_correct = 1, name = ''):
    if count_correct == 1:
        name = welcome_user()
    part_result = part_game(func)
    if count_correct < 3: 
        if part_result == 'Correct!':
            count_correct += 1
            print(part_result)
            run_game(func,count_correct, name)
        else:
            print(f"{part_result}\nLet's try again,{name}")
    else:
        print(f'Congratulations, {name}!')  
        

    
     

    