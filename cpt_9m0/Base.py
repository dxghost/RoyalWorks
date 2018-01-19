# Design game board
# A testing version
# By : cpt_9m0

class gameBoard:
    def __init__(self):
        self.height = 640
        self.width = 420
        self.mosaic_size = 10
        self.river_size = 10
        self.tree_size = 10
        self.tower_size = 40
        self.bridge_size = 30
    def makeBoard(self):
        board_height = self.height // self.mosaic_size
        board_width = self.width // self.mosaic_size
        board = []
        for y in range(board_height):
            board.append([])
        for y in range(board_height):
            for x in range(board_width):
                board[y].append([])
        return board

gBoard = gameBoard()
array = gBoard.makeBoard()
print("Test...")
print(array[0])
