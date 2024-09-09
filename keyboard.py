# File used to handle keyboard events.

import glfw

polyMode = False
tree_scale = 1

def key_event(window,key,scancode,action,mods):
    global polyMode
    global tree_scale

    if key == 80 and action == glfw.PRESS: 
        polyMode = not polyMode

    if key == 265 and action == glfw.PRESS:
        tree_scale += 0.1

    if key == 264 and action == glfw.PRESS:
        tree_scale -= 0.1