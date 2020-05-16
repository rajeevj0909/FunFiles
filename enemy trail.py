import pyglet
from pyglet.window import *
import random
from random import randint
from pyglet.window import key

    

class Gameplay_class():
    def __init__(self):
       # self.set_size(805, 3000)
      # self.image = pyglet.image.load('trongridmap.jpg')
      #  self.background_sprite = pyglet.sprite.Sprite(self.image)
        self.trail_batch=pyglet.graphics.Batch()
        self.enemy_trail_batch=pyglet.graphics.Batch()
        self.carimage=pyglet.image.load('car.png')
        self.carimage.anchor_x =self.carimage.width//2
        self.carimage.anchor_y = self.carimage.height//2
        self.car=pyglet.sprite.Sprite(self.carimage, 100, 100)
        self.direction=0
        #player trail 
        trail_image = pyglet.image.load('trail.fw.png')
        trail_sprite = pyglet.sprite.Sprite(trail_image, self.car.x,self.car.y)
        self.trail_list = []
        self.count = 0
        
        #loading enemy 
        self.yvelocity=5
        self.xvelocity=random.randint(-10,10)
        self.tronimage=pyglet.image.load('tron2.fw.png')
        self.tronimage.anchor_x =self.tronimage.width//2
        self.tronimage.anchor_y = self.tronimage.height//2
        self.tron=pyglet.sprite.Sprite(self.tronimage, 500, 500)
        #enemy trail
        self.enemy_trail_image = pyglet.image.load('trail2.fw.png')
        self.enemy_trail_sprite = pyglet.sprite.Sprite(self.enemy_trail_image, self.tron.x,self.tron.y)
        self.enemy_trail_list=[]
        self.count=0
    def add_trail(self, dt, dt1):
        #player trail

        trail_image = pyglet.image.load('trail.fw.png')
        trail_sprite = pyglet.sprite.Sprite(trail_image, self.car.x,self.car.y)
        self.trail_list.append(self.trail_sprite)
        #enemy trail
        self.enemy_trail_image = pyglet.image.load('trail2.fw.png')
        self.enemy_trail_sprite = pyglet.sprite.Sprite(self.enemy_trail_image, self.tron.x,self.tron.y)
        self.enemy_trail_list.append(self.enemy_trail_sprite)
    def AIMove(self,dt, AImove, count):
        count.append(1)
        movementAI=['Up','Down','Right','Left']
        #AImove.append( random.choice(movementAI))
        #numchoice=[1,2,3,4,5,6,7,8,9,10]
        #straightchoice=random.choice(numchoice)
        if len(AImove)==0:
            print("len Called")
            choice = random.choice(movementAI)
            for i in range(10,20):
                AImove.append( choice)

        direction = AImove.pop()
        print("Current Stack:", AImove)
        if direction =='Up':
                self.tron.y =(self.tron.y+10)
                enemy_trail_image = pyglet.image.load('trail2.fw.png')
                enemy_trail = pyglet.sprite.Sprite(enemy_trail_image, x = self.tron.x,y = self.tron.y, batch =self.enemy_trail_batch)
                self.enemy_trail_list.append(enemy_trail)
               
        if direction=='Down':
                self.tron.y =(self.tron.y-10)
                enemy_trail_image = pyglet.image.load('trail2.fw.png')
                enemy_trail = pyglet.sprite.Sprite(enemy_trail_image, x = self.tron.x,y = self.tron.y, batch =self.enemy_trail_batch)
                self.enemy_trail_list.append(enemy_trail)
               
        if direction=='Right':
                self.tron.x =(self.tron.x+10)
                enemy_trail_image = pyglet.image.load('trail2.fw.png')
                enemy_trail = pyglet.sprite.Sprite(enemy_trail_image, x = self.tron.x,y = self.tron.y, batch =self.enemy_trail_batch)
                self.enemy_trail_list.append(enemy_trail)
               
        if direction=='Left':
                self.tron.x =(self.tron.x-10)
                enemy_trail_image = pyglet.image.load('trail2.fw.png')
                enemy_trail = pyglet.sprite.Sprite(enemy_trail_image, x = self.tron.x,y = self.tron.y, batch =self.enemy_trail_batch)
                self.enemy_trail_list.append(enemy_trail)



        dt = pyglet.clock.tick()
        print(dt)

    def collision(self, dt):
            for enemy_trail in self.enemy_trail_list:
                    if self.car.x == enemy_trail.x and self.car.y == enemy_trail.y:
                        print ('crash 1')
                        print (self.car.x,self.car.y)
            for trail in self.trail_list:
                if self.tron.x == trail.x and self.tron.y == trail.y:
                        print ('crash 2')

   
        
        
    def score(self):
        wins=0
        if self.car.x == enemy_trail.x and self.car.y == enemy_trail.y:
            wins=wins+1
        if self.tron.x == trail.x and self.tron.y == trail.y:
            wins=wins+1
        if wins==3:
            print ('Game over')
        
    def createWindow(self):
        window = pyglet.window.Window(width=1000,height=800,fullscreen=False )
        
        
                            
        @window.event
            
        
        def on_draw():
            window.clear()
           # self.background_sprite.draw()
            self.tron.draw()
            self.trail_batch.draw()
            self.car.draw()
            print('car',self.car.x, self.car.y)
            print ('tron',self.tron.x, self.tron.y)

            self.enemy_trail_batch.draw()
            #self.AIMove(1/60,[],[])
            
            
        #player  movement  
        @window.event
        def on_text_motion(motion):

            if motion== pyglet.window.key.MOTION_UP:
                self.car.update(y=self.car.y+3,rotation=270)
                trail_image = pyglet.image.load('trail.fw.png')
                trail_sprite = pyglet.sprite.Sprite(trail_image, x = self.car.x,y = self.car.y, batch =self.trail_batch)
                self.trail_list.append(trail_sprite)
            if motion==pyglet.window.key.MOTION_DOWN:
                self.car.update(y=self.car.y-3,rotation=90)
                trail_image = pyglet.image.load('trail.fw.png')
                trail_sprite = pyglet.sprite.Sprite(trail_image, x = self.car.x,y = self.car.y, batch =self.trail_batch)
                self.trail_list.append(trail_sprite)
            
            if motion==pyglet.window.key.MOTION_LEFT:
                self.car.update(x=self.car.x-3,rotation=180)
                trail_image = pyglet.image.load('trail.fw.png')
                trail_sprite = pyglet.sprite.Sprite(trail_image, x = self.car.x,y = self.car.y, batch =self.trail_batch)
                self.trail_list.append(trail_sprite)
                
            if motion==pyglet.window.key.MOTION_RIGHT:
                self.car.update(x=self.car.x+3,rotation=0)
                trail_image = pyglet.image.load('trail.fw.png')
                trail_sprite = pyglet.sprite.Sprite(trail_image, x = self.car.x,y = self.car.y, batch =self.trail_batch)
                self.trail_list.append(trail_sprite)
              
     
                   
                
#if __name__ == '__main__': #name is saying the file name and the main is if the file is being run then it runs it 

gp = Gameplay_class()
AImove = []
count = []
pyglet.clock.schedule_interval(gp.collision,1/60)
#pyglet.clock.unschedule_interval(gp.AIMove, 1/60, AImove, count)
pyglet.clock.schedule_interval(gp.AIMove, 1/40, AImove, count)
gp.createWindow()
pyglet.app.run()
