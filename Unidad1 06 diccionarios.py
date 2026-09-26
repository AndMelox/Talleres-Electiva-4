# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de DICCIONARIOS
Electiva IV - Gestion de Datos con Python
"""

# =====================================================================
# Definicion y almacenamiento de datos
# =====================================================================
print("=== Definicion y acceso ===")
diccionario = {"total": 55, "descuento": True, "subtotal": 15}
print(diccionario)

diccionario["version"] = 12.33
print("agregar clave nueva ->", diccionario)

usuario = {
    'nombre': 'Nombre del usuario',
    'edad': 23,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': False
    },
    'No medallas': 10
}
print(usuario)
print(type(usuario), len(usuario))

diccionario2 = {'Eduardo': 1, 'Fernando': 2, 'Uriel': 3, 'Rafael': 4}
print("keys():  ", list(diccionario2.keys()))
print("values():", list(diccionario2.values()))


# =====================================================================
# Metodos principales
# =====================================================================
print("\n=== clear(), copy(), fromkeys() ===")
versiones = dict(python=2.7, zope=2.13, plone=5.1)
otro_versiones = versiones.copy()
print("copy() == original ->", versiones == otro_versiones)

secuencia = ('python', 'zope', 'plone')
print("fromkeys(secuencia) ->", dict.fromkeys(secuencia))
print("fromkeys(secuencia, 0.1) ->", dict.fromkeys(secuencia, 0.1))

versiones.clear()
print("clear() ->", versiones)

print("\n=== items(), len(), pop(), del ===")
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print("items() ->", list(versiones.items()))
print("len()   ->", len(versiones))

versiones.pop('zope')
print("pop('zope') ->", versiones)

del versiones['plone']
print("del ['plone'] ->", versiones)

print("\n=== update() ===")
diccionario1 = {"color": "verde", "precio": 45}
diccionario2b = {"talle": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2b)
print("update() ->", diccionario1)

print("\n=== setdefault() y get() ===")
dic1 = {"color": "rosa", "marca": "Zara"}
print("setdefault('talle','U') ->", dic1.setdefault("talle", "U"))
print("dic1 tras setdefault    ->", dic1)
print("get('color') ->", dic1.get("color"))
print("'color' in dic1 ->", "color" in dic1)

print("\n=== Iterar un diccionario ===")
diccionario3 = {'color': 'rosa', 'marca': 'Zara', 'talle': 'U'}
for k, v in diccionario3.items():
    print(f"{k}: {v}")

print("\n=== enumerate() ===")
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

print("\n=== Construir diccionario con zip() ===")
key_list = ['id', 'name', 'salary']
value_list = [10, 'Hugo', 31.34]
empleado = {}
for key, value in zip(key_list, value_list):
    empleado[key] = value
print(empleado)


# =====================================================================
# EJERCICIOS RESUELTOS
# =====================================================================
print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)


# 1) Diccionario a partir de una lista, clasificando por letra inicial
def clasificar_por_letra(lista_palabras):
    resultado = {}
    for palabra in lista_palabras:
        letra = palabra[0].lower()
        resultado.setdefault(letra, []).append(palabra)
    return resultado


words = ['apple', 'bat', 'bar', 'atom', 'book', 'cat']
print("\n1) Clasificacion por letra inicial:")
print("  ", clasificar_por_letra(words))


# 2) Funcion que reciba una cadena y cuente vocales y consonantes
def contar_vocales_consonantes(cadena):
    vocales = "aeiou"
    conteo = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "Consonantes": 0}
    for letra in cadena.lower():
        if letra in vocales:
            conteo[letra] += 1
        elif letra.isalpha():
            conteo["Consonantes"] += 1
    return conteo


cad = "Gestion de Datos"
print(f"\n2) Conteo vocales/consonantes de '{cad}':")
print("  ", contar_vocales_consonantes(cad))


# 3) Convertir una cadena de clientes (separada por ; y \n) en un
#    diccionario anidado, usando el id como clave principal
def cadena_a_diccionario(cadena):
    lineas = cadena.split("\n")
    encabezado = lineas[0].split(";")   # ['id', 'nombre', 'correo', ...]
    campos = encabezado[1:]             # los campos que no son el id

    resultado = {}
    for linea in lineas[1:]:
        valores = linea.split(";")
        id_cliente = valores[0]
        datos_cliente = valores[1:]
        resultado[id_cliente] = dict(zip(campos, datos_cliente))
    return resultado


entrada = ("id;nombre;correo;movil;salario\n"
           "3412;Pepe Perez;pepeperez@yahoo.com;300281234;150000\n"
           "45342;Maria Melo;mariamelo@yahoo.com;315434223;300000\n"
           "5673321;Fernando Jimenez;ferjim@gmail.com;312342234;230000\n"
           "4545231;Carlos Cardenas;carloscardenas@hotmail.com;3156754323;345000")

print("\n3) Diccionario de clientes:")
diccionario_clientes = cadena_a_diccionario(entrada)
for id_cliente, datos in diccionario_clientes.items():
    print(f"   {id_cliente}: {datos}")