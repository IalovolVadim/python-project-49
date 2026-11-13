from brain_games.engine import run_game
from brain_games.games.progression import gen_progression


def main():
    run_game(gen_progression)
    

if __name__ == '__main__':
    main()