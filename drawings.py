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
    mat_translacao = get_mat_translation(0.5, 0.1, 0)

    # Getting a final transformation matrix and then sending it to GPU.
    mat_transform = mat_translacao @ (mat_rotation_y @ mat_rotation_x)
    glUniformMatrix4fv(loc_transformation, 1, GL_TRUE, mat_transform) 
    
    # Drawing and painting the cube parts.
    glUniform4f(loc_color, 1, 0, 0, 1.0) ### vermelho
    glDrawArrays(GL_TRIANGLE_STRIP, 0, 4)

    glUniform4f(loc_color, 0, 0, 1, 1.0) ### azul
    glDrawArrays(GL_TRIANGLE_STRIP, 4, 4)
    
    glUniform4f(loc_color, 0, 1, 0, 1.0) ### verde
    glDrawArrays(GL_TRIANGLE_STRIP, 8, 4)
    
    glUniform4f(loc_color, 1, 1, 0, 1.0) ### amarela
    glDrawArrays(GL_TRIANGLE_STRIP, 12, 4)
    
    glUniform4f(loc_color, 0.5, 0.5, 0.5, 1.0) ### cinza
    glDrawArrays(GL_TRIANGLE_STRIP, 16, 4)
    
    glUniform4f(loc_color, 0.5, 0, 0, 1.0) ### marrom
    glDrawArrays(GL_TRIANGLE_STRIP, 20, 4)

    # Drawing and painting the pyramid parts.
    glUniform4f(loc_color, 0, 1, 0, 1.0) ### verde
    glDrawArrays(GL_TRIANGLE_STRIP, 24, 4)

    glUniform4f(loc_color, 0.5, 0.5, 0.5, 1.0) ### cinza
    glDrawArrays(GL_TRIANGLES, 28, 3)

    glUniform4f(loc_color, 0, 0, 1, 1.0) ### azul
    glDrawArrays(GL_TRIANGLES, 31, 3)

    glUniform4f(loc_color, 0.5, 0, 0, 1.0) ### marrom
    glDrawArrays(GL_TRIANGLES, 34, 3)

    glUniform4f(loc_color, 1, 0, 0, 1.0) ### vermelho   
    glDrawArrays(GL_TRIANGLES, 37, 3)