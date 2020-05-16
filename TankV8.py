import pyglet
import math
from pyglet.window import key
from pyglet.window import mouse
class tank():
    def __init__(self):
        window=pyglet.window.Window(width=1280, height=720)
        self.ground = pyglet.image.load("ground.png")
        self.ground.width =window.width
        self.ground.height = 100

        self.pillar = pyglet.image.load("ground.png")
        self.pillar.width = 130
        self.pillar.height = 300
        self.pillar = pyglet.sprite.Sprite(img=self.pillar,x=600,y=100)
     
        self.redTank=pyglet.resource.image("tankLeft.png")
        self.redTank.width = 150
        self.redTank.height = 60
        self.tankLeft = pyglet.sprite.Sprite(img=self.redTank,x=50,y=100)
        self.tankLeft.anchor_x = self.redTank.width / 2
        self.tankLeft.anchor_y = self.redTank.height / 2
        
        self.greenTank=pyglet.resource.image("tankRight.png")
        self.greenTank.width = 150
        self.greenTank.height = 60
        self.tankRight=pyglet.sprite.Sprite(img=self.greenTank ,x=((window.width )-200),y=100)
        self.tankRight.anchor_x = self.greenTank.width / 2
        self.tankRight.anchor_y = self.greenTank.height / 2


        self.redTurret=pyglet.resource.image("turretLeft.png")
        self.redTurret.width = 30
        self.redTurret.height = 80
        self.turretLeft = pyglet.sprite.Sprite(img=self.redTurret,x=self.tankLeft.x+100,y=self.tankLeft.y+50)
        self.redTurret.anchor_x = self.redTurret.width / 2
        self.redTurret.anchor_y = 0
        
        self.greenTurret=pyglet.resource.image("turretRight.png")
        self.greenTurret.width = 30
        self.greenTurret.height = 80
        self.turretRight=pyglet.sprite.Sprite(img=self.greenTurret,x=self.tankRight.x+30,y=self.tankRight.y+50)
        self.greenTurret.anchor_x = self.greenTurret.width / 2
        self.greenTurret.anchor_y = 0

        self.bullet = pyglet.resource.image("Bullet.png")
        self.bullet.width = 50
        self.bullet.height = 50
        self.shot=pyglet.sprite.Sprite(img=self.bullet,x=((window.width)+2000),y=100)
        self.shot.anchor_x = self.bullet.width / 2
        self.shot.anchor_y = self.bullet.height / 2

        self.redBarleft = pyglet.resource.image("Rhealthbar.png")
        self.redBarleft.width = 1000
        self.redBarleft.height= 70
        self.RHbar=pyglet.sprite.Sprite(img=self.redBarleft,x=200, y=600)
        self.RHbar.anchor_x = self.redBarleft.width
        self.RHbar.anchor_y = self.redBarleft.height/2

        self.greenBarleft = pyglet.resource.image("Ghealthbar.png")
        self.greenBarleft.width = 1000
        self.greenBarleft.height= 70
        self.GHbar=pyglet.sprite.Sprite(img=self.greenBarleft,x=200, y=600)
        self.GHbar.anchor_x = self.greenBarleft.width
        self.GHbar.anchor_y = self.greenBarleft.height/2
        

        @window.event
        def on_text_motion(motion):
            if (motion==pyglet.window.key.MOTION_LEFT):
                if self.tankRight.x != 730:
                    self.tankRight.x -= 5
                    self.turretRight.x -= 5
                else:
                    print("boundry")
            elif (motion==pyglet.window.key.MOTION_RIGHT):
                if self.tankRight.x != 1130:
                    self.tankRight.x += 5
                    self.turretRight.x += 5
                else:
                    print("boundary")
            elif (motion==pyglet.window.key.MOTION_BACKSPACE):
                if self.tankLeft.x != 0:
                    self.tankLeft.x-=5
                    self.turretLeft.x-=5
                else:
                    print("boundary")
            elif (motion==pyglet.window.key.MOTION_DELETE):
                if self.tankLeft.x!= 450:
                    self.tankLeft.x+=5
                    self.turretLeft.x += 5
                else:
                    print("boundary")
                    
        @window.event
        def on_mouse_motion(x, y, dx, dy):
            turret_x = self.turretRight.x
            turret_y = self.turretRight.y
            mouse_x = x
            mouse_y = y
            x_length = mouse_x - turret_x
            y_length = mouse_y - turret_y
            if y>150:                
                if x_length > 0:
                    angle = math.degrees(math.atan(y_length / x_length))
                    angle = 90 - angle
                    self.turretRight.rotation = angle
                else:
                    angle = math.degrees(math.atan(y_length / x_length))
                    angle = 270 - angle
                    self.turretRight.rotation = angle
            else:
                self.turretRight.rotation = 270
                
        @window.event
        def on_key_release(symbol, modifier):
            if symbol == key.SPACE:
                self.shot.x= self.turretRight.x-25
                self.shot.y= self.turretRight.y-20
                self.yCounter = 30
                def update(dt):
                        self.shot.x = self.shot.x - 12
                        self.shot.y = self.shot.y + self.yCounter
                        self.yCounter -= 1
                        if self.shot.x<self.tankLeft.x+80 and self.shot.y<self.tankLeft.y+35:
                            if self.shot.x>self.tankLeft.x-80 and self.shot.y>self.tankLeft.y-35:
                                print("boom")

                            
                        
                            
                    
                pyglet.clock.schedule_interval(update, 1 / 60.0)                
            
        @window.event       
        def on_mouse_press(x,y,button,modifier):
            if button == mouse.LEFT:
                print(" X"+str(x), " Y"+str(y))

            

        @window.event
        def on_draw():
            window.clear()
            self.tankRight.draw()
            self.pillar.draw()
            self.ground.blit(x=0,y=0)
            self.tankLeft.draw()
            self.turretRight.draw()
            self.turretLeft.draw()
            self.shot.draw()
            self.RHbar.draw()
            self.GHbar.draw()

        pyglet.app.run()
tank()
#spriteName.img or image=imageName

#gravity
#velocity
#negative quadratic equation

