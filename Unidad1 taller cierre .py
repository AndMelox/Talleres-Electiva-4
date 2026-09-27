# -*- coding: utf-8 -*-
#Taller Unidad I - Electiva IV Gestion de Datos con Python
#Docente: Jorge Enrique Quevedo Reyes
#Estudiante: Andres Melo - Oscar

import json
import math
from datetime import date

# PUNTO 1: Cargar el archivo json
with open("Unidad1_Reto.json", "r", encoding="utf-8") as j:
    mydata = json.load(j)

print("=" * 70)
print("PUNTO 1: Datos cargados correctamente")
print("=" * 70)
print(f"Cantidad de estudiantes cargados: {len(mydata)}\n")

# PUNTO 2: Nota promedio por asignatura
# Armamos un diccionario donde la llave es el nombre de la asignatura
# y el valor es una lista con todas las notas de esa asignatura.
# No quitamos las retiradas aqui porque eso solo lo pide el punto 3.

notas_por_asignatura = {}

for estudiante in mydata:
    for asignatura in estudiante["asignaturas"]:
        nombre_asig = asignatura["nombre"]
        notas_por_asignatura.setdefault(nombre_asig, []).append(asignatura["nota"])

promedio_por_asignatura = {
    nombre: round(sum(notas) / len(notas), 2)
    for nombre, notas in notas_por_asignatura.items()
}

print("=" * 70)
print("PUNTO 2: Nota promedio por asignatura")
print("=" * 70)
for nombre, promedio in promedio_por_asignatura.items():
    print(f"  {nombre}: {promedio}")
print()


# PUNTO 3: Nota promedio por estudiante (solo asignaturas NO retiradas)
#          Ordenado por apellido

def nombre_completo_estudiante(estudiante):
    nombres = estudiante["nombres"]
    partes = [nombres.get("primer_nombre", ""), nombres.get("segundo_nombre", "")]
    return " ".join(p for p in partes if p)


def apellido_completo_estudiante(estudiante):
    apellidos = estudiante["apellidos"]
    partes = [apellidos.get("primer_apellido", ""), apellidos.get("segundo_apellido", "")]
    return " ".join(p for p in partes if p)


promedio_por_estudiante = []  # lista de diccionarios

for estudiante in mydata:
    notas_validas = [
        a["nota"] for a in estudiante["asignaturas"] if a["retirada"] == "No"
    ]
    if notas_validas:
        promedio = round(sum(notas_validas) / len(notas_validas), 2)
    else:
        promedio = None  # el estudiante retiro todas sus asignaturas

    promedio_por_estudiante.append({
        "codigo": estudiante["codigo"],
        "nombre": nombre_completo_estudiante(estudiante),
        "apellido": apellido_completo_estudiante(estudiante),
        "promedio": promedio,
    })

# Se ordena por apellido (primer_apellido + segundo_apellido)
promedio_por_estudiante.sort(key=lambda e: e["apellido"])

print("=" * 70)
print("PUNTO 3: Nota promedio por estudiante (no retiradas) - por apellido")
print("=" * 70)
for est in promedio_por_estudiante:
    print(f"  {est['apellido']}, {est['nombre']} ({est['codigo']}): "
          f"{est['promedio']}")
print()

# PUNTO 4: Lista de estudiantes con correo institucional
# Reglas:
# - Dos nombres: {1a letra 1er nombre}{1a letra 2do nombre}.{1er apellido}
#                {2 ultimos digitos documento}
# - Un nombre:   {1a letra 1er nombre}{1a letra 1er apellido}.{2do apellido}
#                {2 ultimos digitos documento}
# - Dominio: @uptc.edu.co

