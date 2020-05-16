import pyglet
from pyglet.gl import *
from pyglet.window import key
import tkinter
import math
import random
win = pyglet.window.Window(width = 1200, height = 720)
class Player:
    def __init__(self):
        self.image = pyglet.image.load('Images/normalPlayer.png')
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.allBullets = pyglet.graphics.Batch()
        self.bullets = []
        self.velocity_x = 100.0
        self.velocity_y = 100.0
        self.rotate_speed = 200
        self.oldAngle = 0
        self.playerSprite = pyglet.sprite.Sprite(self.image,x=(1200/2)-(self.image.width/2),y=(720/2)-(self.image.height/2))
        self.bullet = pyglet.image.load('Images/bullet.png')
        self.bullet.width = 6
        self.bullet.height = 6
    def loadImage(self):
        self.playerSprite.draw()
        self.allBullets.draw()        
    def moveImage(self,dt):
        @win.event
        def on_text_motion(motion):
            if motion == pyglet.window.key.MOTION_LEFT:
                self.playerSprite.rotation -=10
            if motion == pyglet.window.key.MOTION_RIGHT:
                self.playerSprite.rotation += 10
            if motion == pyglet.window.key.MOTION_UP:
                rad = math.radians(self.playerSprite.rotation)
                cosAngle = math.cos(rad)
                sinAngle = math.sin(rad)
                self.playerSprite.y += cosAngle *dt * self.velocity_y
                self.playerSprite.x += sinAngle *dt * self.velocity_x
                self.velocity_x +=100
                self.velocity_y +=100
                if self.velocity_y > 200:
                    self.velocity_x =250
                    self.velocity_y =250
        @win.event
        def on_key_press(key, modifiers):
            if key == pyglet.window.key.SPACE:
                counter = 0
                self.bullets.append(pyglet.sprite.Sprite(self.bullet,x = self.playerSprite.x, y = self.playerSprite.y, batch = self.allBullets))
                for bullet in self.bullets:
                    self.bullets[counter].x = self.playerSprite.x
                    self.bullets[counter].y = self.playerSprite.y
                    self.oldAngle = self.playerSprite.rotation
                    counter = counter + 1
            
    def update(self,dt):
        rad = math.radians(self.playerSprite.rotation)
        cosAngle = math.cos(rad)
        sinAngle = math.sin(rad)
        self.playerSprite.x += sinAngle *dt * self.velocity_x
        self.playerSprite.y += cosAngle *dt * self.velocity_y
        if self.velocity_x > 0:
            self.velocity_y -= 2
            self.velocity_x -= 2
        elif self.velocity_x < 0:
            self.velocity_y = 10
            self.velocity_x = 10
        counter = 0
        for bullet in self.bullets:
            self.bullets[counter].rotation = self.oldAngle
            rad = math.radians(self.bullets[counter].rotation)
            cosAngle = math.cos(rad)
            sinAngle = math.sin(rad)
            self.bullets[counter].y += cosAngle * dt * 500
            self.bullets[counter].x += sinAngle * dt * 500
            enemy.bigCollision()
            enemy.mediumCollision()
            counter = counter + 1
    def getPositions(self):
        counter = 0
        for bullet in self.bullets:
            bulletArray = [self.bullets[counter].x, self.bullets[counter].y, self.bullets[counter]]
            counter = counter + 1
            return(bulletArray)
    def checkBounds(self,dt):
        winMinX = 0
        winMinY = 0
        winMaxX = 1200 
        winMaxY = 720
        if self.playerSprite.x < winMinX:
            self.playerSprite.x = winMaxX
        elif self.playerSprite.x > winMaxX:
            self.playerSprite.x = winMinX
        if self.playerSprite.y < winMinY:
            self.playerSprite.y = winMaxY
        if self.playerSprite.y > winMaxY:
            self.playerSprite.y = winMinY



