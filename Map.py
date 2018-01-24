# By cpt_9m0
# board array

WIDTH = 500 // 10
HEIGHT = 600 // 10

BOARD = [[]]


def create_map_board(width, height):
    for j in range(height):
        BOARD.append([])

    for j in range(height):
        for i in range(width):
            BOARD[j].append([])
    for y in range(height):
        for x in range(width):
            BOARD[y][x] = 1
    # enemy main tower
    for y in range(0, 0 + 11):
        for x in range(20, 20 + 9):
            BOARD[y][x] = 'T2'
    # self main tower
    for y in range(42, 42 + 11):
        for x in range(20, 20 + 9):
            BOARD[y][x] = 'T5'
    # enemy right tower
    for y in range(7, 7 + 9):
        for x in range(34, 34 + 7):
            BOARD[y][x] = 'T3'
    # self right tower
    for y in range(38, 38 + 9):
        for x in range(34, 34 + 7):
            BOARD[y][x] = 'T4'
    # enemy left tower
    for y in range(7, 7 + 9):
        for x in range(7, 7 + 7):
            BOARD[y][x] = 'T1'
    # self left tower
    for y in range(38, 38 + 9):
        for x in range(7, 7 + 7):
            BOARD[y][x] = 'T6'
    # river
    for y in range(29, 33):
        for x in range(0, 10):
            BOARD[y][x] = 0
        for x in range(13, 37):
            BOARD[y][x] = 0
        for x in range(40, 50):
            BOARD[y][x] = 0

    # print_board()


def remove_enemy_left_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T1':
                BOARD[y][x] = 1


def remove_enemy_main_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T2':
                BOARD[y][x] = 1


def remove_enemy_right_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T3':
                BOARD[y][x] = 1


def remove_self_right_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T4':
                BOARD[y][x] = 1


def remove_self_main_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T5':
                BOARD[y][x] = 1


def remove_self_left_tower():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if BOARD[y][x] == 'T6':
                BOARD[y][x] = 1



def print_board():
    for y in range(HEIGHT):
        print(BOARD[y])
        if len((BOARD[y])) != 50:
            print("Erorr")

# print_board()
