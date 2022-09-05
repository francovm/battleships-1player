import unittest
from src import Battleship

class BattleshipTest(unittest.TestCase):

  def test_count_hit_ships_empty_board(self):
    board = Battleship([[" "] * 8 for x in range(8)])
    count = Battleship.count_hit_ships(board)
    self.assertEqual(count, 0)

  def test_count_hit_ships_win_condition(self):
    board = Battleship([[" "] * 8 for x in range(8)])
    for i in range(6):
      board.board[0][i] = "X"
    count = Battleship.count_hit_ships(board)
    self.assertGreater(count, 5)

if __name__ == '__main__':
    unittest.main()