#5 - 50, 1 - 100
#3 unos - 1000
#4 unos - 1100
#5 unos - 10000
#para los cincos - 500,550,600
#combos - extra, se suman ademas de los puntos comunes

import random

def tirar_cubilete():
    list = []
    for i in range(5):
       list.append(random.randint(1, 6)) 
    return list

def cuantos_hay(elemento, lista):
    result = 0
    for i in range(len(lista)):
        if lista[i] == elemento:
            result = result + 1
    return result

def puntos_por_unos(lista_dados):
    puntaje = 0
    
    unos = cuantos_hay(1, lista_dados)
    
    puntaje = puntaje + unos*100
    
    if unos == 5:
        puntaje = puntaje + 10000
    elif unos == 4:
        puntaje = puntaje + 1100
    elif unos == 3:
        puntaje = puntaje + 1000
    return puntaje

def puntos_por_cincos(lista_dados):
    puntaje = 0
    cincos = cuantos_hay(5, lista_dados)
    puntaje = puntaje + cincos*50
    if cincos == 5:
        puntaje = puntaje + 600
    elif cincos == 4:
        puntaje = puntaje + 550
    elif cincos == 3:
        puntaje = puntaje + 500
    return puntaje

def total_puntos(lista_dados):
    puntaje = 0
    puntaje = puntaje + puntos_por_unos(lista_dados)
    puntaje = puntaje + puntos_por_cincos(lista_dados)
    return puntaje

def jugar_ronda(cant_jugadores):
    result = []
    for i in range(cant_jugadores):
        result.append(total_puntos(tirar_cubilete()))
    return result

def acumular_puntos(puntajes_acumulados, puntajes_ronda):
    if len(puntajes_acumulados) == len(puntajes_ronda):
        result = [0]*len(puntajes_acumulados)
        for i in range(len(puntajes_acumulados)):
            result[i] = puntajes_acumulados[i] + puntajes_ronda[i]
        return result
    else:
        print("Error")
        return

def hay_10mil(puntajes_acumulados):
    result = False
    for i in range(len(puntajes_acumulados)):
        if puntajes_acumulados[i] >= 10000:
            result = True
    return result

def partida_completa(cant_jugadores):
    puntajes = [0]*cant_jugadores
    rondas = 0
    while(True):
        if(not hay_10mil(puntajes)):
            puntajes = acumular_puntos(puntajes, jugar_ronda(cant_jugadores))
            rondas = rondas + 1
        else:
            break
    return rondas
    

list = []
for i in range(10000):
    list.append(partida_completa(10))
counter = 0
for i in range(len(list)):
    if(list[i] <= 18):
        counter = counter + 1
        
print(sum(list)/len(list))
print(counter/len(list))




################################################################################
def jugar():
    unos = 0
    cincos = 0
    
    puntaje = 0
    for i in range(5):
        a = random.randint(1, 6)
        if a == 1:
            puntaje = puntaje + 100
            unos = unos + 1
        elif a == 5:
            puntaje = puntaje + 50
            cincos = cincos + 1
    if unos == 5:
        puntaje = puntaje + 10000
    elif unos == 4:
        puntaje = puntaje + 1100
    elif unos == 3:
        puntaje = puntaje + 1000

    if cincos == 5:
        puntaje = puntaje + 600
    elif cincos == 4:
        puntaje = puntaje + 550
    elif cincos == 3:
        puntaje = puntaje + 500
        
    return puntaje

#print(jugar())
