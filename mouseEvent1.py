from pynput.mouse import Button, Controller
import random

mouse = Controller()
while True:
    # Read pointer position
    print('The current pointer position is {0}'.format(mouse.position))
    screen_width,screen_height=100,100
    x=random.randrange(0,screen_width)
    y=random.randrange(0,screen_height)
    # Set pointer position
    mouse.position = (x,y)
    print('Now we have moved it to {0}'.format(mouse.position))

    # Press and release
    mouse.press(Button.right)
    mouse.release(Button.right)