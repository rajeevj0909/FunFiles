'''
https://youtu.be/wEBQEuriu7c       FULL SCREEN OR DIMENSIONS
Full screen:    window=pyglet.window.Window(fullscreen=True, resizable=True)
Dimensions:
window_w=1280
window_h=720
window=pyglet.window.Window(width=window_w,height=window_h, resizable=True)
'''
###
'''  (https://www.youtube.com/watch?v=zEOuDVyczBM&t=21s)  Writing Text  14/6/18
label=pyglet.text.Label("Hi Rajeev", font_name="Comic Sans",font_size=28, x=window.width/2, y=window.width/2, anchor_y="center",anchor_x="center")
@window.event
def on_draw():
    window.clear()
    label.draw()
'''
###
'''  (https://www.youtube.com/watch?v=fY-MLZrzKhE)  Key presses   14/06/18
@window.event
def on_key_press(key,modifiers):
    if (key==pyglet.window.key.DOWN):
        print("DOWN!")
    elif (key==pyglet.window.key.UP):
        print("UP!")
    elif (key==pyglet.window.key.LEFT):
        print("LEFT!")
    elif (key==pyglet.window.key.RIGHT):
        print("RIGHT!")
    elif (key==pyglet.window.key.SPACE):
        print("SPACE!")
    elif (key==pyglet.window.key.ENTER):
        print("ENTER!")
    else:
        print("Doing an event!")
'''
###
'''https://www.youtube.com/watch?v=gCgokFnrZnw     Drawing an image on
@window.event
def on_draw():
    window.clear()
    sprite.draw()
'''
###
'''
(https://www.youtube.com/watch?v=rrULb4y11yE)    Import image and move it around 14/06/18
sprite=pyglet.sprite.Sprite(image,x=(window_w/2)-(image.width/2),y=(window_h/2)-(image.height/2))
steps=10
sprite.y=sprite.y-steps
'''
###
'''
(https://www.youtube.com/watch?v=Szg6aNiu8s4       Loads image from same folder    14/06/18)
image=pyglet.resource.image("Tank.png")
'''
###
'''  https://www.youtube.com/watch?v=i6vpUyq7LyU       MOUSE CLICK/ Movement logs   14/6/18
from pyglet.window import mouse
@window.event
def on_mouse_press(x,y,button,modifiers):
    if button==mouse.LEFT:
        print("LEFT CLICK!")
    elif button==mouse.RIGHT:
        print("RIGHT CLICK!")
'''
###
'''https://www.youtube.com/watch?v=Wz-A451DM5s  15/06/18       Key Hold Motion
@window.event
def on_text_motion(motion):
    if (motion==pyglet.window.key.MOTION_DOWN):
        print("DOWN!")
        sprite.y=sprite.y-steps
    elif (motion==pyglet.window.key.MOTION_UP):
        print("UP!")
        sprite.y=sprite.y+steps
    elif (motion==pyglet.window.key.MOTION_LEFT):
        print("LEFT!")
        sprite.x=sprite.x-steps
    elif (motion==pyglet.window.key.MOTION_RIGHT):
        print("RIGHT!")
        sprite.x=sprite.x+steps
'''
###
''' 15/06/18  https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/image/index.html  Change Image Size
image=pyglet.resource.image("Tank.png")
image.width=150
image.height=150
'''
###
'''  Random Numbers  15/06/18  http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
import random
random_number=(random.randint(1,10))
'''
###
''' Object can't escape boundary   15/06/18
def on_text_motion(motion):
    if (motion==pyglet.window.key.MOTION_DOWN):
        if sprite.y>=0:
            sprite.y=sprite.y-steps
    elif (motion==pyglet.window.key.MOTION_UP):
        if sprite.y<=window_h-image.height:
            sprite.y=sprite.y+steps
    elif (motion==pyglet.window.key.MOTION_LEFT):
        if sprite.x>=0:
            sprite.x=sprite.x-steps
    elif (motion==pyglet.window.key.MOTION_RIGHT):
        if sprite.x<=window_w-image.width:
            sprite.x=sprite.x+steps
'''
###
'''Change Background Colour: Uses RGBA Colours   15/06/18 
from pyglet.gl import *
background_color = (0, .5, .3, 1)
window=pyglet.window.Window(width=window_w,height=window_h, resizable=True)
gl.glClearColor(*background_color)

'''
###
''' Sprite Rotation  18/06/18   https://pyglet.readthedocs.io/en/pyglet-1.2-maintenance/api/pyglet/sprite/pyglet.sprite.Sprite.html
sprite.rotation=90   (This rotates around anchor to face 90 degress)
#Also the anchor point should be centre of image to allow rotation
image.anchor_x=image.width/2
image.anchor_y=image.height/2
'''
###
'''
 Animation of sprite 18/06/18    https://xivilization.net/~marek/binaries/programming_guide.pdf
sprite.dx = 50.0
def update(dt):
    sprite.x += sprite.dx * dt
pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz

'''
###
'''Use the update function to remove objects  19/06/18 Playing around
if bullet_sprite.x<(tank_sprite.x+tankImage.width)and bullet_sprite.x>tank_sprite.x:
    print("HIT")
    tank_sprite.x=500000
    tank_sprite.y=500000
    bullet_sprite.x=500000
    bullet_sprite.y=500000

'''
###
'''

'''
###
#Library
import pyglet
from pyglet.gl import *
import time
#Windows
background_color = (0, .5, .3, 1)
window_w=1280
window_h=720
window=pyglet.window.Window(width=window_w,height=window_h)
gl.glClearColor(*background_color)
#Tank Image
tankImage=pyglet.resource.image("Tank.png")
tankImage.width=150
tankImage.height=150
tank_sprite=pyglet.sprite.Sprite(tankImage,x=(window_w/2)-(tankImage.width/2),y=(window_h/2)-(tankImage.height/2))
tankImage.anchor_x=tankImage.width/2
tankImage.anchor_y=tankImage.height/2
#Bullet Image
bulletImage=pyglet.resource.image("Bullet.png")
bulletImage.width=30
bulletImage.height=30
bullet_sprite=pyglet.sprite.Sprite(bulletImage,x=(window_w*3/4),y=(window_h/2))
bulletImage.anchor_x=bulletImage.width/2
bulletImage.anchor_y=bulletImage.height/2
#Explode Image
explodeImage=pyglet.resource.image("Explode.png")
explodeImage.width=300
explodeImage.height=300
explode_sprite=pyglet.sprite.Sprite(explodeImage,x=600000,y=600000)
#explodeImage.anchor_x=explodeImage.width/2
#explodeImage.anchor_y=explodeImage.height/2
#Draw function
@window.event
def on_draw():
    window.clear()
    tank_sprite.draw()
    bullet_sprite.draw()
    explode_sprite.draw()
    
