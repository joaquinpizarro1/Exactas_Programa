#import numpy as np
import random

def generar_bosque(n):
    tabla = []
    for i in range(0,n):
        x = 0
        tabla.append(x)
    return tabla

def suceso_aleatorio(p):
    prob = False
    a= random.randint(0, 100)
    if p >= a:
        prob = True
    return prob


def brotes(bosque, p):
    t = generar_bosque(bosque)
    for i in range(0, bosque):
        brote = suceso_aleatorio(p)
        if  brote == True:
            t[i] = 1
    return t

def cuantos(bosque, tipo_celda):
    celda = 0
    for i in range (0,len(bosque)):
        if bosque[i] == tipo_celda:
            celda = celda + 1
    return celda

def rayos(bosque, f):
    for i in range(0, len(bosque)):
        rayo = suceso_aleatorio(f)
        if  rayo == True and bosque[i] == 1:
            bosque[i] = -1
    return bosque

def propagacion(bosque):
    for i in range(0, len(bosque)):
        a = -1
        while bosque[i] == a:
            if i >= 1:   
                if bosque[i-1] == 1:
                    bosque[i-1] = -1
            if (len(bosque)-2) >= i:
                if bosque[i+1] == 1:
                    bosque[i+1] = -1
            a = 0
    return bosque

def limpieza(bosque): 
    bosque= propagacion(bosque)
    for i in range(0, len(bosque)):
        if bosque[i] == -1:
            bosque [i] = 0
    return bosque

def dinamica(n, a, p, f):
    prom_a = []
    promedio_sobreviviente = 0
    for i in range (0, a):
        arboles = brotes(n,p)
        arboles = rayos(arboles, f) 
        arboles = limpieza(arboles)
        cont = cuantos(arboles, 1)
        prom_a.append(cont)
    for i in range(0, a):
        promedio_sobreviviente = promedio_sobreviviente  + prom_a[i]
    promedio_sobreviviente = promedio_sobreviviente / a
    return promedio_sobreviviente

bosque = dinamica(5000,5,60,5)


