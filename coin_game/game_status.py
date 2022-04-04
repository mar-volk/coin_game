from __future__ import annotations
import copy
from typing import List


MAX_ROWS = 4


class GameStatus:
    def __init__(self, coin_placements: List[int] = None):
        # ToDo: make this inependant of game size
        self.coin_placements = (
            coin_placements if coin_placements is not None else [1, 2, 3, 4]
        )
        self._is_winning_position = True if sum(self.coin_placements) == 0 else None
        self._winning_moves = None
        self.is_finished = True if sum(self.coin_placements) == 0 else None

    def remove_coin(self, pos: int) -> None:
        assert pos in range(MAX_ROWS)
        self.coin_placements[pos] -= 1
        self.validate()

    def analyze(self):
        _ = self.is_winning_position()

    def is_winning_position(self) -> bool:
        if sum(self.coin_placements) == 0:
            # It is my turn and I no coin is remaining
            self._is_winning_position = True
            return True
        else:
            # Create all possible moves and situation of opponent after move
            valid_moves = self.get_valid_moves()
            option_space = {}  # move: new_status
            for move in valid_moves:
                status_for_opponent = self.copy()
                status_for_opponent.remove_coin(move)
                option_space[move] = status_for_opponent

            tmp_winning_moves = []
            for move, opponent_status in option_space.items():
                if not opponent_status.is_winning_position():
                    tmp_winning_moves.append(move)
            self._winning_moves = tmp_winning_moves
            self._is_winning_position = len(tmp_winning_moves) > 0
            return len(tmp_winning_moves) > 0

    def copy(self) -> GameStatus:
        return copy.deepcopy(self)

    def get_valid_moves(self) -> List[int]:
        return [
            pos
            for pos in range(len(self.coin_placements))
            if self.coin_placements[pos] > 0
        ]

    def validate(self) -> None:
        """Raises Error if self.coin_placements is invalid"""
        for pos in range(len(self.coin_placements)):
            if self.coin_placements[pos] < 0:
                raise InvalidGameStatusError(
                    f"Expected >= 0 coins on position {pos} but found {self.coin_placements[pos]}"
                )


class InvalidGameStatusError(Exception):
    """The game status is invalid"""

    pass
