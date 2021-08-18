from time import sleep
#from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
#keyboard = KeyboardController()
mouse = MouseController()



def click_mouse():
    sleep(1)
    # Read pointer position
    print('The current pointer position is {0}'.format(mouse.position))
    sleep(1)

    # Set pointer position center of the page
    mouse.position = (827, 366)
    print('Now we have moved it to {0}'.format(mouse.position))
    sleep(1)

    # Press and release 1
    mouse.click(Button.left, 2)
    sleep(2)
    # Press and release 2
    mouse.click(Button.left, 2)
    sleep(2)

    print("Key.SPACE")
    # Press and release space
    #keyboard.press(Key.space)
    #keyboard.release(Key.space)
    sleep(2)