from random import randint
import os
import time

class GameOfLife:
    def __init__(self, width = 10, height = 10, speed = 1):

        self.height = height
        self.width = width  
        self.cells = self.GenerateCells(True)
        self.speed = 1./speed
        self.gameOver = False
        self.stepCounter = 0

    def GenerateCells(self, randomize=False):
        if randomize == True:
            return [[randint(0,1) for i in range(self.width)] for j in range(self.height)]
    
    def DrawField(self):
        new_cells = []
        
        print('_', end = '')
        for i in self.cells:
            print('__', end = '')
        print('_')

        for i in self.cells:
            print('|', end = '')
            for j in i:
                if(j == 1):
                    print('o ', end = '')
                else:
                    print('  ', end = '')
            print('|')
        
        print('|', end = '')
        for i in self.cells:
            print('__', end = '')
        print('|')

    def GetNeighbour(self, i, j, maxX, maxY):
        if(i < 0 or i > maxX or j < 0 or j > maxY):
            return 0
        return self.cells[i][j]

    def Step(self):
        new_cell_list = [[0 for i in range(self.width)] for j in range(self.height)]
        
        self.stepCounter += 1
        for i in range(self.width):
            for j in range(self.height):
                cell = self.cells[i][j]
                nw = self.GetNeighbour(i - 1, j - 1, len(self.cells) - 1, len(self.cells[0]) - 1);
                n  = self.GetNeighbour(i - 1, j    , len(self.cells) - 1, len(self.cells[0]) - 1);
                ne = self.GetNeighbour(i - 1, j + 1, len(self.cells) - 1, len(self.cells[0]) - 1);
                w  = self.GetNeighbour(i    , j - 1, len(self.cells) - 1, len(self.cells[0]) - 1);
                e  = self.GetNeighbour(i    , j + 1, len(self.cells) - 1, len(self.cells[0]) - 1);
                sw = self.GetNeighbour(i + 1, j - 1, len(self.cells) - 1, len(self.cells[0]) - 1);
                s  = self.GetNeighbour(i + 1, j    , len(self.cells) - 1, len(self.cells[0]) - 1);
                se = self.GetNeighbour(i + 1, j + 1, len(self.cells) - 1, len(self.cells[0]) - 1);

                living = nw + n + ne + w + e + sw + s + se

                if(living == 0 and cell == 3):
                    new_cell_list[i][j] = 1
                elif(cell == 1 and living < 2):
                    new_cell_list[i][j] = 0
                elif( cell == 1 and (living == 2 or living == 3) ):
                    new_cell_list[i][j] = 1
                elif(cell == 1 and living > 3):
                    new_cell_list[i][j] = 0
        
        if(self.cells != new_cell_list):
            self.cells = new_cell_list
        else: 
            self.gameOver = True

    def Run(self):
        while not self.gameOver:
            self.DrawField()
            self.Step()
            time.sleep(self.speed)
            os.system("cls")
        print("Game is over in", self.stepCounter, "steps")


if __name__ == "__main__":
    game = GameOfLife(50, 50, 1)
    game.Run()