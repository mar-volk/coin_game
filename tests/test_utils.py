import unittest
from unittest import TestCase
import pytest
from coin_game import GameStatus
from coin_game.game_status import InvalidGameStatusError


class TestGameStatus(TestCase):
    def test_init(self):
        gs = GameStatus()
        self.assertEqual(gs.coin_placements, [1, 2, 3, 4])

        gs1 = GameStatus([1, 1, 1])
        self.assertEqual(gs1.coin_placements, [1, 1, 1])

    def test_remove_coin(self):
        gs = GameStatus([1, 2, 3, 4])
        gs.remove_coin(pos=2, num=1)
        self.assertEqual(gs.coin_placements, [1, 2, 2, 4])

        gs = GameStatus([1, 2, 3, 4])
        gs.remove_coin(pos=1, num=1)
        gs.remove_coin(pos=1, num=1)
        with pytest.raises(InvalidGameStatusError):
            gs.remove_coin(pos=1, num=1)

        # remove 3 coins
        gs = GameStatus([4, 3])
        gs.remove_coin(pos=1, num=3)
        self.assertEqual(gs.coin_placements, [4, 0])

    def test_copy(self):
        gs_org = GameStatus([1, 2, 3, 4])
        gs_copy = gs_org.copy()
        gs_copy.remove_coin(pos=3, num=1)
        self.assertEqual(gs_copy.coin_placements, [1, 2, 3, 3])
        self.assertEqual(gs_org.coin_placements, [1, 2, 3, 4])

    def test_validate(self):
        gs = GameStatus([1, 2])
        gs.remove_coin(pos=0, num=1)
        with pytest.raises(InvalidGameStatusError):
            gs.remove_coin(pos=0, num=1)

    def test_get_valid_moves(self):
        gs = GameStatus([1, 1, 1])
        val_moves = gs.get_valid_moves()
        self.assertEqual(val_moves, [(0, 1), (1, 1), (2, 1)])

        gs = GameStatus([0, 1, 2])
        val_moves = gs.get_valid_moves()
        self.assertEqual(val_moves, [(1, 1), (2, 1), (2, 2)])

    def test_is_winning_position(self):
        gs = GameStatus([0, 0, 0])
        self.assertTrue(gs.is_winning_position())

        gs = GameStatus([1, 0, 1])
        self.assertTrue(gs.is_winning_position())

        gs = GameStatus([0, 1, 0])
        self.assertFalse(gs.is_winning_position())

        gs = GameStatus([1, 1, 1])
        self.assertFalse(gs.is_winning_position())

    def test_analyze(self):
        gs = GameStatus([1, 0, 1], verbose=False)
        self.assertIsNone(gs._is_winning_position)
        gs.analyze()
        self.assertEqual(gs._is_winning_position, True)

    def test_is_finished(self):
        gs = GameStatus([0, 0, 0])
        self.assertTrue(gs.is_finished())

        gs = GameStatus([1, 0, 0])
        self.assertFalse(gs.is_finished())


if __name__ == "__main__":
    unittest.main()