class Enemies:
    def __init__(self):
        self.mediumImage = pyglet.image.load('Images/mediumAsteroid.png')
        self.smallImage = pyglet.image.load('Images/smallAsteroid.png')
        self.asteroids = pyglet.graphics.Batch()
        self.asteroidList = []
        self.asteroidList.append(pyglet.sprite.Sprite(pyglet.image.load('Images/largeAsteroid.png'), x = 0, y = 0, batch = self.asteroids,))
        self.mediumSize = 50
        self.angle = random.randint(0,360)
    def loadEnemy(self):
        self.asteroids.draw()
    def smallMove(self,dt):
        counter = 0
        for asteroid in self.asteroidList:
            self.asteroidList[counter].rotation = self.angle
            rad = math.radians(self.asteroidList[counter].rotation)
            cosAngle = math.cos(rad)
            sinAngle = math.sin(rad) 
            self.asteroidList[counter].y += cosAngle *dt * 100
            self.asteroidList[counter].x += sinAngle *dt * 100
            counter = counter + 1
    def checkBounds(self,dt):
        counter = 0
        for asteroids in self.asteroidList:
            winMinX = 0
            winMinY = 0
            winMaxX = 1200
            winMaxY = 720
            if self.asteroidList[counter].x < winMinX:
                self.asteroidList[counter].x = winMaxX
            elif self.asteroidList[counter].x > winMaxX:
                self.asteroidList[counter].x = winMinX
            if self.asteroidList[counter].y < winMinY:
                self.asteroidList[counter].y = winMaxY
            if self.asteroidList[counter].y > winMaxY:
                self.asteroidList[counter].y = winMinY
            counter = counter + 1
    def bigCollision(self):
        counter = 0
        for asteroid in self.asteroidList:
            bulletpositions = player.getPositions()
            collisionDistance = self.asteroidList[counter].width/2 + bulletpositions[2].width/2
            actualDistance = math.sqrt((self.asteroidList[counter].position[0] - bulletpositions[0]) ** 2 +
                                       (self.asteroidList[counter].position[1] - bulletpositions[1]) ** 2)
        if actualDistance <=collisionDistance and self.asteroidList[counter].width == 70:
            print("HIT")
            self.postx = self.asteroidList[counter].position[0]
            self.posty = self.asteroidList[counter].position[1]
            self.asteroidList.remove(self.asteroidList[counter])
            bulletpositions[2].x = 5000
            bulletpositions[2].y = 5000
            self.asteroidList.append(pyglet.sprite.Sprite(self.mediumImage, x= self.postx, y = self.posty, batch = self.asteroids))
            self.angle = random.randint(0,360)
            self.asteroidList[counter].rotation = self.angle
            print("Medium")
        else:
            print("Not hit")
    def mediumCollision(self):
        counter = 0
        for asteroid in self.asteroidList:
            bulletpositions = player.getPositions()
            collisionDistance = self.asteroidList[counter].width/2 + bulletpositions[2].width/2
            actualDistance = math.sqrt((self.asteroidList[counter].position[0] - bulletpositions[0]) ** 2 +
                                       (self.asteroidList[counter].position[1] - bulletpositions[1]) ** 2)
        if actualDistance <=collisionDistance and self.asteroidList[counter].width == 50:
            self.postxx = self.asteroidList[counter].position[0]
            self.postyy = self.asteroidList[counter].position[1]
            self.asteroidList.remove(self.asteroidList[counter])
            self.asteroidList.append(pyglet.sprite.Sprite(self.smallImage, x= self.postxx, y = self.postyy, batch = self.asteroids))
            self.angle = random.randint(0,360)
            self.asteroidList[counter].rotation = self.angle
        else:
            print("Not hit")

                            
                                    
player = Player()
enemy = Enemies()

@win.event
def on_draw():
    win.clear()
    player.loadImage()
    enemy.loadEnemy()
pyglet.clock.schedule_interval(player.moveImage, 1/120)
pyglet.clock.schedule_interval(player.update, 1/120)
pyglet.clock.schedule_interval(player.checkBounds, 1/120)
pyglet.clock.schedule_interval(enemy.smallMove, 1/120)
pyglet.clock.schedule_interval(enemy.checkBounds, 1/120)

pyglet.app.run()
