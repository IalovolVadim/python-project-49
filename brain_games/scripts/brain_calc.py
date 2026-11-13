from brain_games.engine import run_game
from brain_games.games.calc import gen_calc


def main():
    run_game(gen_calc)

if __name__ == '__main__':
    main()