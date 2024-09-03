from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
import numpy as np
from itertools import accumulate


# Getting all the vertexes used in our project.

# Creating the house
house = get_vertexes_house()
size = []
size.append(len(house))

# creating the person
person, size_person = get_vertexes_person()
size = size + size_person

# creating the ground
ground, size_ground = get_vertexes_ground()
size = size + size_person

# joining everyone
vertexes = np.concatenate((house, person))
vertexes = np.concatenate((vertexes, ground))
size = list(accumulate(size))

#----------------------------------------------
# Configuring the screen used to show the objects.
window = init_window()
program = create_program()
send_data_to_gpu(program, vertexes)
render_window(window)

#----------------------------------------------
# Getting GPU variables.

loc_color = get_loc_color(program)
loc_transformation = get_loc_transformation(program)

#----------------------------------------------
# Code main loop.
while not glfw.window_should_close(window):
    # Reading user interactions.
    glfw.poll_events() 

    # Clearing screen and loading a new solid background.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Drawing the objects.
    draw_house(loc_transformation, loc_color)
    draw_person(loc_transformation, loc_color, size)
    draw_ground(loc_transformation, loc_color, size)
    
    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()
