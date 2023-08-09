import numpy as np

def crear_tablero(m,n): #Funcion que crear la tabla y la completa con una "M" en los bordes
    t = np.repeat(' ',(m+2)*(n+2)).reshape(m+2,n+2)
    for i in range (0,n+2):
       t[(0,i)] = 'M' 
       t[((m+2)-1,i)] = 'M'
    for i in range (0,m+2):
      t[(i,0)] = 'M' 
      t[(i,(n+2)-1)] = 'M'   
# definimos la coordenadas de los animales
    filas = [1, 2, 2, 3, 1]
    columnas = [3, 1, 3, 1, 1]
    animal = ["A", "A", "A", "A", "L"]
# y ahora los asignamos dentro del tablero
    for i in range(len(animal)):
        t[(filas[i], columnas[i])] = animal[i]
    return t
  
def vecinos_de(tablero, coord):
    lista_vecinos = []
    x,i = coord
    for p in range(i-1,i+2):
        for j in range(x-1,x+2):
          if (p > 0 and p < 5) and (j > 0 and j < 4):
                if tablero[j,p] != 'M':
                    q = (j,p)
                    if q != coord:
                        lista_vecinos.append(q) 
    return lista_vecinos

def buscar_adyacente(tablero, coord, objetivo):
    vecinos = vecinos_de(t,coord)
    ad = False 
    for i in range(len(vecinos)):
        if tablero[vecinos[i]] == objetivo and ad == False:
            ad = True
    return ad

def mover(tablero, coord):
    vecinos = vecinos_de(tablero,coord)
    ad = False 
    if tablero[coord] == 'L':
        ad = True
    if tablero[coord] == 'A':
        ad = True
    if ad == True: 
        ad = False
        for i in range(len(vecinos)):
           if tablero[vecinos[i]] == " " and ad == False:
               tablero[vecinos[i]] = tablero[coord]
               tablero[coord] = " "
               ad = True
    return tablero

def alimentar(tablero, coord):
    vecinos = vecinos_de(tablero,coord)
    ad = False
    if tablero[coord] == 'L':
        ad = True
    if ad == True:
       ad = False
       for i in range(len(vecinos)):
           if tablero[vecinos[i]] == "A" and ad == False:
               tablero[vecinos[i]] = tablero[coord]
               tablero[coord] = " "
               ad = True
    return tablero

def reproducir(tablero, coord):
    vecinos = vecinos_de(tablero,coord)
    ad = ' ' 
    if tablero[coord] == 'L':
        ad = 'L'
    if tablero[coord] == 'A':
        ad = 'A'
    a = False
    if ad == 'L': 
        for i in range(0,len(vecinos)):
            if tablero[vecinos[i]] == 'L':
                for j in range(i,len(vecinos)):
                    if tablero[vecinos[j]] == ' ' and a == False:
                        tablero[vecinos[j]] = tablero[coord]
                        a = True
    if ad == 'A': 
        for i in range(0,len(vecinos)):
            if tablero[vecinos[i]] == 'A':
                for j in range(i,len(vecinos)):
                    if tablero[vecinos[j]] == ' ' and a == False:
                        tablero[vecinos[j]] = tablero[coord]
                        a = True
    return tablero

def fase_mover(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]    
    for j in range(1, cantidad_columnas-1):
        for i in range(1, cantidad_filas-1):
            coord = (i,j)
            tablero = mover(tablero, coord)
    return tablero

def fase_alimentar(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for j in range(1, cantidad_columnas-1):
        for i in range(1, cantidad_filas-1):
            coord = (i,j)
            tablero = alimentar(tablero, coord)
    return tablero

def fase_reproducir(tablero):
    cantidad_filas = tablero.shape[0]
    cantidad_columnas = tablero.shape[1]
    for j in range(1, cantidad_columnas-1):
        for i in range(1, cantidad_filas-1):
            coord = (i,j)
            print (coord)
            tablero = reproducir(tablero, coord)
    return tablero

def evolucionar_en_el_tiempo(t, k):
    t = fase_alimentar(t)
    t = fase_reproducir(t)
    t = fase_mover(t)
    return t 

t = crear_tablero(3,4)
t = evolucionar_en_el_tiempo(t, 5)
