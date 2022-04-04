"""Script to generate table of all possible statuses in game and winning moves"""

from game_status import GameStatus
from tqdm import tqdm


if __name__ == "__main__":
    possible_game_statuses = []
    for pos0 in range(2):
        for pos1 in range(3):
            for pos2 in range(4):
                for pos3 in range(5):
                    possible_game_statuses.append([pos0, pos1, pos2, pos3])

    print(f"Number of possible game statuses: {len(possible_game_statuses)}")

    winnging_moves = []
    for status in tqdm(possible_game_statuses):
        gs = GameStatus(status, verbose=False)
        gs.analyze()
        winnging_moves.append(gs._winning_moves)

    print("# Status, Winning moves (position, numer of coins to remove):")
    for status, wm in zip(possible_game_statuses, winnging_moves):
        print(status, wm)

    print("finished")
