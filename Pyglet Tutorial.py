'''
https://youtu.be/wEBQEuriu7c       FULL SCREEN OR DIMENSIONS
Full screen:    window=pyglet.window.Window(fullscreen=True)
Dimensions:     window=pyglet.window.Window(width=1280,height=720)
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
sprite=pyglet.sprite.Sprite(image,x=image.width/2,y=image.height/4)
steps=10
sprite.y=sprite.y-steps
'''
###
'''
(https://www.youtube.com/watch?v=Szg6aNiu8s4       Loads image from same folder    14/06/18)
image=pyglet.resource.image("Tank.png")
'''
###
'''  https://www.youtube.com/watch?v=i6vpUyq7LyU        MOUSE CLICK/ Movement logs   14/6/18
from pyglet.window import mouse
@window.event
def on_mouse_press(x,y,button,modifiers):
    if button==mouse.LEFT:
        print("LEFT CLICK!")
    elif button==mouse.RIGHT:
        print("RIGHT CLICK!")
'''
###
'''https://www.youtube.com/watch?v=Wz-A451DM5s         Key Hold Motion
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
'''https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/modules/image/index.html  Change Image Size
image=pyglet.resource.image("Tank.png")
image.width=150
image.height=150
'''
###
'''

'''
###
'''

'''
###
'''
import pyglet

window=pyglet.window.Window(fullscreen=True)

image=pyglet.resource.image("Tank.png")
image.width=150
image.height=150
sprite=pyglet.sprite.Sprite(image,x=250,y=500)


@window.event
def on_draw():
    window.clear()
    sprite.draw()
    
steps=30
@window.event
def on_text_motion(motion):
    if (motion==pyglet.window.key.MOTION_DOWN):
        print("DOWN!")
        sprite.y=sprite.y-steps
        sprite.anchor_y=50
    elif (motion==pyglet.window.key.MOTION_UP):
        print("UP!")
        sprite.y=sprite.y+steps
        sprite.anchor_y=100
    elif (motion==pyglet.window.key.MOTION_LEFT):
        print("LEFT!")
        sprite.x=sprite.x-steps
    elif (motion==pyglet.window.key.MOTION_RIGHT):
        print("RIGHT!")
        sprite.x=sprite.x+steps
    


'''
pyglet.app.run()

