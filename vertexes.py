# File contaning functions that have the vertexes used to created a object. It is a simpler way to modularize
# our objects without using a bunch of files.

import numpy as np
import random
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
        Returns an array containing all the vertexes of our person object.

        The tree is created by a sphere above and 5 cylinders(the same one 5 times).
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
    cyl = cylinder(0.1,0.9)
    sph = sphere(0.3)
    vertexes = np.concatenate((cyl, sph))

    # Creating an array containing the amount of vertexes used in each shape.
    size = []
    size.append(len(cyl))
    size.append(len(sph))

    return vertexes, size

def get_vertexes_sun():
    '''
    Returns an array containing all the vertexes of our sun object.

    The tree is created by positioning a sphere with some triangles.
    '''

    # Preparing space for 30 vertexes using 3 coordinates (x,y,z).
    triangles = np.zeros(30, [("position", np.float32, 3)])

    # Filling the coordinates of each vertex.
    triangles['position'] = [
        # Triangle 1.
        (0.05*math.cos(0), 0.05*math.sin(0), 0.01),         
        (0.05*math.cos(math.pi/5), 0.05*math.sin(math.pi/5), 0.01),
        (0.12*math.cos(math.pi/10), 0.12*math.sin(math.pi/10), 0.01),

        # Triangle 2.
        (0.05*math.cos(math.pi/5), 0.05*math.sin(math.pi/5), 0.01),         
        (0.05*math.cos(2*math.pi/5), 0.05*math.sin(2*math.pi/5), 0.01),
        (0.12*math.cos(1.5*math.pi/5), 0.12*math.sin(1.5*math.pi/5), 0.01),

        # Triangle 3.
        (0.05*math.cos(2*math.pi/5), 0.05*math.sin(2*math.pi/5), 0.01),            
        (0.05*math.cos(3*math.pi/5), 0.05*math.sin(3*math.pi/5), 0.01),
        (0.12*math.cos(2.5*math.pi/5), 0.12*math.sin(2.5*math.pi/5), 0.01),

        # Triangle 4.
        (0.05*math.cos(3*math.pi/5), 0.05*math.sin(3*math.pi/5), 0.01),
        (0.05*math.cos(4*math.pi/5), 0.05*math.sin(4*math.pi/5), 0.01),
        (0.12*math.cos(3.5*math.pi/5), 0.12*math.sin(3.5*math.pi/5), 0.01),

        # Triangle 5.
        (0.05*math.cos(4*math.pi/5), 0.05*math.sin(4*math.pi/5), 0.01),         
        (0.05*math.cos(5*math.pi/5), 0.05*math.sin(5*math.pi/5), 0.01),
        (0.12*math.cos(4.5*math.pi/5), 0.12*math.sin(4.5*math.pi/5), 0.01),
        
        # Triangle 6.
        (0.05*math.cos(5*math.pi/5), 0.05*math.sin(5*math.pi/5), 0.01),           
        (0.05*math.cos(6*math.pi/5), 0.05*math.sin(6*math.pi/5), 0.01),
        (0.12*math.cos(5.5*math.pi/5), 0.12*math.sin(5.5*math.pi/5), 0.01),

        # Triangle 7.
        (0.05*math.cos(6*math.pi/5), 0.05*math.sin(6*math.pi/5), 0.01),            
        (0.05*math.cos(7*math.pi/5), 0.05*math.sin(7*math.pi/5), 0.01),
        (0.12*math.cos(6.5*math.pi/5), 0.12*math.sin(6.5*math.pi/5), 0.01),

        # Triangle 8.
        (0.05*math.cos(7*math.pi/5), 0.05*math.sin(7*math.pi/5), 0.01),
        (0.05*math.cos(8*math.pi/5), 0.05*math.sin(8*math.pi/5), 0.01),
        (0.12*math.cos(7.5*math.pi/5), 0.12*math.sin(7.5*math.pi/5), 0.01),

        # Triangle 9.
        (0.05*math.cos(8*math.pi/5), 0.05*math.sin(8*math.pi/5), 0.01),         
        (0.05*math.cos(9*math.pi/5), 0.05*math.sin(9*math.pi/5), 0.01),
        (0.12*math.cos(8.5*math.pi/5), 0.12*math.sin(8.5*math.pi/5), 0.01),
        
        # Triangle 10.
        (0.05*math.cos(9*math.pi/5), 0.05*math.sin(9*math.pi/5), 0.01),           
        (0.05*math.cos(10*math.pi/5), 0.05*math.sin(10*math.pi/5), 0.01),
        (0.12*math.cos(9.5*math.pi/5), 0.12*math.sin(9.5*math.pi/5), 0.01),
    ]
    sph = sphere(0.07)
    vertexes = np.concatenate((triangles, sph))

    # Creating an array containing the amount of vertexes used in each shape.
    size = []
    size.append(len(triangles))
    size.append(len(sph))

    return vertexes, size

def get_vertexes_ground(grass):
    '''
    Returns an array containing all the 4 vetexes of our ground object.

    The ground is created using only a plan.
    '''

    # Preparing space for 4 vertexes using 3 coordinates (x,y,z).
    ground = np.zeros(4, [("position", np.float32, 3)])

    # Filling the coordinates of each vertex.
    ground['position'] = [
        # Surface  1.
        (-1, -1.2, -1),
        (-1, 0.03, +1),
        (+1, -1.2, -1),
        (+1, 0.03,  +1),        
    ]
    grass_vertexes = []
    colors = []
    delta = 0.03
    for i in range(grass):
        # Random vertexes, but still on the plane
        # Since we have the ground as a plane 0x + 4y -2.46z + 2.34d = 0
        # we can manipulate this generation selecting two random values, for y and d for example
        # and finding the third with the formula
        x1 = np.random.uniform(-1, 1)
        y1 = np.random.uniform(-1.2, 0.03)
        z1 = (4 * y1 + 2.34) / 2.46

        # Generate new points close to the original ones with a range delta
        x2 = x1 + np.random.uniform(-delta, delta)
        y2 = y1 + np.random.uniform(-delta, delta)
        z2 = (4 * y2 + 2.34) / 2.46
        # The third point can be outside of the plane, but above, so 0x + 4y -2.46z + 2.34d > 0
        # we do this by adding a small value to one of its coordinates
        x3, y3, z3 = random.uniform((x1+x2)/2 - 0.1,(x1+x2)/2 + 0.1), random.uniform((y1+y2)/2 - 0.1,(y1+y2)/2 + 0.1), random.uniform((z1+z2)/2 - 0.03,(z1+z2)/2 + 0.03)
        y3 += delta
        colors.append(0.5 + random.uniform(0, 0.3))
        
        grass_vertexes.append((x1, y1, z1))
        grass_vertexes.append((x2, y2, z2))
        grass_vertexes.append((x3, y3, z3))
    grass_coord = np.zeros(3 *grass, [("position", np.float32, 3)])
    grass_coord['position'] = np.array(grass_vertexes)
    vertexes = np.concatenate((ground, grass_coord))

    size = []
    size.append(len(ground))
    size.append(len(grass_vertexes))

    return vertexes, size, colors