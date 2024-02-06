import unittest
from app.model import *

class GridTests(unittest.TestCase):
    def test_create_grid_assume_getCells_returns_array_with_the_given_size(self):
        size = 3
        grid = Grid(size)
        self.assertEqual(len(grid.getCells()), size)
        self.assertEqual(len(grid.getCells()[0]), size)

    def test_move_assume_getCells_retruns_correct_cell(self):
        grid = Grid(3)
        player = Player.createXplayer()
        grid.move(player, 1, 2)
        self.assertTrue(grid.getCells()[1][2] == player)
    
    def test_create_grid_get_cells_assume_all_None(self):
        grid = Grid(3)
        for row in grid.getCells():
            notNone = list(filter(lambda player: player is not None, row))
            self.assertTrue(len(notNone) == 0)
    
    def test_given_3x3_grid_move_assume_no_winner(self):
        grid = Grid(3)
        grid.move(Player.createOplayer(), 0, 0)
        self.assertTrue(grid.getWinner() is None)
    
    def test_given_3x3_grid_fill_middle_row_with_X_assume_getWinner_returns_playerX(self):
        grid = Grid(3)
        playerX = Player.createXplayer()
        grid.move(playerX, 1, 0)
        grid.move(playerX, 1, 1)
        grid.move(playerX, 1, 2)
        self.assertTrue(grid.getWinner() is playerX)
    
    def test_given_3x3_grid_fill_middle_row_with_X_and0_assume_getWinner_returns_None(self):
        grid = Grid(3)
        playerX = Player.createXplayer()
        grid.move(playerX, 1, 0)
        grid.move(playerX, 1, 1)
        grid.move(Player.createOplayer(), 1, 2)
        self.assertTrue(grid.getWinner() is None)
    
    def test_given_3x3_grid_with_spare_result_assume_getWinner_returns_None(self):
        size = 3
        grid = Grid(size)
        playerX = Player.createXplayer()
        playerO = Player.createOplayer()
        row = 0
        for col in range(size):
            if col % 2 == 0:
                grid.move(playerX, row, col)
            else:
                grid.move(playerO, row, col)
            row += 1
        self.assertTrue(grid.getWinner() is None)

    def test_given_3x3_grid_with_playerX_winner_by_colls_assume_getWinner_returns_player_X(self):
        row = 0
        size = 3
        while row < size:
            grid = Grid(size)
            playerX = Player.createXplayer()
            for col in range(size):
                grid.move(playerX, row, col)
            self.assertEqual(grid.getWinner(), playerX)
            self.assertNotEqual(grid.getWinner(), Player.createOplayer())
            self.assertNotEqual(grid.getWinner(), None)
            row += 1
    
    def test_given_3x3_grid_with_playerX_winner_by_primary_diagonal_assume_getWinner_returns_player_X(self):
        grid = Grid(3)
        playerX = Player.createXplayer()
        grid.move(playerX, 0, 0)
        grid.move(playerX, 1, 1)
        grid.move(playerX, 2, 2)
        self.assertEqual(grid.getWinner(), playerX)
        self.assertNotEqual(grid.getWinner(), Player.createOplayer())
        self.assertNotEqual(grid.getWinner(), None)

    def test_given_3x3_grid_with_playerX_winner_by_secondary_diagonal_assume_getWinner_returns_player_X(self):
        grid = Grid(3)
        playerX = Player.createXplayer()
        grid.move(playerX, 0, 2)
        grid.move(playerX, 1, 1)
        grid.move(playerX, 2, 0)
        self.assertEqual(grid.getWinner(), playerX)
        self.assertNotEqual(grid.getWinner(), Player.createOplayer())
        self.assertNotEqual(grid.getWinner(), None)

    def test_player_createXplayer(self):
        self.assertTrue(Player.createXplayer().getMark() == "X")
    
    def test_player_createOplayer(self):
        self.assertTrue(Player.createOplayer().getMark() == "O")
    