#NEEDS TO FIX THE FIRST MOVE AFTER RUNNING


steps=10
speed=300

def collision():
    if (bullet_sprite.x<(tank_sprite.x+tankImage.width))and (bullet_sprite.x>tank_sprite.x):
        tempx=tank_sprite.x
        tempy=tank_sprite.y
        tank_sprite.x=500000
        tank_sprite.y=500000
        bullet_sprite.x=500000
        bullet_sprite.y=500000
        explode_sprite.x=tempx
        explode_sprite.y=tempy


#Key Functions
@window.event
def on_text_motion(motion):
    if (motion==pyglet.window.key.MOTION_DOWN):
        if bullet_sprite.y>=bulletImage.width/2:
            bullet_sprite.rotation=270
            bullet_sprite.dx = speed
            def update(dt):
                bullet_sprite.y= bullet_sprite.y- (bullet_sprite.dx * dt)
                collision()
            pyglet.clock.schedule_interval(update, 1/60.0)# update at 60Hz
    elif (motion==pyglet.window.key.MOTION_UP):
        if bullet_sprite.y<=window_h-(bulletImage.height/2):
            bullet_sprite.rotation=90
            bullet_sprite.dx = speed
            def update(dt):
                bullet_sprite.y= bullet_sprite.y+ (bullet_sprite.dx * dt)
                collision()
            pyglet.clock.schedule_interval(update, 1/60.0)
    elif (motion==pyglet.window.key.MOTION_LEFT):
        if bullet_sprite.x>=bulletImage.height/2:
            bullet_sprite.rotation=0
            bullet_sprite.dx = speed
            def update(dt):
                bullet_sprite.x= bullet_sprite.x- (bullet_sprite.dx * dt)
                collision()
            pyglet.clock.schedule_interval(update, 1/60.0)
    elif (motion==pyglet.window.key.MOTION_RIGHT):
        if bullet_sprite.x<=window_w-(bulletImage.width/2):
            bullet_sprite.rotation=180
            bullet_sprite.dx = speed
            def update(dt):
                bullet_sprite.x= bullet_sprite.x+ (bullet_sprite.dx * dt)
                collision()
            pyglet.clock.schedule_interval(update, 1/60.0)

#Run Window
pyglet.app.run()
