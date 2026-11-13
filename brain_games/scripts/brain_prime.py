from brain_games.engine import run_game
from brain_games.games.prime import gen_prime


def main():
    run_game(gen_prime)
    

if __name__ == '__main__':
    main()