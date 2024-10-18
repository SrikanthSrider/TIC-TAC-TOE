#run this file
from Board import Board

Mainboard = Board()
player = True

while True:
    Mainboard.display_board()
    coords = Mainboard.get_player_move(player)
    Mainboard.board = Mainboard.make_player_move(coords, player)
    winner = Mainboard.get_winner()
    if winner == 1 or winner == 2:
        Mainboard.display_board()
        print(f"The winner is Player {winner}!")
        break
    elif winner == 0:
        Mainboard.display_board()
        print(f"It is a tie!")
        break
    elif winner == -1:
        player = not player
