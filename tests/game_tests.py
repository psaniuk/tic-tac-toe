import unittest
from app.model import *

class GameTests(unittest.TestCase):
    def test_create_game_assume_isCompleted_false(self):
        game = Game(3)
        self.assertFalse(game.isCompleted())
    
    def test_create_game_assume_getResult_returns_grid_cells(self):
        game = Game(3)
        result = game.getResult()
        self.assertTrue(len(result) == 3)
        self.assertTrue(len(result[0]) == 3)
    
    def test_play_assume_grid_updated(self):
        size = 3
        game = Game(size)
        for i in range(size * size):
            game.play(i)
            row = i // size
            col = i % size
            self.assertTrue(game.getResult()[row][col] is not None)
    
    def test_play_with_extra_move_assume_exception_raise(self):
        size = 3
        game = Game(size)
        with self.assertRaises(NoMovesAvailableException):
            _ = [game.play(i) for i in range(size * size + 1)]
        