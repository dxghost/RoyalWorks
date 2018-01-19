# Design game board
# A testing version
# By : cpt_9m0

class gameBoard:

    def __init__(self):
        self.height = 640
        self.width = 420
        self.mosaic = 'mosaic'
        self.mosaic_size = 20
        self.river = 'river'
        self.river_size = 20
        self.tree = 'tree'
        self.tree_size = 20
        self.tower = 'tower'
        self.tower_size = 40
        self.bridge = 'bridge'
        self.bridge_size = 30
        self.card = 'card'
        self.card_size = 60
    def makeBoard(self):
        board_height = self.height // self.mosaic_size
        board_width = self.width // self.mosaic_size
        board = []
        for y in range(board_height):
            board.append([])
            pass
        for y in range(board_height):
            for x in range(board_width):
                board[y].append(self.mosaic)
                pass
            pass
        for x in range(board_width):
            board[(board_height // 2) - 1][x] = self.river
            pass
        for x in range(board_width):
            board[0][x] = self.tree
            board[board_height - 1][x] = self.tree
            pass
        for y in range(board_height):
            board[y][0] = self.tree
            board[y][board_width - 1] = self.tree
            pass

        board[(board_height // 2) - 2][board_width // 4] = self.bridge
        board[(board_height // 2) - 1][board_width // 4] = self.bridge
        board[(board_height // 2)][board_width // 4] = self.bridge
        board[(board_height // 2) - 2][board_width - (board_width // 4)] = self.bridge
        board[(board_height // 2) - 1][board_width - (board_width // 4)] = self.bridge
        board[(board_height // 2)][board_width - (board_width // 4)] = self.bridge

        board[board_height // 6 -2][board_width // 3 - 2] = self.tower
        board[board_height // 6 -1][board_width // 3 - 2] = self.tower
        board[board_height // 6 -2][board_width // 3 - 1] = self.tower
        board[board_height // 6 -1][board_width // 3 - 1] = self.tower

        board[board_height // 6 -2][board_width // 3 - 2 + int(0.25 * self.mosaic_size)] = self.tower
        board[board_height // 6 -1][board_width // 3 - 2 + int(0.25 * self.mosaic_size)] = self.tower
        board[board_height // 6 -2][board_width // 3 - 1 + int(0.25 * self.mosaic_size)] = self.tower
        board[board_height // 6 -1][board_width // 3 - 1 + int(0.25 * self.mosaic_size)] = self.tower

        board[board_height // 6 -2][board_width // 3 - 2 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[board_height // 6 -1][board_width // 3 - 2 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[board_height // 6 -2][board_width // 3 - 1 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[board_height // 6 -1][board_width // 3 - 1 + int(0.25 * self.mosaic_size) * 2] = self.tower

        board[(board_height * 5) // 6 -2][board_width // 3 - 2] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 2] = self.tower
        board[(board_height * 5) // 6 -2][board_width // 3 - 1] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 1] = self.tower

        board[(board_height * 5) // 6 -2][board_width // 3 - 2 + int(0.25 * self.mosaic_size)] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 2 + int(0.25 * self.mosaic_size)] = self.tower
        board[(board_height * 5) // 6 -2][board_width // 3 - 1 + int(0.25 * self.mosaic_size)] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 1 + int(0.25 * self.mosaic_size)] = self.tower

        board[(board_height * 5) // 6 -2][board_width // 3 - 2 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 2 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[(board_height * 5) // 6 -2][board_width // 3 - 1 + int(0.25 * self.mosaic_size) * 2] = self.tower
        board[(board_height * 5) // 6 -1][board_width // 3 - 1 + int(0.25 * self.mosaic_size) * 2] = self.tower
        return board

import time
gameboard = gameBoard()
boardArray = gameboard.makeBoard()
print("Test...")
import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAY =pygame.display.set_mode((gameboard.width, gameboard.height))
pygame.display.set_caption = "Clash Royal"
DONE = False
DISPLAY.fill((0, 50, 10))

while not DONE:
    for y in range(gameboard.height // gameboard.mosaic_size):
        for x in range(gameboard.width // gameboard.mosaic_size):
            if boardArray[y][x] == gameboard.tree:
                pygame.draw.rect(DISPLAY, (0, 255, 0), (x * gameboard.mosaic_size, y * gameboard.mosaic_size, gameboard.tree_size, gameboard.tree_size))
            elif boardArray[y][x] == gameboard.river:
                pygame.draw.rect(DISPLAY, (0, 0, 255), (x * gameboard.mosaic_size, y * gameboard.mosaic_size, gameboard.river_size, gameboard.river_size))
            elif boardArray[y][x] == gameboard.tower:
                pygame.draw.rect(DISPLAY, (0, 0, 0), (x * gameboard.mosaic_size, y * gameboard.mosaic_size, gameboard.tower_size, gameboard.tower_size))
            elif boardArray[y][x] == gameboard.bridge:
                pygame.draw.rect(DISPLAY, (102, 22, 2), (x * gameboard.mosaic_size, y * gameboard.mosaic_size, gameboard.bridge_size, gameboard.bridge_size))
            else:
                pygame.draw.rect(DISPLAY, (0, 50, 10), (x * gameboard.mosaic_size, y * gameboard.mosaic_size, gameboard.mosaic_size, gameboard.mosaic_size))
    for even in pygame.event.get():
        if even.type == QUIT:
            DONE = True
            pygame.quit()
    pygame.display.update()

