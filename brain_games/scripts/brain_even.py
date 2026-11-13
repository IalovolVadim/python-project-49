from brain_games.engine import run_game
from brain_games.games.even import gen_even


def main():
    run_game(gen_even)
    

if __name__ == '__main__':
    main()
