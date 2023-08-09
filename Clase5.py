import numpy as np

def crear_tablero(n): #Funcion que crear la tabla y la completa con 0
    t = np.repeat(0,n*n).reshape(n,n)
    for i in range (0,n):
        t[(0,i)] = -1
        t[(n-1,i)] = -1
        t[(i,0)] = -1
        t[(i,n-1)] = -1
    return t

def es_borde(tablero, coord):
    bool1 = False
    if tablero[(coord)] == -1:
        bool1 = True
    return bool1

def tirar_copo(tablero, coord):
    tablero[coord] = tablero[coord] + 1
    return tablero

def vecinos_de(tablero, coord):
    lista_vecinos = []
    x,i = coord
    if tablero[x+1,i] != -1:
        q = (x+1,i)
        lista_vecinos.append(q)
    if tablero[x-1,i] != -1:
        q = (x-1,i)
        lista_vecinos.append(q)
    if tablero[x,i+1] != -1:
        q = (x,i+1)
        lista_vecinos.append(q)
    if tablero[x+1,i-1] != -1:
        q = (x,i-1)
        lista_vecinos.append(q)
    return lista_vecinos
    
def desbordar_posicion(tablero, coord):
    x,i = coord
    if tablero[coord] >= 4:
        if tablero[x+1,i] != -1:
            q = (x+1,i)
            tablero[q] += 1
        if tablero[x-1,i] != -1:
            q = (x-1,i)
            tablero[q] += 1
        if tablero[x,i+1] != -1:
            q = (x,i+1)
            tablero[q] += 1
        if tablero[x+1,i-1] != -1:
            q = (x,i-1)
            tablero[q] += 1
        tablero[coord] = tablero[coord] - 4
    return tablero

def desbordar_valle(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if tablero[i,j] != -1 and tablero[i,j] >= 4:
                coord = (i,j)
                tablero = desbordar_posicion(tablero, coord)
    return tablero

def hay_que_desbordar(tablero):
    desbordar = False
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for i in range(1, cantidad_filas - 1):
        for j in range(1, cantidad_columnas - 1):
            if tablero[i,j] >= 4:
                desbordar = True
    return desbordar
    
def estabilizar(tablero):
    while (hay_que_desbordar(tablero)):
        tablero = desbordar_valle(tablero)
    return tablero

def paso(t): #llamo a la funcion para que la complete con 0
    coord = (4,4)
    for i in range (0,12):
        t = tirar_copo(t, coord)
    #t1 = desbordar_posicion(t1, coord)
    #t1 = desbordar_valle(t1)
    #check = hay_que_desbordar(t1)
    
    t = estabilizar(t)
    return t

import imageio
import os
from matplotlib import pyplot as plt 

def guardar_foto(t, paso):
    dir_name = "output"
    if not os.path.exists(dir_name): # me fijo si no existe el directorio
        os.mkdir(dir_name) #si no existe lo creo
        
    ax = plt.gca()
    file_name = os.path.join(dir_name, "out{:05}.png".format(paso))
    plt.imshow(t, vmin=-1, vmax=3)
    ax.set_title("Copos tirados: {}".format(paso+1)) #titulo
    plt.savefig(file_name)
    
def hacer_video(cant_fotos):
    dir_name = "output"
    lista_fotos=[]
    for i in range (cant_fotos):
        file_name = os.path.join(dir_name, "out{:05}.png".format(i))
        lista_fotos.append(imageio.imread(file_name))
        
    video_name = os.path.join(dir_name, "avalancha.mp4")
    # genero el video con 10 Copos por segundo. Explorar otros valores:
    imageio.mimsave(video_name, lista_fotos, fps=10)
    print('Estamos trabajando en el directorio', os.getcwd())
    print('y se guardo el video:', video_name)
    
def probar(n, pasos):
    t = crear_tablero(n)
    for i in range(pasos):
        paso(t)
        guardar_foto(t, i)
    hacer_video(pasos)
    return t

t1 = probar (9, 200)
