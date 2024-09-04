# File contaning functions that have the vertexes used to created a object. It is a simpler way to modularize
# our objects without using a bunch of files.

import numpy as np
import math
from shapes import *

def get_vertexes_house():
    '''
    Returns an array containg all the 40 vertexes of our house object.

    The house is created by positioning a pyramid above a cube.
    '''

    # Preparing space for 40 vertexes using 3 coordinates (x,y,z).
    vertexes = np.zeros(40, [("position", np.float32, 3)])

    # Filling the coordinates of each vertex.
    vertexes['position'] = [
        # Cube face 1.
        (-0.2, -0.2, -0.2),
        (+0.2, -0.2, -0.2),         
        (-0.2, -0.2, +0.2),
        (+0.2, -0.2, +0.2),

        # Cube face 2.
        (+0.2, -0.2, +0.2),
        (+0.2, -0.2, -0.2),         
        (+0.2, +0.2, +0.2),
        (+0.2, +0.2, -0.2),

        # Cube face 3.
        (+0.2, -0.2, -0.2),
        (-0.2, -0.2, -0.2),            
        (+0.2, +0.2, -0.2),
        (-0.2, +0.2, -0.2),

        # Cube face 4.
        (-0.2, -0.2, +0.2),
        (+0.2, -0.2, +0.2),
        (-0.2, +0.2, +0.2),
        (+0.2, +0.2, +0.2),

        # Cube face 5.
        (-0.2, -0.2, -0.2),
        (-0.2, -0.2, +0.2),         
        (-0.2, +0.2, -0.2),
        (-0.2, +0.2, +0.2),
        
        # Cube face 6.
        (-0.2, +0.2, +0.2),
        (+0.2, +0.2, +0.2),           
        (-0.2, +0.2, -0.2),
        (+0.2, +0.2, -0.2),

        # Pyramid face 1.
        (+0.2, +0.2, +0.2),
        (+0.2, -0.2, +0.2),
        (-0.2, +0.2, +0.2),
        (-0.2, -0.2, +0.2),

        # Pyramid face 2.
        (+0.2, +0.2, +0.2),
        (+0.2, +0.2, -0.2),
        ( 0.0, +0.4,  0.0),

        # Pyramid face 3.
        (+0.2, +0.2, -0.2),
        (-0.2, +0.2, -0.2),
        ( 0.0, +0.4,  0.0),

        # Pyramid face 4.
        (+0.2, +0.2, +0.2),
        (-0.2, +0.2, +0.2),
        ( 0.0, +0.4,  0.0),

        # Pyramid face 5.
        (-0.2, +0.2, +0.2),
        (-0.2, +0.2, -0.2),
        ( 0.0, +0.4,  0.0)
    ]

    return vertexes

def get_vertexes_person():
    '''
        Generates the cylinder and the sphere for the person
    '''

    cyl = cylinder(0.1,0.5)
    sph = sphere(0.2)
    vertexes = np.concatenate((cyl, sph))

    size = []
    size.append(len(cyl))
    size.append(len(sph))

    return vertexes, size

def get_vertexes_tree():
    '''
    Returns an array containing all the vertexes of our tree object.

    The tree is created by positioning a sphere above a cylinder.
    '''

    # Generating the cylinder and sphere vertexes.
    cyl = cylinder(0.1,0.7)
    sph = sphere(0.3)
    vertexes = np.concatenate((cyl, sph))

    # Creating an array containing the amount of vertexes used in each shape.
    size = []
    size.append(len(cyl))
    size.append(len(sph))

    return vertexes, size

def get_vertexes_ground():
    '''
    Returns an array containing all the 4 vetexes of our ground object.

    The ground is created using only a plan.
    '''

    # Preparing space for 4 vertexes using 3 coordinates (x,y,z).
    vertexes = np.zeros(4, [("position", np.float32, 3)])

    # Filling the coordinates of each vertex.
    vertexes['position'] = [
        # Surface  1.
        (-1, -1.2, -1),
        (-1, 0.03, +1),
        (+1, -1.2, -1),
        (+1, 0.03,  +1),        
    ]

    return vertexes, [len(vertexes)]