def generar_correo(estudiante):
    nombres = estudiante["nombres"]
    apellidos = estudiante["apellidos"]

    primer_nombre = nombres.get("primer_nombre", "")
    segundo_nombre = nombres.get("segundo_nombre", "")
    primer_apellido = apellidos.get("primer_apellido", "")
    segundo_apellido = apellidos.get("segundo_apellido", "")

    documento = str(estudiante["documento"])
    ultimos_digitos = documento[-2:]

    if segundo_nombre:
        usuario = f"{primer_nombre[0]}{segundo_nombre[0]}.{primer_apellido}{ultimos_digitos}"
    else:
        usuario = f"{primer_nombre[0]}{primer_apellido[0]}.{segundo_apellido}{ultimos_digitos}"

    return f"{usuario.lower()}@uptc.edu.co"


estudiantes_correos = [
    (nombre_completo_estudiante(e) + " " + apellido_completo_estudiante(e),
     generar_correo(e))
    for e in mydata
]

print("=" * 70)
print("PUNTO 4: Estudiantes y correo institucional")
print("=" * 70)
for nombre, correo in estudiantes_correos:
    print(f"  {nombre}: {correo}")
print()

# PUNTO 5: Ejercicios de los cuadernillos de la Unidad 1

# 5.1 Cuadernillo de OPERADORES / FUNCIONES

# a) Vocal o consonante
def es_vocal(caracter):
    """Recibe un caracter y retorna True si es vocal, False si es consonante."""
    return caracter.lower() in "aeiou"


# b) Ecuacion cuadratica como funcion
def ecuacion_cuadratica(a, b, c):
    """Resuelve ax^2 + bx + c = 0 y retorna las raices (reales o complejas)."""
    discriminante = b ** 2 - 4 * a * c
    if discriminante >= 0:
        raiz = math.sqrt(discriminante)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
    else:
        raiz = math.sqrt(-discriminante)
        x1 = complex(-b / (2 * a), raiz / (2 * a))
        x2 = complex(-b / (2 * a), -raiz / (2 * a))
    return x1, x2


# c) Histograma
def histogram(lista):
    """Recibe una lista de numeros e imprime un histograma de 'H'."""
    for numero in lista:
        print("H" * numero)


print("=" * 70)
print("PUNTO 5.1: Operadores / Funciones")
print("=" * 70)
print(f"  '{'a'}' es vocal? -> {es_vocal('a')}")
print(f"  '{'z'}' es vocal? -> {es_vocal('z')}")
print(f"  Raices de x^2 - 5x + 6 = 0 -> {ecuacion_cuadratica(1, -5, 6)}")
print("  Histograma de [3, 5, 1]:")
histogram([3, 5, 1])
print()

# 5.2 Cuadernillo de CADENAS
print("=" * 70)
print("PUNTO 5.2: Cadenas")
print("=" * 70)

texto_demo = "gestion de datos"

# replace(): reemplaza todas las ocurrencias de una subcadena por otra
print("replace() ->", texto_demo.replace("datos", "python"))

# find(): retorna el indice de la primera aparicion, o -1 si no existe
print("find()    ->", texto_demo.find("de"))

# count(): cuenta cuantas veces aparece una subcadena
print("count()   ->", texto_demo.count("a"))

# capitalize(): pone en mayuscula solo la primera letra de la cadena
print("capitalize() ->", texto_demo.capitalize())

# title(): pone en mayuscula la primera letra de cada palabra
print("title()   ->", texto_demo.title())

# rstrip(): elimina espacios (u otros caracteres) al final de la cadena
print("rstrip()  ->", "'" + "  hola mundo   ".rstrip() + "'")

# index(): igual que find(), pero lanza ValueError si no encuentra la subcadena
print("index()   ->", texto_demo.index("datos"))

# casefold() es como lower() pero mas estricto, sirve mejor cuando se
# comparan cadenas que pueden traer tildes o caracteres especiales
print("casefold() ->", "GESTIÓN".casefold())

