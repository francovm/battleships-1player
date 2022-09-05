
from src import Battleship,create_message
from src import BOARD_SIZE,NUMBER_GUESS,NUMBER_SHIPS


def RunGame(): 
  computer_board = Battleship([[" "] * BOARD_SIZE for i in range(BOARD_SIZE)])
  user_guess_board = Battleship([[" "] * BOARD_SIZE for i in range(BOARD_SIZE)])
  board, ships_location = Battleship.create_ships(computer_board)

  turns = NUMBER_GUESS
  while turns > 0:
    
    #get user input
    user_x_row, user_y_column = Battleship.get_user_input(object)
    
    #check if duplicate guess
    while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
      print("You guessed that one already")
      user_x_row, user_y_column = Battleship.get_user_input(object)
    
    #check for hit or miss
    if computer_board.board[user_x_row][user_y_column] == "X":
      print("You sunk 1 of my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "X"
      ships_location.remove([user_x_row,user_y_column])
    else:
      # print("You missed my battleship!")
      user_guess_board.board[user_x_row][user_y_column] = "-"
      for i in create_message(user_x_row,user_y_column,ships_location):print(i)
        
              
    #check for win or lose
    if Battleship.count_hit_ships(user_guess_board) == NUMBER_SHIPS:
      print("You hit all 5 battleships! You WIN")
      break
    else:
      turns -= 1
      print(f"You have {turns} turns remaining")
      if turns == 0:
        print("Sorry you ran out of turns, GAME OVER")
        break

if __name__ == '__main__':
  RunGame()