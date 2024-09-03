# File containing functions that configure the screen that will be used to show our project.

import glfw
from OpenGL.GL import *

HEIGHT = 700
WIDTH = 700
WINDOW_NAME = 'Project 1'

# Shaders' code.
vertex_code = """
        attribute vec3 position;
        uniform mat4 mat_transformation;
        void main(){
            gl_Position = mat_transformation * vec4(position,1.0);
        }
        """
fragment_code = """
        uniform vec4 color;
        void main(){
            gl_FragColor = color;
        }
        """

def init_window():
    '''
    Instantiates a GLFW window.
    '''
    
    glfw.init()
    glfw.window_hint(glfw.VISIBLE, glfw.FALSE)
    window = glfw.create_window(WIDTH, HEIGHT, WINDOW_NAME, None, None)
    glfw.make_context_current(window)
    glfw.show_window(window)

    return window

def create_program():
    '''
    Requests GPU slots for the program and shaders to then compile and attach
    these shaders to this program slot.
    '''

    # Request a program and shader slots from GPU.
    program  = glCreateProgram()
    vertex   = glCreateShader(GL_VERTEX_SHADER)
    fragment = glCreateShader(GL_FRAGMENT_SHADER)

    # Set shaders source.
    glShaderSource(vertex, vertex_code)
    glShaderSource(fragment, fragment_code)

    # Compile shaders.
    glCompileShader(vertex)
    if not glGetShaderiv(vertex, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(vertex).decode()
        print(error)
        raise RuntimeError("Error compiling Vertex Shader.")
    glCompileShader(fragment)
    if not glGetShaderiv(fragment, GL_COMPILE_STATUS):
        error = glGetShaderInfoLog(fragment).decode()
        print(error)
        raise RuntimeError("Error compiling Fragment Shader.")

    # Attach shader objects to the program.
    glAttachShader(program, vertex)
    glAttachShader(program, fragment)

    # Build program.
    glLinkProgram(program)
    if not glGetProgramiv(program, GL_LINK_STATUS):
        print(glGetProgramInfoLog(program))
        raise RuntimeError('Error linking the program.')
        
    # Make program the default program.
    glUseProgram(program)

    return program

def send_data_to_gpu(program, vertexes):
    '''
    Requests GPU slots to program data and then sends this data to this slot.
    '''

    # Request a buffer slot from GPU.
    buffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)

    # Localize the GPU variable (the one we defined in vertex shader) that represents each vertex.
    loc_vertex = glGetAttribLocation(program, "position")
    glEnableVertexAttribArray(loc_vertex)

    # Sending vertexes data to this GPU variable.
    glBufferData(GL_ARRAY_BUFFER, vertexes.nbytes, vertexes, GL_DYNAMIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffer)
    stride = vertexes.strides[0]
    offset = ctypes.c_void_p(0)
    glVertexAttribPointer(loc_vertex, 3, GL_FLOAT, False, stride, offset)

def render_window(window):
    '''
    Render a already created window.
    '''

    glfw.show_window(window)
    glEnable(GL_DEPTH_TEST)

def get_loc_color(program):
    '''
    Returns the color variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "color")

def get_loc_transformation(program):
    '''
    Returns the transformation matrix variable localized in the GPU.
    '''

    return glGetUniformLocation(program, "mat_transformation")