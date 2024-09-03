# File contaning functions that have the vertexes used to created a object. It is a simpler way to modularize
# our objects without using a bunch of files.

import numpy as np

def get_vertexes_house():
    '''
    Returns an array containg all the 40 vertexes of our house object.

    The house is created positioning a pyramid above a cube.
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