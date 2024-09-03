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