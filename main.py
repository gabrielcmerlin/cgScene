from OpenGL.GL import *
from config_screen import *
from drawings import *
from vertexes import *
from vertexes import *
import keyboard as kb

# Getting all the vertexes used in our project.

# Creating the house.
house = get_vertexes_house()

index_vertexes = {}
start = 0
index_vertexes['house'] = [start,len(house)]
start = len(house)

# Creating the person
person, coords_person = get_vertexes_person()

index_vertexes['person'] = [start]
for value in coords_person:
    index_vertexes['person'].append(index_vertexes['person'][-1] + value)
start = len(person) + start

# Creating the ground
ground, coords_ground, colors = get_vertexes_ground(10000)

index_vertexes['ground'] = [start]
for value in coords_ground:
    index_vertexes['ground'].append(index_vertexes['ground'][-1] + value)
start = len(ground) + start

# Creating the tree.
tree, coords_tree = get_vertexes_tree()

index_vertexes['tree'] = [start]
for value in coords_tree:
    index_vertexes['tree'].append(index_vertexes['tree'][-1] + value)
start = len(tree) + start

# Creating the sun.
sun, coords_sun = get_vertexes_sun()

index_vertexes['sun'] = [start]
for value in coords_sun:
    index_vertexes['sun'].append(index_vertexes['sun'][-1] + value)

# Joining everyone
vertexes = np.concatenate((house, person))
vertexes = np.concatenate((vertexes, ground))
vertexes = np.concatenate((vertexes, tree))
vertexes = np.concatenate((vertexes, sun))

#----------------------------------------------
# Configuring the screen used to show the objects.
window = init_window()
program = create_program()
send_data_to_gpu(program, vertexes)
render_window(window)

# Activating the keyboard handler function and initializing an auxiliar variable.
glfw.set_key_callback(window,kb.key_event)

#----------------------------------------------
# Getting GPU variables.

loc_color = get_loc_color(program)
loc_transformation = get_loc_transformation(program)

#----------------------------------------------
# Code main loop.
while not glfw.window_should_close(window):
    # Reading user interactions.
    glfw.poll_events()
    kb.sun_rot += kb.sun_speed
    kb.person_step += kb.person_speed

    # Activating the polygon view mode.
    if kb.polyMode:
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)

    # Clearing screen and loading a new solid background.
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glClearColor(1.0, 1.0, 1.0, 1.0)

    # Drawing the objects.
    draw_ground(loc_transformation, loc_color, index_vertexes, colors)
    draw_house(loc_transformation, loc_color)
    draw_person(loc_transformation, loc_color, index_vertexes)
    draw_tree(loc_transformation, loc_color, index_vertexes)
    draw_sun(loc_transformation, loc_color, index_vertexes)

    # Displaying the next frame.
    glfw.swap_buffers(window)

glfw.terminate()