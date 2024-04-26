

import random
import numpy as np
import matplotlib.pyplot as plt

def generar_bosque(cantidad:int):
    return np.repeat(0,cantidad)
#return np.zeros(cantidad)

def cuantos(bosque, tipo_celda):
    counter = 0
    for celda in bosque:
        if celda == tipo_celda:
            counter = counter + 1
    return counter


def suceso_aleatorio(p):
    if(random.randint(0,100)<=p):
        if(p != 0):
            return True
        else:
            return False
    else:
        return False

def brotes(bosque, p):
    bosque1 = bosque.copy()
    for i in range(len(bosque1)):
        if(suceso_aleatorio(p)):
            bosque1[i] = 1
    return bosque1

def rayos(bosque, f):
    bosque1 = bosque.copy()
    for i in range(len(bosque1)):
        if(suceso_aleatorio(f) and bosque1[i] == 1):
            bosque1[i] = -1
    return bosque1


def propagacion(bosque):
    bosque1 = bosque.copy()
    for a in range(len(bosque)):
        for i in range(len(bosque1)):
            if(bosque1[i] == 1):
                if(i != (len(bosque1)-1)):
                    if(bosque1[i+1] == -1):
                        bosque1[i] = -1
                if(i != 0):
                    if(bosque1[i-1] == -1):
                        bosque1[i] = -1
    return bosque1

def limpieza(bosque):
    bosque1 = bosque.copy()
    for i in range(len(bosque1)):
        if(bosque1[i] == -1):
            bosque1[i] = 0
    return bosque1

def dinamica(n, a, p, f):
    list = []
    for i in range(a):
        bosque = generar_bosque(n)
        bosque = brotes(bosque, p)
        bosque = rayos(bosque, f)
        bosque = propagacion(bosque)
        bosque = limpieza(bosque)
        list.append(cuantos(bosque, 1))
    return sum(list)/len(list)

max = 0
dict = {}
for i in range (0,101):
    value = dinamica(100,500,i,2)
    dict[i] = value
    if(value > max):
        max = value
#print(max)
#print(dict)
optimo = 0
for key in dict.keys():
    if dict[key] == max:
        optimo = key
print("Optimo: " + str(optimo))

plt.plot(dict.keys(), dict.values())
plt.ylabel("Result")
plt.show()


