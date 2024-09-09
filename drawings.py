# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *
import keyboard as kb

def draw_house(loc_transformation, loc_color):
    '''
    Draws a cube and a pyramid above it to create a 3D house.
    '''

    # Getting the transformation matrixes needed to move our house.
    mat_rotation_x = get_mat_rotation_x(0.02)
    mat_rotation_y = get_mat_rotation_y(0.2)
    mat_translacao = get_mat_translation(0.7, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the shadowed cube parts.
    glUniform4f(loc_color, 0.74, 0.74, 0.32, 1.0) # baixo
    glDrawArrays(GL_TRIANGLE_STRIP, 4, 4)
    glUniform4f(loc_color, 0.74, 0.74, 0.32, 1.0) # direita
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    # Drawing and painting the lighted cube parts.
    glUniform4f(loc_color, 0.97, 0.97, 0.41, 1.0) # frente
    glDrawArrays(GL_TRIANGLE_STRIP, 8, 4)
    glUniform4f(loc_color, 0.97, 0.97, 0.41, 1.0) # atrás
    glDrawArrays(GL_TRIANGLE_STRIP, 12, 4)
    glUniform4f(loc_color, 0.97, 0.97, 0.41, 1.0) # esquerda
    glDrawArrays(GL_TRIANGLE_STRIP, 16, 4)
    glUniform4f(loc_color, 0.97, 0.97, 0.41, 1.0) # cima
    glDrawArrays(GL_TRIANGLE_STRIP, 20, 4)

    # Drawing and painting the shadowed pyramid parts.
    glUniform4f(loc_color, 0.75, 0.38, 0, 1.0) # baixo
    glDrawArrays(GL_TRIANGLE_STRIP, 24, 4)
    glUniform4f(loc_color, 0.75, 0.38, 0, 1.0) # direita
    glDrawArrays(GL_TRIANGLES, 28, 3)

    # Drawing and painting the lighted pyramid parts.
    glUniform4f(loc_color, 0.88, 0.44, 0, 1.0) # frente
    glDrawArrays(GL_TRIANGLES, 31, 3)
    glUniform4f(loc_color, 0.88, 0.44, 0, 1.0) # atrás
    glDrawArrays(GL_TRIANGLES, 34, 3)
    glUniform4f(loc_color, 0.88, 0.44, 0, 1.0) # esquerda
    glDrawArrays(GL_TRIANGLES, 37, 3)

def draw_tree(loc_transformation, loc_color, size):
    '''
    Draws a cylinder and a sphere above it to create a 3D tree.
    '''

    # Getting the transformation matrixes needed to move our tree.
    mat_rotation_x = get_mat_rotation_x(1.5)
    mat_rotation_z = get_mat_rotation_z(0)
    mat_scale      = get_mat_scale(kb.tree_scale, kb.tree_scale, kb.tree_scale)
    mat_translacao = get_mat_translation(-0.5, 0.3, -0.1)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_scale @ (mat_rotation_z @ mat_rotation_x))
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the cylinder.
    glUniform4f(loc_color, 0.4, 0.2, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['tree'][0], size['tree'][1] - size['tree'][0])

    glUniform4f(loc_color, 0, 0.6, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['tree'][1], size['tree'][2] - size['tree'][1])

def draw_sun(loc_transformation, loc_color, size):
    '''
    Draws a sphere with triangles acrros above it to create a 3D sun.
    '''

    # Getting the transformation matrixes needed to move our sun.
    mat_rotation_x = get_mat_rotation_x(0)
    mat_rotation_y = get_mat_rotation_y(0)
    mat_rotation_z = get_mat_rotation_z(kb.sun_rot)
    mat_translacao = get_mat_translation(0, 0.75, 0.98)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_rotation_z @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the traingles.
    glUniform4f(loc_color, 1, 0.9, 0, 1.0)
    for i in range (10):
        glDrawArrays(GL_TRIANGLE_STRIP, size['sun'][0] + 3*i,3)

    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 

    glUniform4f(loc_color, 1, 1, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['sun'][1], size['sun'][2] - size['sun'][1])

def draw_ground(loc_transformation, loc_color, size, colors):
    '''
    Draws a single plan (2D) to create a simple 3D ground.
    then add randomly generated grass in the form of triangles
    '''

    # Getting the transformation matrix needed to move our ground.
    mat_rotation_x = get_mat_rotation_x(0.1)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_rotation_x
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the ground plan.
    glUniform4f(loc_color, 0.17, 0.63, 0.17, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['ground'][0], 4)

    # Generating grass colors
    for i in range(len(colors)):
        glUniform4f(loc_color, 0.0, colors[i], 0.0, 1.0)
        glDrawArrays(GL_TRIANGLES, size['ground'][1] + i * 3, 3)
        

def draw_person(loc_transformation, loc_color, size):
    '''
    Draws a person using the same cilynder multiple times
    for the body and a sphere for the head
    '''
    global_mat_rotation_x = get_mat_rotation_x(0)
    global_mat_rotation_y = get_mat_rotation_y(0)
    global_mat_translacao = get_mat_translation(0.5 + kb.person_step, 0, -0.4)
    global_mat_scale = get_mat_scale(0.8,0.8,0.8)
    global_mat_transform = global_mat_translacao @ global_mat_scale @ (global_mat_rotation_y @ global_mat_rotation_x)
    
    # Getting the transformation matrixes needed to move our left leg.
    mat_rotation_x = get_mat_rotation_x(1)
    mat_rotation_y = get_mat_rotation_y(-1)
    mat_translacao = get_mat_translation(-0.45, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 

    glUniform4f(loc_color, 0, 0.8, 1, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][0], size['person'][1] - size['person'][0])

    
    # Getting the transformation matrixes needed to move our right leg.
    mat_rotation_x = get_mat_rotation_x(0.9)
    mat_rotation_y = get_mat_rotation_y(0.6)
    mat_translacao = get_mat_translation(-0.4, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    glUniform4f(loc_color, 0, 0.8, 1, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][0], size['person'][1] - size['person'][0])

    # Getting the transformation matrixes needed to move our torso.
    mat_rotation_x = get_mat_rotation_x(math.pi/2 + 0.1)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.4, 0.5, -0.05)

    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    glUniform4f(loc_color, 1, 0, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][0], size['person'][1] - size['person'][0])

    # Getting the transformation matrixes needed to move our left arm.
    mat_rotation_x = get_mat_rotation_x(-0.9)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.6, 0.1, -0.2)

    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    glUniform4f(loc_color, 1, 0.2, 0.2, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][0], size['person'][1] - size['person'][0])

    # Getting the transformation matrixes needed to move our right arm.
    mat_rotation_x = get_mat_rotation_x(-0.7)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.75, 0.15, 0)

    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    glUniform4f(loc_color, 1, 0, 0.2, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][0], size['person'][1] - size['person'][0])

    # Getting the transformation matrixes needed to move our head.
    mat_rotation_x = get_mat_rotation_x(1)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.3,0.64, 0)

    mat_transform = global_mat_transform @ mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    glUniform4f(loc_color, 1, 0.5, 0, 1.0)
    glDrawArrays(GL_TRIANGLE_STRIP, size['person'][1], size['person'][2] - size['person'][1])
    for triangle in range(size['person'][1],size['person'][2],3):
        glUniform4f(loc_color, 1, 0.5, 0, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)