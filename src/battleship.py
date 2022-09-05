import random
from src.constants import NUMBER_SHIPS

          
class Battleship:
  def __init__(self, board):
    self.board = board

  def create_ships(self):
    self.ships = []
    for i in range(NUMBER_SHIPS):
      self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      while self.board[self.x_row][self.y_column] == "X":
        self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
      self.board[self.x_row][self.y_column] = "X"
      self.ships.append([self.x_row,self.y_column])
    return self.board, self.ships


  def get_user_input(self):
    try:
      x_row= input("Enter the row of the ship: ")
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
    hit_ships = 0
    for row in self.board:
      for column in row:
        if column == "X":
          hit_ships += 1
    return hit_ships

def create_message(x,y,ships):
    message = []
    for i in range(len(ships)):
        x_guess,y_guess = x,y
        if (abs(x_guess-ships[i][0])+
              abs(y_guess-ships[i][1])) <= 2:
            message.append("SHIP_{0}:HOT".format(i+1))    
        else:
            if (abs(x_guess-ships[i][0])+
              abs(y_guess-ships[i][1])) <= 4:
                message.append("SHIP_{0}:WARM".format(i+1))
            else:
                message.append("SHIP_{0}:COLD".format(i+1))
    return message