# Dividir una frase en palabras, en letras, reemplazar y unir
frase = "Gestión de Datos"
print("\nEntrada:", frase)
print("split()                       ->", frase.split())
print("replace('Gestión','Analítica')->", frase.replace("Gestión", "Analítica"))
print("'-'.join(frase)               ->", "-".join(frase))
print("'-'.join(frase.split())       ->", "-".join(frase.split()))

# Fecha actual -> extraer mes
hoy = date.today()
hoy_str = str(hoy)  # formato 'AAAA-MM-DD'
mes = hoy_str.split("-")[1]
print(f"\nFecha actual: {hoy_str} -> Mes {mes}")
print()

# 5.3 Cuadernillo de LISTAS
print("=" * 70)
print("PUNTO 5.3: Listas")
print("=" * 70)


def mostrar_empleados(empleados):
    """Recibe una lista [nombres, edades, pesos] e imprime cada empleado."""
    nombres, edades, pesos = empleados
    for i in range(len(nombres)):
        print(f"Empleado # {i + 1}: Nombre: {nombres[i]}, "
              f"Edad: {edades[i]}, Peso: {pesos[i]}")


nombres = ["Luis", "Pedro", "Lucia"]
edades = [20, 18, 30]
peso = [55.6, 60, 65.8]
empleados = [nombres, edades, peso]
mostrar_empleados(empleados)

# copy(), remove(), del, clear(), in, diferencia append/extend
print("\n-- Demostracion de metodos de listas --")
lista_demo = [1, 2, 3, 4]
copia = lista_demo.copy()          # copy(): copia superficial, independiente del original
print("copy()   ->", copia)

lista_demo.remove(3)               # remove(): elimina la PRIMERA ocurrencia del valor dado
print("remove(3)->", lista_demo)

del lista_demo[0]                  # del: elimina el elemento en la posicion (indice) indicada
print("del [0]  ->", lista_demo)

print("in       ->", 2 in lista_demo)  # in: verifica si un valor existe en la lista

lista_demo.clear()                 # clear(): vacia la lista, queda [] pero sigue existiendo
print("clear()  ->", lista_demo)

# Diferencia append vs extend
lista_a = [1, 2, 3]
lista_a.append([4, 5])             # append: agrega el argumento completo como UN solo elemento
print("append([4,5]) ->", lista_a)

lista_b = [1, 2, 3]
lista_b.extend([4, 5])             # extend: agrega cada elemento del iterable por separado
print("extend([4,5]) ->", lista_b)


def tiene_duplicados(lista):
    """Retorna True si hay algun elemento repetido, sin modificar la lista."""
    return len(lista) != len(set(lista))


def eliminar_duplicados(lista):
    """Retorna una nueva lista sin elementos duplicados, conservando el orden."""
    sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados


lista_prueba = [1, 2, 2, 3, 4, 4, 5]
print(f"\n¿'{lista_prueba}' tiene duplicados? -> {tiene_duplicados(lista_prueba)}")
print(f"Lista sin duplicados -> {eliminar_duplicados(lista_prueba)}")
print()

# 5.4 Cuadernillo de CONJUNTOS

print("=" * 70)
print("PUNTO 5.4: Conjuntos")
print("=" * 70)

# Diferencia entre set y frozenset:
# - set: es MUTABLE, se pueden agregar/quitar elementos (add, remove, etc.)
# - frozenset: es INMUTABLE, una vez creado no se puede modificar; por ser
#   inmutable, un frozenset SI puede usarse dentro de otro set o como
#   clave de diccionario (un set normal no puede).

# Demostración
conjunto_mutable = {1, 2, 3}
conjunto_inmutable = frozenset([1, 2, 3])

print("set original      ->", conjunto_mutable)
print("frozenset original->", conjunto_inmutable)

# Un set SI permite agregar elementos
conjunto_mutable.add(4)
print("set despues de add(4) ->", conjunto_mutable)

# Un frozenset NO permite agregar ni quitar elementos (no tiene add/remove)
try:
    conjunto_inmutable.add(4)
except AttributeError as error:
    print("Error al intentar modificar el frozenset ->", error)

