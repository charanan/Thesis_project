from input_utils import load_input
from puzzle import solve_puzzle
from print import print_result_board


### USER DEFINED ###
W, H, shapes = load_input("input.txt")

### SOLVING PUZZLE ###
result_board = solve_puzzle(W, H, shapes)

if result_board:
    ### PRINT RESULT ###
    print_result_board(W, H, result_board)

else:
    print("No solution")
