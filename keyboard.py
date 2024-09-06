# File used to handle keyboard events.

import glfw

polyMode = False

def key_event(window,key,scancode,action,mods):
    global polyMode

    if key == 80 and action == glfw.PRESS: 
        polyMode = not polyMode