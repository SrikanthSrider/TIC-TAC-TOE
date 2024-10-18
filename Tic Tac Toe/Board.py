#download this file
import numpy as np
from copy import deepcopy 
class Board:
    def __init__(
            self, board = np.zeros((3,3), dtype= int), \
            diagonal = None, antidiagonal = None, \
            rows = None, columns = None
            ) -> None:
        
        self.board = board
        

    def __available_moves(self):
        return np.array([(x,y) for x in range(len(self.board)) for y in range(len(self.board)) if self.board[x][y] == 0])
    
    def __available_rows(self):
        return np.array(list(set([x + 1 for x in range(len(self.board)) for y in range(len(self.board)) if self.board[x][y] == 0 ])))

    def __available_columns(self):
        return np.array(list(set([y for x in range(len(self.board)) for y in range(len(self.board)) if self.board[x][y] == 0 ])))
    
    def __diagonal(self):
        return self.board.diagonal()
    
    def __antidiagonal(self):
        return np.fliplr(self.board).diagonal()
    
    def __rows(self):
        return self.board
    
    def __columns(self):
        return np.array( [self.board[:,x] for x in range(len(self.board)) ] )


    def display_board(self):
        printing_board = self.board.tolist()
        for x in range(len(printing_board)):
            for y in range(len(printing_board)):
                if printing_board[x][y] == 1:
                    printing_board[x][y] = '[X]'
                elif printing_board[x][y] == 2:
                    printing_board[x][y] = '[O]'
                else:
                    if y == 0:
                        printing_board[x][y] = '[ ]'
                    if y == 1:
                        printing_board[x][y] = '[ ]'
                    if y == 2:
                        printing_board[x][y] = '[ ]'
                    
        print(f"This is the board: ")
        for x in range(len(printing_board)):
            for y in range(len(printing_board[x])):
                if y == 0 or y == 1:
                    print(printing_board[x][y], sep= ' ', end= '')
                else:
                    print(printing_board[x][y], sep= ' ', end= "\n")

        return None

    def __get_coord_row(self, markerobj):
        available_rows = self.__available_rows()
        coord_row = input(f"Enter the coordinate of the row you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, available_rows))  )
        while True:
            try:
                coord_row = int(coord_row)
            except:
                print(f"You have not entered valid row input. Try again.")
                coord_row = input(f"Enter the coordinate of the row you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, available_rows)))
            else:
                if coord_row not in available_rows:
                    print(f"You have not entered a valid row. Try again")
                    coord_row = input(f"Enter the coordinate of the row you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, available_rows)))
                else:
                    print(f"Valid row coordinate: {coord_row}")
                    return coord_row

    def __get_coord_column(self, markerobj, col_due_to_sel_row):
        coord_column = input(f"Enter the coordinate of the column you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, col_due_to_sel_row)) + \
                            "\n(Enter -1 to go back to rows)" )
        while True:
            try:
                coord_column = int(coord_column)
            except:
                print(f"You have not entered valid column input. Try again.")
                coord_column = input(f"Enter the coordinate of the column you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, col_due_to_sel_row)) + \
                            "\n(Enter -1 to go back to rows)" )
            else:
                if coord_column not in col_due_to_sel_row:
                    if coord_column == -1:
                        return coord_column
                    else:
                        print(f"You have not entered a valid column. Try again")
                        coord_column = input(f"Enter the coordinate of the column you would to place your {markerobj}. Valid inputs are: " + ", ".join(map(str, col_due_to_sel_row)) + \
                                "\n(Enter -1 to go back to rows)" )
                else:
                    return coord_column


    def get_player_move(self, player):
        if player == True:
            turn = "Player 1"
            markerobj = "cross"

        elif player == False:
            turn = "Player 2"
            markerobj = "circle"

        coordinates = []
        
        print(f"It is {turn}"+ "'s" + " turn")

        coord_row = self.__get_coord_row(markerobj)
        available_moves = self.__available_moves()
        
        while True:
            col_due_to_row = [y + 1 for [x, y] in available_moves if x == coord_row - 1 ]
            coord_column = self.__get_coord_column(markerobj, col_due_to_row)
            if coord_column == -1:
                print("Going back to rows")
                coord_row = self.__get_coord_row(markerobj)
            else:
                coordinates.append(coord_row - 1)
                coordinates.append(coord_column - 1)
                print(f"Valid column coordinate: {coord_column}")
                print(f"Your coordinates are row = {coord_row} and column = {coord_column}")
                return coordinates

    def make_player_move(self, coords, player):
        if player == True:
            marker = 1
        elif player == False:
            marker = 2

        from copy import deepcopy
        new_board = deepcopy(self.board)
        new_board[coords[0]][coords[1]] = marker
        return new_board

    def get_winner(self):
        available_moves = self.__available_moves()
        diagonal = self.__diagonal()
        antidiagonal = self.__antidiagonal()
        rows = self.__rows()
        columns = self.__columns()

        if all((x in [1] for x in diagonal)) == True or \
            all((x in [1] for x in antidiagonal)) == True or \
            any([all((y in [1] for y in x)) for x in rows]) or \
            any([all((y in [1] for y in x)) for x in columns]):
            winner = 1

        elif all((x in [2] for x in diagonal)) == True or \
            all((x in [2] for x in antidiagonal)) == True or \
            any([all((y in [2] for y in x)) for x in rows]) or \
            any([all((y in [2] for y in x)) for x in columns]):
            winner = 2

        else:
            if len(available_moves) == 0:
                winner = 0
            else:
                winner = -1

        return winner
