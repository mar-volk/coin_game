from __future__ import annotations
import copy
from typing import List, Tuple


MAX_ROWS = 4


class GameStatus:
    def __init__(self, coin_placements: List[int] = None, verbose: bool = True) -> None:
        self.coin_placements = (
            coin_placements if coin_placements is not None else [1, 2, 3, 4]
        )
        self._is_winning_position = True if sum(self.coin_placements) == 0 else None
        self._winning_moves = None
        self.verbose = verbose
        self.validate()

    def remove_coin(self, pos: int, num: int) -> None:
        assert pos in range(MAX_ROWS)
        self.coin_placements[pos] -= num
        self.validate()

    def analyze(self) -> None:
        _ = self.is_winning_position()
        if self.verbose:
            self.print_status()

    def is_winning_position(self) -> bool:
        if sum(self.coin_placements) == 0:
            # It is my turn. If no coin is remaining, then I am the winner.
            self._is_winning_position = True
            return True
        else:
            # Create all possible moves and situation of opponent after move
            moves = self.get_valid_moves()
            statuses_after_move = []
            for move in moves:
                status_for_opponent = self.copy()
                status_for_opponent.remove_coin(pos=move[0], num=move[1])
                statuses_after_move.append(status_for_opponent)

            tmp_winning_moves = []
            for move, opponent_status in zip(moves, statuses_after_move):
                if not opponent_status.is_winning_position():
                    tmp_winning_moves.append(move)
            self._winning_moves = tmp_winning_moves
            self._is_winning_position = len(tmp_winning_moves) > 0
            return len(tmp_winning_moves) > 0

    def copy(self) -> GameStatus:
        return copy.deepcopy(self)

    def get_valid_moves(self) -> List[Tuple[int, int]]:
        valid_moves = []
        for pos in range(len(self.coin_placements)):
            for num_removed_coins in range(1, self.coin_placements[pos] + 1):
                valid_moves.append((pos, num_removed_coins))
        return valid_moves

    def validate(self) -> None:
        """Raises Error if self.coin_placements is invalid"""
        for pos in range(len(self.coin_placements)):
            if self.coin_placements[pos] < 0:
                raise InvalidGameStatusError(
                    f"Expected >= 0 coins on position {pos} but found {self.coin_placements[pos]}"
                )

    def print_status(self) -> None:
        print(f"coin_placement: {self.coin_placements}")
        for num_coins in self.coin_placements:
            if num_coins == 0:
                print("_")
            else:
                print("●" * num_coins)
                pass

        if self._is_winning_position is None:
            print("The situation was not been analyzed, yet.")
        elif not self._is_winning_position:
            print("If your opponent makes everything right, he will win.")
        elif self._is_winning_position:
            print("If you do everything right, you can win.")

        print(
            f"Winning moves (position, number of coins to remove): {self._winning_moves}"
        )

        if self.is_finished():
            print("The game is finished.")
        else:
            print("The game is not finished.")

    def is_finished(self) -> bool:
        if sum(self.coin_placements) == 0:
            return True
        else:
            return False


class InvalidGameStatusError(Exception):
    """The game status is invalid"""

    pass
