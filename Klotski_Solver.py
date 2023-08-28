import copy
from PIL import Image

# Converts 5 x 4 matrix to unique 20 digit integer
# Returns the integer representation
def board_to_int(board):
    hash_value = 0
    multiplier = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            hash_value += board[i][j]*multiplier
            multiplier *= 10
    return hash_value

# Converts 20 digit integer to unique 5 x 4 matrix
# Returns the array representaion
def int_to_board(value):
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    multiplier = 10
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = (value % multiplier) * 10 // multiplier
            multiplier *= 10
    return board

# Swaps position (a,b) with position (x,y)
def swap(board, a, b, x, y):
    temp = board[a][b]
    board[a][b] = board[x][y]
    board[x][y] = temp

# Returns a list of integers representing all positions reachable 
# by a single legal move from the current board (according to the rules of Klotski)
def generate_children(board):
    children = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 0):
                if(i > 0):
                    if(board[i-1][j] == 1):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i-1, j)
                        children.append(board_to_int(temp))
                    if(board[i-1][j] == 2):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i-2, j)
                        children.append(board_to_int(temp))
                    if(board[i-1][j] == 3):
                        if(j<3):
                            if(board[i-1][j+1] == 3):
                                if(board[i][j+1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j+1, i-1, j+1)
                                    swap(temp, i, j, i-1, j)
                                    children.append(board_to_int(temp))
                        if(j>0):
                            if(board[i-1][j-1] == 3):
                                if(board[i][j-1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j-1, i-1, j-1)
                                    swap(temp, i, j, i-1, j)
                                    children.append(board_to_int(temp))
                    if(board[i-1][j] == 4):
                        if(j<3):
                            if(board[i-1][j+1] == 4):
                                if(board[i][j+1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j+1, i-2, j+1)
                                    swap(temp, i, j, i-2, j)
                                    children.append(board_to_int(temp))
                        if(j>0):
                            if(board[i-1][j-1] == 4):
                                if(board[i][j-1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j-1, i-2, j-1)
                                    swap(temp, i, j, i-2, j)
                                    children.append(board_to_int(temp))
                if(i < 4):
                    if(board[i+1][j] == 1):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i+1, j)
                        children.append(board_to_int(temp))
                    if(board[i+1][j] == 2):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i+2, j)
                        children.append(board_to_int(temp))
                    if(board[i+1][j] == 3):
                        if(j<3):
                            if(board[i+1][j+1] == 3):
                                if(board[i][j+1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j+1, i+1, j+1)
                                    swap(temp, i, j, i+1, j)
                                    children.append(board_to_int(temp))
                        if(j>0):
                            if(board[i+1][j-1] == 3):
                                if(board[i][j-1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j-1, i+1, j-1)
                                    swap(temp, i, j, i+1, j)
                                    children.append(board_to_int(temp))
                    if(board[i+1][j] == 4):
                        if(j<3):
                            if(board[i+1][j+1] == 4):
                                if(board[i][j+1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j+1, i+2, j+1)
                                    swap(temp, i, j, i+2, j)
                                    children.append(board_to_int(temp))
                        if(j>0):
                            if(board[i+1][j-1] == 4):
                                if(board[i][j-1] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j-1, i+2, j-1)
                                    swap(temp, i, j, i+2, j)
                                    children.append(board_to_int(temp))
                if(j > 0):
                    if(board[i][j-1] == 1):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i, j-1)
                        children.append(board_to_int(temp))
                    if(board[i][j-1] == 3):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i, j-2)
                        children.append(board_to_int(temp))
                    if(board[i][j-1] == 2):
                        if(i<4):
                            if(board[i+1][j-1] == 2):
                                if(board[i+1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j-1)
                                    swap(temp, i+1, j, i+1, j-1)
                                    children.append(board_to_int(temp))
                        if(i>0):
                            if(board[i-1][j-1] == 2):
                                if(board[i-1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j-1)
                                    swap(temp, i-1, j, i-1, j-1)
                                    children.append(board_to_int(temp))
                    if(board[i][j-1] == 4):
                        if(i<4):
                            if(board[i+1][j-1] == 4):
                                if(board[i+1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j-2)
                                    swap(temp, i+1, j, i+1, j-2)
                                    children.append(board_to_int(temp))
                        if(i>0):
                            if(board[i-1][j-1] == 4):
                                if(board[i-1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j-2)
                                    swap(temp, i-1, j, i-1, j-2)
                                    children.append(board_to_int(temp))
                if(j < 3):
                    if(board[i][j+1] == 1):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i, j+1)
                        children.append(board_to_int(temp))
                    if(board[i][j+1] == 3):
                        temp = copy.deepcopy(board)
                        swap(temp, i, j, i, j+2)
                        children.append(board_to_int(temp))
                    if(board[i][j+1] == 2):
                        if(i<4):
                            if(board[i+1][j+1] == 2):
                                if(board[i+1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j+1)
                                    swap(temp, i+1, j, i+1, j+1)
                                    children.append(board_to_int(temp))
                        if(i>0):
                            if(board[i-1][j+1] == 2):
                                if(board[i-1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j+1)
                                    swap(temp, i-1, j, i-1, j+1)
                                    children.append(board_to_int(temp))
                    if(board[i][j+1] == 4):
                        if(i<4):
                            if(board[i+1][j+1] == 4):
                                if(board[i+1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j+2)
                                    swap(temp, i+1, j, i+1, j+2)
                                    children.append(board_to_int(temp))
                        if(i>0):
                            if(board[i-1][j+1] == 4):
                                if(board[i-1][j] == 0):
                                    temp = copy.deepcopy(board)
                                    swap(temp, i, j, i, j+2)
                                    swap(temp, i-1, j, i-1, j+2)
                                    children.append(board_to_int(temp))
    return children

# Returns true if the board is in a solved state, false otherwise
def solved(board):
    if(board[4][1] == 4 and board[4][2] == 4):
        return True
    return False

# Returns true if the board is in a valid position, false otherwise
# Ex: An invalid position is one where two parts of a single piece are not adjacent
def valid(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if(board[i][j] == 2):
                if(i > 0 and i < 4):
                    if(board[i-1][j] != 2 and board[i+1][j] != 2):
                        return False
            if(board[i][j] == 3):
                if(j > 0 and j < 3):
                    if(board[i][j-1] != 3 and board[i][j+1] != 3):
                        return False
                if(j == 0):
                    if(board[i][j+1] != 3):
                        return False
                if(j == 3):
                    if(board[i][j-1] != 3):
                        return False
    return True

# Given a 20 digit integer representing a board, the function
# returns the 20 digit integer representing the reflected board
def invert(value):
    board = int_to_board(value)
    swap(board, 0, 0, 0, 3)
    swap(board, 0, 1, 0, 2)
    swap(board, 1, 0, 1, 3)
    swap(board, 1, 1, 1, 2)
    swap(board, 2, 0, 2, 3)
    swap(board, 2, 1, 2, 2)
    swap(board, 3, 0, 3, 3)
    swap(board, 3, 1, 3, 2)
    swap(board, 4, 0, 4, 3)
    swap(board, 4, 1, 4, 2)
    return(board_to_int(board))

# Given an image and coordinates (x,y) the function returns an integer representing the
# type of piece present at that position
def detect_piece(image, x, y):
    if(image.getpixel((x,y)) > 160 and image.getpixel((x,y)) < 175):
        return 0
    if(image.getpixel((x+image.width//30,y)) > 130 and image.getpixel((x+image.width//30,y)) < 150):
        return 0
    border_left = False
    border_right = False
    border_up = False
    border_down = False
    for i in range(x-image.width//4, x+image.width//4):
        if(i < 0):
            border_left = True
            continue
        if(i >= image.width):
            border_right = True
            continue
        if(image.getpixel((i, y)) == 0):
            if(i < x):
                border_left = True
            else:
                border_right = True
    for i in range(y-image.height//5, y+image.height//5):
        if(i < 0):
            border_up = True
            continue
        if(i >= image.height):
            border_down = True
            continue
        if(image.getpixel((x, i)) == 0):
            if(i < y):
                border_up = True
            else:
                border_down = True
        
    if(border_left and border_right):
        if(border_up and border_down):
            return 1
        else:
            return 2
    if(border_left != border_right):
        if(border_up and border_down):
            return 3
        else:
            return 4
        
# Given an image of a valid klotski puzzle (cropped to fit the board), 
# the function returns a 5 x 4 matrix represenation of the board
def image_to_board(image_name):
    board = [[0]*4 for i in range(5)]
    image = Image.open(image_name)
    image = image.convert("L")
    height = image.height
    width = image.width
    stepX = width // 4
    stepY = height // 5
    startX = stepX // 2
    startY = stepY // 2
    for i in range(5):
        for j in range(4):
            board[i][j] = detect_piece(image, startX + stepX * j, startY + stepY * i)
    return board

# Returns the solved state of an inputted kloski puzzle
# Uses an optimized BFS to find the fastest solution (minimum moves),
# and prints out the board at each step of the solution
def solve(board):
    visited = set({})
    queue = []
    paths = {}
    current = board_to_int(board)
    visited.add(current)
    while(not solved(int_to_board(current))):
        moves = generate_children(int_to_board(current))
        for move in moves:
            if(valid(int_to_board(move)) and move not in visited and invert(move) not in visited):
                queue.append(move)
                visited.add(move)
                paths[move] = current
        current = queue.pop(0)
    while(current != board_to_int(board)):
        for line in int_to_board(current):
            print(line)
        print('-------------')
        current = paths[current]
    return int_to_board(current)

# data = [[2,4,4,2],
#         [2,4,4,2],
#         [1,2,0,1],
#         [1,2,0,1],
#         [3,3,3,3]]
data = image_to_board("Downloads/Klotski_Test_3.jpeg")
solve(data)
