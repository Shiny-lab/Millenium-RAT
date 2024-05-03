import numpy as np
import pandas as pd




def coincidencia(lista):
    lista1 = []
    for element in lista:
        if element in lista1:
            return True
        else:
            lista1.append(element)
    return False

def sin_repetidos(lista):
    lista1 = []
    for element in lista:
        if not element in lista1:
            lista1.append(element)
    return lista1

def filtrar_filas(filas, columna, valor):
    result = []
    for i in range(len(filas)):
        if filas[i][columna] == valor:
            result.append(filas[i])
    return result


def convertir_en_lista(filas, columna):
    result = []
    for i in range(len(filas)):
        result.append(filas[i][columna])
    return result

def hay_coincidencia_en_equipo(filas, equipo):
    filas1 = filtrar_filas(filas, "Equipo", equipo)
    lista = convertir_en_lista(filas1, "dia_mes")
    return coincidencia(lista)

def porc_equipos_con_coincidencia(filas, equipos):
    counter = 0
    for i in range(len(equipos)):
        if(hay_coincidencia_en_equipo(filas, equipos[i]) == True):
            counter = counter + 1
    return counter/len(equipos)
    
def convertir_en_lista_sin_na(filas, columna):
    result = []
    for i in range(len(filas)):
        #if(str(filas[i][columna]) != "nan"):
        if(not pd.isna(filas[i][columna])):
            result.append(filas[i][columna])
    return result


datos_jugadores = pd.read_csv("datos_jugadores.csv")
filas = datos_jugadores.to_dict('records')

#a) Cuál es el promedio de edad de los delanteros de Vélez?

filas1 = filtrar_filas(filas, "Equipo", "Velez")
filas1 = filtrar_filas(filas1, "Puesto", "DEL")
total = 0
lista = convertir_en_lista_sin_na(filas1, "Edad")
for i in range(len(lista)):
    total = total + int(lista[i])
print(total/len(lista))


#b) Cuál es el jugador más viejo? A qué equipo pertenece?

lista = convertir_en_lista_sin_na(filas, "Edad")
maxima = 0
for i in range(len(lista)):
    if(int(lista[i]) > maxima):
        maxima = int(lista[i])
for i in range(len(filas)):
    if(filas[i]["Edad"] == maxima):
        print("Nombre: " + str(filas[i]["Jugador"]) + ", equipo: " + str(filas[i]["Equipo"]))

#c) Cuál es el puesto del jugador más petiso? A qué equipo pertenece?

lista = convertir_en_lista_sin_na(filas, "Altura_cm")
minima = 1000
for i in range(len(lista)):
    if(int(lista[i]) < minima):
        minima = int(lista[i])
    
for i in range(len(filas)):
    if(filas[i]["Altura_cm"] == minima):
        print("Puesto: " + str(filas[i]["Puesto"]) + ", equipo: " + str(filas[i]["Equipo"]))


#d ) Cuantos delanteros tiene Belgrano?

filas1 = filtrar_filas(filas, "Equipo", "Belgrano")
counter = 0
for i in range(len(filas1)):
    if(filas1[i]["Puesto"] == "DEL"):
        counter = counter + 1
print(counter)

#e) Cuantos defensores tienen menos de 20 o más de 30 años?
filas1 = filtrar_filas(filas, "Puesto", "DEF")
counter = 0
for i in range(len(filas1)):
    if(int(filas1[i]["Edad"]) >= 20 and int(filas1[i]["Edad"]) <= 30):
        counter = counter + 1
print(counter)

#f) Qué proporción de los jugadores nació en Enero?

counter = 0
for i in range(len(filas)):
    if(str(filas[i]["dia_mes"]).__contains__("ene")):
        counter = counter + 1
print(counter/len(filas))