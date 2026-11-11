from brain_games.cli import welcome_user
import prompt
import random


def part_game(func_gen): 
    gen_quest,gen_answer = func_gen()
    user_answer = prompt.string(f'Quesion: {gen_quest}\nYour answer:')
    if user_answer == str(gen_answer):
        return 'Correct!'
    else:
        return f'{user_answer} is wrong answer ;(. Correct answer was {str(gen_answer)}'



def run_game(func_gen):
    name = welcome_user()
    count_correct = 0
    while count_correct < 3:
        result = part_game(func_gen)
        if result == 'Correct!':    
            count_correct += 1
            print(result)
        else:
            
            print(result)
            break 
    if count_correct == 3:
        print(f'Congratulations, {name}!')
        

    
     

    