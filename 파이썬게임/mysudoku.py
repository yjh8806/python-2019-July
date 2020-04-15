class Sudoku:
    def __init__(self):
        self.welcome()
        self.answers()
        self.display()
        self.taking_answer()

    def welcome(self):
        print("welcome to sudoku!")
        print("each box is numbered starting from 0 to 80")
        print("to fill in the missing box please put the box number and the number you want followed by ,")

    def answers(self):
        global correct_answer
        global question
        correct_answer = [1,2,6,4,3,7,9,5,8,8,9,5,6,2,1,4,7,3,3,7,4,9,8,5,1,2,6,4,5,7,1,9,3,8,6,2,9,8,3,2,4,6,5,1,7,6,1,2,5,7,8,3,9,4,2,6,9,3,1,4,7,8,5,5,4,8,7,6,9,2,3,1,7,3,1,8,5,2,6,4,9]
        question = [0 for i in range(81)]
        question[1] = 2
        question[12] = 6
        question[17] = 3
        question[19] = 7
        question[20] = 4
        question[22] = 8
        question[32] = 3
        question[35] = 2
        question[37] = 8
        question[40] = 4
        question[43] = 1
        question[45] = 6
        question[48] = 5
        question[58] = 1
        question[60] = 7
        question[61] = 8
        question[63] = 5
        question[68] = 9
        question[79] = 4

    def display(self):
        global correct_answer
        global question
        global board
        board = ["_|" for i in range(81)]
        board[1] = '2|'
        board[12] = '6|'
        board[17] = '3|'
        board[19] = '7|'
        board[20] = '4|'
        board[22] = '8|'
        board[32] = '3|'
        board[35] = '2|'
        board[37] = '8|'
        board[40] = '4|'
        board[43] = '1|'
        board[45] = '6|'
        board[48] = '5|'
        board[58] = '1|'
        board[60] = '7|'
        board[61] = '8|'
        board[63] = '5|'
        board[68] = '9|'
        board[79] = '4|'

        print ('\n'.join(''.join(board[i:i+9]) for i in range(0,81,9)))

    def taking_answer(self):
        global correct_answer
        global question
        global board
        while question != correct_answer:
            direction, answer = map(int, input("num_box, number you want to put, \n(if you want to quit press 0,0) : ").split(","))
            if answer != 0:
                question[direction] = answer
                board[direction] = "%d|"%answer
                print ('\n'.join(''.join(board[i:i+9]) for i in range(0,81,9)))
            else:
                break

Sudoku()



















#
# import random
#
# dcells = []
# def sudokusize():
#     for i in range(9):
#         for j in range(9):
#             dcells.append((i,j))
#             # print(dcells)
#             return dcells
#
# def draw_problem():
#     count = 9
#     tile = '|{}'
#     for count, cell in enumerate(dcells):
#         if count % 9 == 0:
#             print()
#         elif cell == (0,1):
#             print("2|", end="")
#         elif cell == (0,3):
#             print("3|", end="")
#         elif cell == (0,7):
#             print("4|", end="")
#         elif cell == (0,8):
#             print("9|", end="")
#         elif cell == (1, 0):
#             print("8|", end="")
#         elif cell == (1, 8):
#             print("6|", end="")
#         elif cell == (2, 1):
#             print("6|", end="")
#         elif cell == (2, 3):
#             print("5|", end="")
#         elif cell == (3, 1):
#             print("4|", end="")
#         elif cell == (3, 5):
#             print("1|", end="")
#         elif cell == (3, 6):
#             print("6|", end="")
#         elif cell == (4, 2):
#             print("6|", end="")
#         elif cell == (4, 6):
#             print("3|", end="")
#         elif cell == (5, 0):
#             print("9|", end="")
#         elif cell == (5, 7):
#             print("2|", end="")
#         elif cell == (6, 0):
#             print("4|", end="")
#         elif cell == (6, 2):
#             print("3|", end="")
#         elif cell == (6, 4):
#             print("2|", end="")
#         elif cell == (6, 6):
#             print("5|", end="")
#         elif cell == (7, 0):
#             print("2|", end="")
#         elif cell == (7, 5):
#             print("9|", end="")
#         elif cell == (7, 8):
#             print("7|", end="")
#         elif cell == (8, 5):
#             print("8|", end="")
#         else:
#             print(" |", end="")
#
#
# sudokusize()
# draw_problem()