# Por ser inmutable (hashable), un frozenset SI puede usarse como
# clave de un diccionario o guardarse dentro de otro set.
# Un set normal NO puede, porque no es hashable.
diccionario_con_frozenset_como_clave = {conjunto_inmutable: "conjunto congelado"}
print("Diccionario con frozenset como clave ->", diccionario_con_frozenset_como_clave)

try:
    diccionario_con_set_como_clave = {conjunto_mutable: "esto va a fallar"}
except TypeError as error:
    print("Error al usar un set normal como clave ->", error)

conj_a = {1, 2, 3, 4}
conj_b = {3, 4, 5, 6}

# intersection_update() modifica el conjunto sobre el que se llama, por eso
# aqui usamos una copia (copia_a) y asi no dañamos conj_a para los demas ejemplos
copia_a = conj_a.copy()
copia_a.intersection_update(conj_b)
print("intersection_update() ->", copia_a)

# isdisjoint(): True si los conjuntos NO tienen elementos en comun
print("isdisjoint()          ->", conj_a.isdisjoint({10, 11}))

# issubset(): True si todos los elementos del conjunto que llama el metodo
# estan dentro del otro (aqui probamos si {1,2} esta dentro de conj_a)
print("issubset()            ->", {1, 2}.issubset(conj_a))

# issuperset(): True si conj_a contiene todos los elementos del otro
print("issuperset()          ->", conj_a.issuperset({1, 2}))

# pop(): elimina y retorna un elemento arbitrario del conjunto
copia_pop = conj_a.copy()
elemento_sacado = copia_pop.pop()
print("pop()                 -> elemento:", elemento_sacado, "| queda:", copia_pop)

# remove(): elimina un elemento especifico (lanza error si no existe)
copia_remove = conj_a.copy()
copia_remove.remove(2)
print("remove(2)             ->", copia_remove)

# symmetric_difference(): elementos que estan en uno u otro, pero NO en ambos
print("symmetric_difference()->", conj_a.symmetric_difference(conj_b))

# symmetric_difference_update() hace lo mismo pero modifica el conjunto
# que la llama; usamos una copia (copia_sd) para no alterar conj_a
copia_sd = conj_a.copy()
copia_sd.symmetric_difference_update(conj_b)
print("symmetric_diff_update()->", copia_sd)

# union(): todos los elementos de ambos conjuntos, sin repetidos
print("union()               ->", conj_a.union(conj_b))

# update() agrega al conjunto que la llama todos los elementos del otro;
# usamos una copia (copia_update) para no tocar conj_a directamente
copia_update = conj_a.copy()
copia_update.update(conj_b)
print("update()              ->", copia_update)
print()


# 5.5 Cuadernillo de DICCIONARIOS
print("=" * 70)
print("PUNTO 5.5: Diccionarios")
print("=" * 70)


# a) Clasificar palabras por letra inicial
def clasificar_por_letra(lista_palabras):
    resultado = {}
    for palabra in lista_palabras:
        letra = palabra[0].lower()
        resultado.setdefault(letra, []).append(palabra)
    return resultado


words = ["apple", "bat", "bar", "atom", "book", "cat"]
print("Clasificacion por letra inicial:", clasificar_por_letra(words))


# b) Contar vocales y consonantes de una cadena
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
print(f"Conteo vocales/consonantes de '{cad}':", contar_vocales_consonantes(cad))


# c) Parsear cadena de clientes a diccionario anidado
def cadena_a_diccionario(cadena):
    lineas = cadena.split("\n")
    encabezado = lineas[0].split(";")  # ['id', 'nombre', 'correo', 'movil', 'salario']
    campos = encabezado[1:]            # los campos que no son el id

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

diccionario_clientes = cadena_a_diccionario(entrada)
print("\nDiccionario de clientes:")
for id_cliente, datos in diccionario_clientes.items():
    print(f"  {id_cliente}: {datos}")