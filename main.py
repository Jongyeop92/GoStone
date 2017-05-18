# -*- coding: utf8 -*-

import copy

BLACK = "X"
WHITE = "O"

B = BLACK
W = WHITE

def change(color):
    if color == B:
        return W
    else:
        return B

def flip(board, command):
    copyBoard = copy.deepcopy(board)
    
    if command[0] in ["r", "R"]:
        row = True
    else:
        row = False

    idx = int(command[1]) - 1

    if row:
        for i in range(len(board[0])):
            copyBoard[idx][i] = change(board[idx][i])
    else:
        for i in range(len(board)):
            copyBoard[i][idx] = change(board[i][idx])
    
    return copyBoard

def showBoard(board):
    print "\n".join("".join(row) for row in board)

def test():
    board = [[W, W, W, W, W],
             [B, B, B, B, B]]

    assert change(B) == W
    assert change(W) == B

    assert flip(board, "r1") == [[B, B, B, B, B],
                                 [B, B, B, B, B]]
    assert flip(board, "c1") == [[B, W, W, W, W],
                                 [W, B, B, B, B]]

    showBoard(board)
    print
    
    print "Success"

def main():
    puzzle = [[B, W, B, B, B],
              [W, B, W, B, W],
              [B, W, W, W, B],
              [W, B, W, W, B],
              [B, W, B, W, B]]

    answer = [[B, B, B, W, W],
              [B, B, B, B, W],
              [B, B, W, B, W],
              [B, B, B, W, B],
              [B, B, B, B, W]]

    nowBoard = copy.deepcopy(puzzle)
    count = 0

    while nowBoard != answer:
        print
        showBoard(nowBoard)
        print
        
        command = raw_input("Command: ")
        nowBoard = flip(nowBoard, command)

        count += 1

    print
    showBoard(answer)
    print
    print "Complete!"
    print "Count: %d" % count

if __name__ == "__main__":
    #test()
    main()
