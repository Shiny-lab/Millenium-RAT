


def obtener_alfabeto(archivo):
    contents = ""
    with open(archivo, "r", encoding="utf-8") as f:
        contents = f.read()
        return contents
    
def codificar_caracter(letra, alfabeto, k):
    index = alfabeto.index(letra)
    if (index + k <= len(alfabeto) - 1):
        return alfabeto[index + k]
    else:
        return alfabeto[index + k - len(alfabeto)]
    
def normalizar(mensaje):
    mensaje = mensaje.lower()
    mensaje_new = ""
    for i in mensaje:
        if i == "á":
            mensaje_new += "a"
        elif i == "é":
            mensaje_new += "e"
        elif i == "ú":
            mensaje_new += "u"
        elif i == "ó":
            mensaje_new += "o"
        elif i == "í":
            mensaje_new += "i"
        elif i == "ü":
            mensaje_new += "u"
        else:
            mensaje_new += i
    return mensaje_new


def codificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    mensaje_new = ""
    for i in mensaje:
        if i in alfabeto:
            mensaje_new += codificar_caracter(i, alfabeto, k)
        else:
            mensaje_new += i
    return mensaje_new

def decodificar_caracter(letra, alfabeto, k):
    index = alfabeto.index(letra)
    if (index - k >= 0):
        return alfabeto[index - k]
    else:
        return alfabeto[index - k + len(alfabeto)]

def decodificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    mensaje_new = ""
    for i in mensaje:
        if i in alfabeto:
            mensaje_new += decodificar_caracter(i, alfabeto, k)
        else:
            mensaje_new += i
    return mensaje_new


def codificar_archivo(archivo,alfabeto,k):
    contents = obtener_alfabeto(archivo)
    new_contents = codificar(contents, alfabeto, k)
    lista = archivo.split(".")
    lista.pop(len(lista) - 1)
    archivo1 = "".join(lista) + ".enc"
    with open(archivo1, "w", encoding="utf-8") as f:
        f.write(new_contents)
    return new_contents
        
def decodificar_archivo(archivo,alfabeto,k):
    contents = obtener_alfabeto(archivo)
    new_contents = decodificar(contents, alfabeto, k)
    lista = archivo.split(".")
    lista.pop(len(lista) - 1)
    archivo1 = "".join(lista) + ".dec"
    with open(archivo1, "w", encoding="utf-8") as f:
        f.write(new_contents)
    return new_contents

def quitar(elementos, lista):
    new_lista = []
    for i in range(len(lista)):
        if not lista[i] in elementos:
            new_lista.append(lista[i])
    return new_lista


def sin_repetidos(cadena):
    result = ""
    for i in cadena:
        if result.find(i) == -1:
            result += i
    return result


def crear_codificacion(palabra, alfabeto):
    palabra = sin_repetidos(palabra)
    a = list(palabra) + quitar(list(palabra), list(alfabeto))
    dicctionary = {}
    if len(a) == len(alfabeto):
        for i in range(len(alfabeto)):
            dicctionary[alfabeto[i]] = a[i]
    return dicctionary

def codificar_con_dicc(mensaje,diccionario):
    mensaje = normalizar(mensaje)
    mensaje_new = ""
    for i in mensaje:
        if i in diccionario.keys():
            mensaje_new += diccionario[i]
        else:
            mensaje_new += i
    return mensaje_new

def decodificar_con_dicc(mensaje,diccionario):
    mensaje = normalizar(mensaje)
    mensaje_new = ""
    for i in mensaje:
        if i in diccionario.values():
            mensaje_new += list(diccionario.keys())[list(diccionario.values()).index(i)]
        else:
            mensaje_new += i
    return mensaje_new


def codificar_archivo_con_dicc(archivo,diccionario):
    contents = obtener_alfabeto(archivo)
    new_contents = codificar_con_dicc(contents, diccionario)
    lista = archivo.split(".")
    lista.pop(len(lista) - 1)
    archivo1 = "".join(lista) + ".enc"
    with open(archivo1, "w", encoding="utf-8") as f:
        f.write(new_contents)
    return new_contents


def decodificar_archivo_con_dicc(archivo,diccionario):
    contents = obtener_alfabeto(archivo)
    new_contents = decodificar_con_dicc(contents, diccionario)
    lista = archivo.split(".")
    lista.pop(len(lista) - 1)
    archivo1 = "".join(lista) + ".dec"
    with open(archivo1, "w", encoding="utf-8") as f:
        f.write(new_contents)
    return new_contents

alf = obtener_alfabeto("alfabeto.txt")
dicc = {'a':'1','b':'9','c':'2','d':'-'}
print(decodificar_archivo_con_dicc("original.enc",dicc))



