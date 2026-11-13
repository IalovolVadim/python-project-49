from brain_games.engine import run_game
from brain_games.games.gcd import gen_gcd


def main():
    run_game(gen_gcd)
    

if __name__ == '__main__':
    main()