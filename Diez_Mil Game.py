import random

def tirar_cubilete():
    cincodados = []
    for i in range (0,5):
        dado= random.randint(1, 6)
        cincodados.append(dado)
    return cincodados

def cuantos_hay(elemento, lista):
    rep = 0
    for i in range (0, 5):
        if lista[i] == elemento:
            rep = rep + 1 
    return rep

def puntos_por_unos(lista):
    unos = cuantos_hay(1, lista)
    if unos == 0:
        puntos_uno = 0
    if unos == 1:
        puntos_uno = 100
    if unos == 2:
        puntos_uno = 200
    if unos == 3:
        puntos_uno = 1000
    if unos == 4:
        puntos_uno = 1100
    if unos == 5:
        puntos_uno = 10000
    return puntos_uno

def puntos_por_cincos(lista): 
    cincos = cuantos_hay(5, lista)
    if cincos == 0:
        puntos_cinco = 0
    if cincos == 1:
        puntos_cinco = 50
    if cincos == 2:
        puntos_cinco = 100
    if cincos == 3:
        puntos_cinco = 500
    if cincos == 4:
        puntos_cinco = 550
    if cincos == 5:
        puntos_cinco = 600
    return puntos_cinco

def total_puntos(a, b):
    puntos = a + b 
    return puntos

def jugar_ronda(k): 
    puntos_ronda = []
    for i in range (0,k):
        lista = tirar_cubilete()
        a = puntos_por_cincos(lista)
        b = puntos_por_unos(lista)
        x = total_puntos(a,b)
        puntos_ronda.append(x)
    return puntos_ronda
    
def acumular_puntos(puntajes_acumulados, puntajes_ronda):
    acumulados = []
    for i in range (0, len(puntajes_acumulados)):  
        x = puntajes_acumulados[i] + puntajes_ronda[i]
        acumulados.append(x)
    return acumulados

def hay_10mil(puntajes):
    i = 0
    verificar = False 
    while verificar == False and i < len(puntajes):
        if puntajes[i] >= 10000:
            verificar = True
        i = i + 1
    return verificar

def partida_completa(k):
    rondas = 0
    check = False
    puntaje_acum = []
    for i in range (0,k):
        x = 0 
        puntaje_acum.append(x)
    while check == False:
        jugar = jugar_ronda(k)
        puntaje_acum = acumular_puntos (puntaje_acum, jugar)
        check = hay_10mil(puntaje_acum)
        print(puntaje_acum)
        rondas = rondas + 1
        
    return rondas

def promedio_rondas(reps):
    ronda = 0
    for i in range (0, reps):
        completo = partida_completa(10)
        ronda = completo + ronda
    prom = ronda / reps 
    
    return prom

promedio = promedio_rondas(10000)

    



