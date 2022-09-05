import random
from src.constants import NUMBER_SHIPS,BOARD_SIZE


class Battleship:
  """A class to make it easier to understand the code. Contains methods that make the game works
  """
  def __init__(self, board):
      self.board = board

  def create_ships(self):
    """Randomly place down ships in the board

    Returns:
        board: board with the position of teh ships mark as X
        ships: Coordinates location for each ships in a list.
    """
    self.ships = []
    for i in range(NUMBER_SHIPS):
        self.x_row, self.y_column = random.randint(
            0, 7), random.randint(0, BOARD_SIZE-1)
        while self.board[self.x_row][self.y_column] == "X":
            self.x_row, self.y_column = random.randint(
                0, 7), random.randint(0, BOARD_SIZE-1)
        self.board[self.x_row][self.y_column] = "X"
        self.ships.append([self.x_row, self.y_column])
    return self.board, self.ships

  def get_user_input(self):
    """Get valid row and column to place bullet shot"

    Returns:
        x,y: the coordinates (row and column ) of the shot.
    """
    try:
        x_row = input("Enter the row of the ship: ")
        while x_row not in '12345678' or int(x_row) > 10:
            print('Not an appropriate choice, please select a valid row')
            x_row = input("Enter the row of the ship: ")

        y_column = input("Enter the column of the ship: ")
        while y_column not in "12345678" or int(y_column) > 10:
            print('Not an appropriate choice, please select a valid column')
            y_column = input("Enter the column of the ship: ")
        return int(x_row)-1, int(y_column)-1
    except ValueError and KeyError:
        print("Not a valid input")
        return self.get_user_input()

  def count_hit_ships(self):
    """Count the number of ships has been hit. 

    Returns:
        hit_ships: Number of hit ships.
    """
    hit_ships = 0
    for row in self.board:
        for column in row:
            if column == "X":
                hit_ships += 1
    return hit_ships


def create_message(x, y, ships):
  """Create a message if the shot is hot, warm or cold

  Args:
      x (int): row
      y (int): column
      ships (list): list of coordinates

  Returns:
      message: list with message per ship
  """
  message = []
  for i in range(len(ships)):
      x_guess, y_guess = x, y
      if (abs(x_guess-ships[i][0]) +
              abs(y_guess-ships[i][1])) <= 2:
          message.append("SHIP_{0}:HOT".format(i+1))
      else:
          if (abs(x_guess-ships[i][0]) +
                  abs(y_guess-ships[i][1])) <= 4:
              message.append("SHIP_{0}:WARM".format(i+1))
          else:
              message.append("SHIP_{0}:COLD".format(i+1))
  return message
