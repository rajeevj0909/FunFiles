import pyglet
from pyglet.gl import *
from pyglet.window import mouse
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
#Tank2 Image
tank_sprite2=pyglet.sprite.Sprite(tankImage,x=((tankImage.width/2)+100),y=((tankImage.height/2)+100))
tank_sprite2.visible=True
tank_sprite2.rotation=270 
#Bullet Image
bulletImage=pyglet.resource.image("Bullet.png")
bulletImage.width=30
bulletImage.height=30
bullet_sprite=pyglet.sprite.Sprite(bulletImage,x=(window_w*3/4),y=(window_h/2))
bullet_sprite.visible=False
bulletImage.anchor_x=bulletImage.width/2
bulletImage.anchor_y=bulletImage.height/2
'''#Bullet2 Image
bullet_sprite2=pyglet.sprite.Sprite(bulletImage,x=(window_w*3/4),y=(window_h/2))
bullet_sprite2.visible=True'''
#IMAGE LIST
#ammo=[bullet_sprite,bullet_sprite2]
#Explode Image
explodeImage=pyglet.resource.image("Explode.png")
explodeImage.width=300
explodeImage.height=300
explode_sprite=pyglet.sprite.Sprite(explodeImage,x=(window_w/4),y=(window_h/2))
explode_sprite.visible=False
explodeImage.anchor_x=explodeImage.width/2
explodeImage.anchor_y=explodeImage.height/2
#Draw function
@window.event
def on_draw():
    window.clear()
    tank_sprite.draw()
    tank_sprite2.draw()
    bullet_sprite.draw()
    explode_sprite.draw()
#NEEDS TO FIX THE FIRST MOVE AFTER RUNNING

steps=10
speed=800
coll_listx=[tank_sprite.y+(tankImage.height/2),tank_sprite.y-(tankImage.height/2)]
coll_listy=[tank_sprite.x+(tankImage.width/2),tank_sprite.x-(tankImage.width/2)]
collision_under=(bullet_sprite.y<(tank_sprite.y+(tankImage.height/2)))
collision_over=(bullet_sprite.y>(tank_sprite.y-(tankImage.height/2)))
collision_left=(bullet_sprite.x<(tank_sprite.x+(tankImage.width/2)))
collision_right=(bullet_sprite.x>(tank_sprite.x-(tankImage.width/2)))
#if collision_under and collision_over and collision_left and collision_right:
#if bullet_sprite.x in coll_listx:
#if (bullet_sprite.y<(tank_sprite.y+(tankImage.height/2))) and (bullet_sprite.y>(tank_sprite.y-(tankImage.height/2))) and (bullet_sprite.x<(tank_sprite.x+(tankImage.width/2)))and (bullet_sprite.x>(tank_sprite.x-(tankImage.width/2))):   
    
def collision():
    if (bullet_sprite.y<(tank_sprite2.y+(tankImage.height/2))) and (bullet_sprite.y>(tank_sprite2.y-(tankImage.height/2))) and (bullet_sprite.x<(tank_sprite2.x+(tankImage.width/2)))and (bullet_sprite.x>(tank_sprite2.x-(tankImage.width/2))):
        tank_sprite2.visible=False
        bullet_sprite.visible=False
        explode_sprite.visible=True
        explode_sprite.x=tank_sprite2.x
        explode_sprite.y=tank_sprite2.y
        bullet_sprite.dy = 0
        bullet_sprite.x=-10
        bullet_sprite.y=-10
        #time.sleep(2)
        #explode_sprite.visible=False
        


#Key Functions
@window.event
def on_text_motion(motion):
    if (motion==pyglet.window.key.MOTION_DOWN):
        if tank_sprite.y>=0:
            tank_sprite.rotation=0 
            tank_sprite.y=tank_sprite.y-steps
    elif (motion==pyglet.window.key.MOTION_UP):
        if tank_sprite.y<=window_h-tankImage.height:
            tank_sprite.rotation=180 
            tank_sprite.y=tank_sprite.y+steps
    elif (motion==pyglet.window.key.MOTION_LEFT):
        if tank_sprite.x>=0:
            tank_sprite.rotation=90 
            tank_sprite.x=tank_sprite.x-steps
    elif (motion==pyglet.window.key.MOTION_RIGHT):
        if tank_sprite.x<=window_w-tankImage.width:
            tank_sprite.rotation=270
            tank_sprite.x=tank_sprite.x+steps
@window.event
def on_key_press(key,modifiers):
        if (key==pyglet.window.key.SPACE):
            bullet_sprite.visible=True
            if tank_sprite.rotation==90:#LEFT
                bullet_sprite.x=tank_sprite.x-tankImage.width/2
                bullet_sprite.y=tank_sprite.y
                bullet_sprite.rotation=0
                bullet_sprite.dx = speed
                def update(dt):
                    bullet_sprite.x -= bullet_sprite.dx * dt
                    collision()
                pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
            elif tank_sprite.rotation==0:#DOWN
                bullet_sprite.x=tank_sprite.x
                bullet_sprite.y=tank_sprite.y-tankImage.height/2
                bullet_sprite.rotation=270
                bullet_sprite.dy = speed
                def update(dt):
                    bullet_sprite.y -= bullet_sprite.dy * dt
                    collision()
                pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
            elif tank_sprite.rotation==180:#UP
                bullet_sprite.x=tank_sprite.x
                bullet_sprite.y=tank_sprite.y+tankImage.height/2
                bullet_sprite.rotation=90
                bullet_sprite.dy = speed
                def update(dt):
                    bullet_sprite.y += bullet_sprite.dy * dt
                    collision()
                pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
            elif tank_sprite.rotation==270:#RIGHT
                bullet_sprite.x=tank_sprite.x+tankImage.width/2
                bullet_sprite.y=tank_sprite.y
                bullet_sprite.rotation=180
                bullet_sprite.dx = speed
                def update(dt):
                    bullet_sprite.x += bullet_sprite.dx * dt
                    collision()
                pyglet.clock.schedule_interval(update, 1/60.0) # update at 60Hz
            bullet_sprite.visible=True
            #time.sleep(1)
            collision()
        

#Run Window
pyglet.app.run()
