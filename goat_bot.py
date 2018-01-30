
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from random import randint, uniform
import time

m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
while True:
    n = randint(0,3)
    if n == 0:
        #m.click(x_dim/8, y_dim/2, 1)
        k.press_key(k.down_key)
        k.press_key(k.left_key)
	time.sleep(uniform(0,.3))
        k.release_key(k.down_key)
	k.release_key(k.left_key)
    elif n == 1:
        #m.click(x_dim/8, y_dim/2, 1)
        k.press_key(k.down_key)
	k.press_key(k.right_key)
        time.sleep(uniform(0,.3))
        k.release_key(k.down_key)
	k.release_key(k.right_key)
    elif n == 2:
        #m.click(x_dim/8, y_dim/2, 1)
        k.press_key(k.right_key)
	k.press_key(k.up_key)
        time.sleep(uniform(0,.3))
        k.release_key(k.right_key)
	k.release_key(k.up_key)
    elif n == 3:
        #m.click(x_dim/8, y_dim/2, 1)
        k.press_key(k.up_key)
	k.press_key(k.left_key)
        time.sleep(uniform(0,.3))
        k.release_key(k.up_key)
	k.release_key(k.left_key)
