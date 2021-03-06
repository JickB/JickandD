from class_Tile import Tile

class Game:
    def __init__(self,x,y):
        board = [[Tile() for j in range(x)] for i in range(y)]
        self.board=board

    def board_print(self):
        for i in range(len(self.board[0])):
            for j in range(len(self.board[i])):
                print(self.board[j][i].output,end ="")
            print()

    def update_player(self,player):
        self.board[player.x][player.y].output="P"
        self.board[player.x][player.y].has_player=True

    def old_player(self,player):
        self.board[player.x][player.y].output=self.board[player.x][player.y].original_tile
        self.board[player.x][player.y].has_player=False
