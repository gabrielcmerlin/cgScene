# File contating functions that draw each one of our composed objects.

from OpenGL.GL import *
from geometric_transf import *

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

def draw_tree():
    pass

def draw_ground(loc_transformation, loc_color, size):
    '''
    Draws a person using the same cilynder multiple times
    for the body and a sphere for the head
    '''
    # Getting the transformation matrixes needed to move our house.
    mat_rotation_x = get_mat_rotation_x(-0.2)
    mat_rotation_y = get_mat_rotation_y(0.5)
    mat_translacao = get_mat_translation(0, -0.2, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the shadowed cube parts.
    glUniform4f(loc_color, 0, 1, 0.5, 1.0) # baixo
    glDrawArrays(GL_TRIANGLE_STRIP, size[2], 4)
    glUniform4f(loc_color, 0, 1, 0.5, 1.0) # direita
    glDrawArrays(GL_TRIANGLE_STRIP, size[2]+4, 4)

def draw_person(loc_transformation, loc_color, size):
    '''
    Draws a person using the same cilynder multiple times
    for the body and a sphere for the head
    '''
    # Getting the transformation matrixes needed to move our left leg.
    mat_rotation_x = get_mat_rotation_x(1)
    mat_rotation_y = get_mat_rotation_y(-1)
    mat_translacao = get_mat_translation(-0.45, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    
    for triangle in range(size[0],size[1],3):
        glUniform4f(loc_color, 0, 0.8, 1, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)
    
    # Getting the transformation matrixes needed to move our right leg.
    mat_rotation_x = get_mat_rotation_x(0.9)
    mat_rotation_y = get_mat_rotation_y(0.6)
    mat_translacao = get_mat_translation(-0.4, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    
    for triangle in range(size[0],size[1],3):
        glUniform4f(loc_color, 0, 0.8, 1, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)

    # Getting the transformation matrixes needed to move our torso.
    mat_rotation_x = get_mat_rotation_x(math.pi/2 + 0.1)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.4, 0.5, 0)

    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    
    for triangle in range(size[0],size[1],3):
        glUniform4f(loc_color, 1, 0, 0, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)

    # Getting the transformation matrixes needed to move our left arm.
    mat_rotation_x = get_mat_rotation_x(-0.9)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.6, 0.1, -1)

    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    
    for triangle in range(size[0],size[1],3):
        glUniform4f(loc_color, 1, 0.2, 0.2, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)

    # Getting the transformation matrixes needed to move our right arm.
    mat_rotation_x = get_mat_rotation_x(-0.7)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.75, 0.15, 0)

    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    
    for triangle in range(size[0],size[1],3):
        glUniform4f(loc_color, 1, 0, 0.2, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)

    # Getting the transformation matrixes needed to move our head.
    mat_rotation_x = get_mat_rotation_x(1)
    mat_rotation_y = get_mat_rotation_y(1)
    mat_translacao = get_mat_translation(-0.3,0.64, 0)

    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    for triangle in range(size[1],size[2],3):
        glUniform4f(loc_color, 1, 0.5, 0, 1.0)
        
        glDrawArrays(GL_TRIANGLES, triangle, 3)