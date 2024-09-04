import math
import numpy as np

PI = 3.141592

def CoordCilindro(t, h, r):
    x = r * math.cos(t)
    y = r * math.sin(t)
    z = h
    return (x,y,z)

def CoordSphere(u,v,r):
    x = r*math.sin(v)*math.cos(u)
    y = r*math.sin(v)*math.sin(u)
    z = r*math.cos(v)
    return (x,y,z)

def cylinder(r = 0.1, H = 0.5):

    num_sectors = 20 # qtd de sectors (longitude)
    num_stacks = 20 # qtd de stacks (latitude)

    # grid sectos vs stacks (longitude vs latitude)
    sector_step = (PI*2)/num_sectors # variar de 0 até 2π
    stack_step = H/num_stacks # variar de 0 até H

    # Entrada: angulo de t, altura h, raio r
    # Saida: coordenadas no cilindro

    # vamos gerar um conjunto de vertices representantes poligonos
    # para a superficie da esfera.
    # cada poligono eh representado por dois triangulos
    vertices_list = []
    for j in range(0,num_stacks): # para cada stack (latitude)
        
        for i in range(0,num_sectors): # para cada sector (longitude) 
            
            u = i * sector_step # angulo setor
            v = j * stack_step # altura da stack
            
            un = 0 # angulo do proximo sector
            if i+1==num_sectors:
                un = PI*2
            else: un = (i+1)*sector_step
                
            vn = 0 # altura da proxima stack
            if j+1==num_stacks:
                vn = H
            else: vn = (j+1)*stack_step
            
            # verticies do poligono
            p0=CoordCilindro(u, v, r)
            p1=CoordCilindro(u, vn, r)
            p2=CoordCilindro(un, v, r)
            p3=CoordCilindro(un, vn, r)
            
            # triangulo 1 (primeira parte do poligono)
            vertices_list.append(p0)
            vertices_list.append(p2)
            vertices_list.append(p1)
            
            # triangulo 2 (segunda e ultima parte do poligono)
            vertices_list.append(p3)
            vertices_list.append(p1)
            vertices_list.append(p2)
                        
            if v == 0:
                vertices_list.append(p0)
                vertices_list.append(p2)
                vertices_list.append(CoordCilindro(0, v, 0))
            if vn == H:
                #faz um triangulo a partir do mesmo angulo u, mas com as alturas em h = vn
                vertices_list.append(p1)
                vertices_list.append(p3)
                vertices_list.append(CoordCilindro(0, vn, 0))

    total_vertices = len(vertices_list)
    vertices = np.zeros(total_vertices, [("position", np.float32, 3)])
    vertices['position'] = np.array(vertices_list)

    return vertices

def sphere(r = 0.5):
    num_sectors = 20 # qtd de sectors (longitude)
    num_stacks = 20 # qtd de stacks (latitude)


    # grid sectos vs stacks (longitude vs latitude)
    sector_step=(PI*2)/num_sectors # variar de 0 até 2π
    stack_step=(PI)/num_stacks # variar de 0 até π

    vertices_list = []
    for i in range(0,num_sectors): # para cada sector (longitude)
        for j in range(0,num_stacks): # para cada stack (latitude)
            
            
            
            u = i * sector_step # angulo setor
            v = j * stack_step # angulo stack
            
            un = 0 # angulo do proximo sector
            if i+1==num_sectors:
                un = PI*2
            else: un = (i+1)*sector_step
                
            vn = 0 # angulo do proximo stack
            if j+1==num_stacks:
                vn = PI
            else: vn = (j+1)*stack_step
            
            # vertices do poligono
            p0=CoordSphere(u, v, r)
            p1=CoordSphere(u, vn, r)
            p2=CoordSphere(un, v, r)
            p3=CoordSphere(un, vn, r)
            
            # triangulo 1 (primeira parte do poligono)
            vertices_list.append(p0)
            vertices_list.append(p2)
            vertices_list.append(p1)
            
            # triangulo 2 (segunda e ultima parte do poligono)
            vertices_list.append(p3)
            vertices_list.append(p1)
            vertices_list.append(p2)


    total_vertices = len(vertices_list)
    vertices = np.zeros(total_vertices, [("position", np.float32, 3)])
    vertices['position'] = np.array(vertices_list)

    return vertices