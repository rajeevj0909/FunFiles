#This version of my code has complete maze generation - working sprite and wall collision - making a menu
import pygame
from tkinter import *
import random



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
ranCol = (0, 170, 160)

"""class Menu(tkinter.Tk):
    def __init__(self):
        self.label = tkinter.Label(self, test="Hello")
        self.label.pack()
        self.mainloop()"""

class Window():
    screen = pygame.display.set_mode((900, 900))

    def __init__(self):
        super().__init__()
        pygame.init()
        self.maze = Maze(800, 800, 40)
        self.update()

    def update(self):
        self.maze.coordsGen()
        self.maze.ranDelete()
        self.maze.walls()



class Maze():
    def __init__(self, g_width, g_height, cell_size):
        self.cellSize = cell_size
        self.gridWidth = g_width
        self.gridHeight = g_height
        self.coords = []


    def coordsGen(self):
        for row in range(int(self.gridWidth / self.cellSize)):
            for col in range(int(self.gridHeight / self.cellSize)):
                self.coords.append([row * self.cellSize, col * self.cellSize,
                                    row * self.cellSize, col * self.cellSize + self.cellSize,
                                    row * self.cellSize, col * self.cellSize + self.cellSize,
                                    row * self.cellSize + self.cellSize, col * self.cellSize + self.cellSize,
                                    row * self.cellSize + self.cellSize, col * self.cellSize + self.cellSize,
                                    row * self.cellSize + self.cellSize, col * self.cellSize,
                                    row * self.cellSize + self.cellSize, col * self.cellSize,
                                    row * self.cellSize, col * self.cellSize])


    def walls(self):
        for x in range(len(self.coords)):
            pos = 0
            for y in range(int(len(self.coords[x]) / 2)):
                try:
                    pygame.draw.line(Window.screen, ranCol, (self.coords[x][pos], self.coords[x][pos + 1]), (self.coords[x][pos + 2], self.coords[x][pos + 3]), 2)
                    pos = pos + 4
                except (IndexError, TypeError):
                    if TypeError:
                        pos = pos + 4
                        continue
                    else:
                        break

    def ranDelete(self):
        counts = 0
        # The below lists contain my values that have been visited, while the current value contains the current cell
        visited = []
        stack = []
        position = 0
        while len(visited) != len(self.coords):
            # neighbors is a list which contains all the values next to the current cell
            process = True
            position = position
            neighbors = [position + 1, position - 1, position + int(self.gridHeight / self.cellSize),position - int(self.gridHeight / self.cellSize)]
            temp = [position + 1, position - 1, position + int(self.gridHeight / self.cellSize),position - int(self.gridHeight / self.cellSize)]
            removeLine = [[4, 5, 6, 7, 12, 13, 14, 15], [12, 13, 14, 15, 4, 5, 6, 7], [8, 9, 10, 11, 0, 1, 2, 3],[0, 1, 2, 3, 8, 9, 10, 11]]
            try:  # This list contains the points at which the coordinates in self.coords need to be removed
                while process == True:
                    nextPos = random.choice(temp)  # next position is a random selection out of a temporary clone of neighbors
                    # The next IF and ELIF are set so if the cell is on the above or below boundary, then they do not jump up to the next cell
                    if position % int(self.gridHeight / self.cellSize) == 0:
                        if (position - 1) in temp:
                            temp.remove(position - 1)
                            nextPos = random.choice(temp)
                    elif nextPos % int(self.gridHeight / self.cellSize) == 0:
                        if (position + 1) in temp:
                            temp.remove(nextPos)
                            nextPos = random.choice(temp)
                    # if the next position is valid:
                    if nextPos not in visited and nextPos in range(len(self.coords)):
                        for x in range(4):
                            # removethe values out of self.coords specified in removeLines and sets them equal to 'None'
                            self.coords[position][removeLine[neighbors.index(nextPos)][x]] = None
                            self.coords[nextPos][removeLine[neighbors.index(nextPos)][x + 4]] = None
                        # add the position to stack and choose a next position
                        stack.append(position)
                        position = nextPos
                        process = False
                    else:
                        temp.remove(nextPos)
                        nextPos = random.choice(temp)
                visited.append(position) #add the position to the visited list
            # If temp is empty, then draw the walls as is
            except IndexError:
                process = False
                counts = counts + 1
                position, stack = self.backTrack(position, stack, 0, visited)

    def backTrack(self, btPosition, btStack, count, btVisited):
        btPosition = btStack.pop()
        n = [btPosition + 1, btPosition - 1, btPosition + int(self.gridHeight / self.cellSize),btPosition - int(self.gridHeight/ self.cellSize)]  # all the neighbors
        temp = [btPosition + 1, btPosition - 1, btPosition + int(self.gridHeight / self.cellSize),btPosition - int(self.gridHeight / self.cellSize)]
        for x in n:
            if x in btVisited or x not in range(len(self.coords)):  # if x is in the visited list or isnt even in the grid at all then remove it
                temp.remove(x)
        if temp != []:  # if some of the x values make it through, temp wont be empty, meaning there are neighbors for the returned position to go to
            return (btPosition, btStack)
        else:  # if temp is empty
            return self.backTrack(btPosition, btStack, count + 1, btVisited)  # recurse with the new values


W=900
H=900

class playerSprite(pygame.sprite.Sprite):
    def __init__(self, sWidth, sHeight):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.sWidth = sWidth
        self.sHeight = sHeight
        self.image = pygame.Surface((self.sWidth, self.sHeight))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.center = (20, 20)


    def update(self):
        self.movement()


    def movement(self):
        key = pygame.key.get_pressed()
        dist = 2
        if key[pygame.K_DOWN]:
            if savedScreen.get_at((self.rect.x,self.rect.y + self.sHeight + dist)) == (0,0,0):
                if savedScreen.get_at((self.rect.x + self.sWidth, self.rect.y + self.sHeight + dist)) == (0,0,0):
                    self.rect.y += dist
        elif key[pygame.K_UP]:
            if savedScreen.get_at((self.rect.x, self.rect.y - dist)) == (0,0,0):
                if savedScreen.get_at((self.rect.x + self.sWidth, self.rect.y - dist)) == (0,0,0):
                    self.rect.y -= dist
        if key[pygame.K_RIGHT]:
            if savedScreen.get_at((self.rect.x + dist + self.sWidth, self.rect.y)) == (0,0,0):
                if savedScreen.get_at((self.rect.x + dist + self.sWidth, self.rect.y + self.sHeight)) == (0,0,0):
                    self.rect.x += dist
        elif key[pygame.K_LEFT]:
            if savedScreen.get_at((self.rect.x - dist, self.rect.y)) == (0,0,0):
                if savedScreen.get_at((self.rect.x - dist, self.rect.y + self.sHeight)) == (0,0,0):
                    self.rect.x -= dist

class finishSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.Pos()

    def Pos(self):
        self.rect.center = (window.maze.gridWidth - int(window.maze.cellSize/2), window.maze.gridHeight - int(window.maze.cellSize/2))





window = Window()
savedScreen = pygame.Surface.copy(Window.screen)
#savedScreen = window.screen

clock = pygame.time.Clock()
player = playerSprite(20,20)
finish = finishSprite()

sprites = pygame.sprite.Group()
sprites.add(finish)
sprites.add(player)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    sprites.update()
    window.screen.blit(savedScreen, (0, 0))
    sprites.draw(window.screen)
    #savedScreen.blit(window.screen, (0,0))
    #print(player.rect.x)
    pygame.display.update()
    player.rect.colliderect(finish.rect)
    if player.rect.colliderect(finish.rect) == True:
        print("Done")
        break