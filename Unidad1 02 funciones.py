# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de FUNCIONES
Electiva IV - Gestion de Datos con Python
"""

import math

# =====================================================================
# Funciones propias de Python: max() y min()
# =====================================================================
print("=== max() y min() ===")
a, b, c, d = 10, 30, 120, 500
print("maximo:", max(a, b, c, d))
print("minimo:", min(a, b, c, d))
print("max([3,6,1]):", max([3, 6, 1]))


# =====================================================================
# range() y list()
# =====================================================================
print("\n=== range() y list() ===")
print(type(range(10)))
print(list(range(7, 10)))
print(list(range(15)))
print(list(range(1, 11)))          # inicio distinto de 0
print(list(range(1, 11, 2)))       # con paso
print(list(range(0, -10, -1)))
print(list(range(-10, 0)))

for j in range(5):
    print(j)

lista = ["Hola", 1, 50.78, ['a', 'b']]
for l in lista:
    print(l)

# Imprimir la letra "b" del elemento sub-lista en la ultima posicion
print(lista[3][1])


# =====================================================================
# sum() y help()
# =====================================================================
print("\n=== sum() ===")
s = sum((a, b, c, d))
print(s)
print(sum([a, b, c, d]))
print(sum([3, 4, 2]))

# Suma de los numeros entre 2 y 20, de 2 en 2
print("Suma 2 a 20 de 2 en 2:", sum(range(2, 21, 2)))

# help(sum)  -> abre la ayuda interactiva; se deja comentado para no
#               bloquear la ejecucion del script.


# =====================================================================
# Funciones incorporadas usando modulos (import)
# =====================================================================
print("\n=== Uso de modulos: math ===")


def cal_funcionseno():
    angulo = 45
    ar = angulo * math.pi / 180
    return math.sin(ar)


print("seno(45):", cal_funcionseno())


def arit(a, i):
    print("factorial:", math.factorial(a))
    print("potencia:", math.pow(a, i))
    print("raiz*a redondeada:", round((math.sqrt(a) / 8) * a, 2))


arit(5, 3)


# =====================================================================
# Sintaxis general de una funcion propia
# =====================================================================
# def NOMBRE(LISTA_DE_PARAMETROS):
#     """DOCSTRING_DE_FUNCION"""
#     SENTENCIAS
#     return [EXPRESION]

# Variables locales y globales
def sumanumeros(a, b):
    global c
    c = a + b


sumanumeros(4, 5)
print("\nVariable global 'c' tras llamar sumanumeros(4,5):", c)


# =====================================================================
# EJERCICIOS RESUELTOS
# =====================================================================
print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)


# 1. Funcion que reciba un caracter y evalue si es vocal o consonante.
#    Si es vocal retorna True.
def es_vocal(caracter):
    """Recibe un caracter y retorna True si es vocal, False si es consonante."""
    return caracter.lower() in "aeiou"


print("\n1) es_vocal('a') ->", es_vocal('a'))
print("   es_vocal('z') ->", es_vocal('z'))


# 2. Ecuacion cuadratica convertida a funcion.
def ecuacion_cuadratica(a, b, c):
    """Resuelve ax^2 + bx + c = 0 y retorna sus dos raices."""
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


print("\n2) Raices de x^2 - 5x + 6 = 0 ->", ecuacion_cuadratica(1, -5, 6))
print("   Raices de x^2 + x + 1 = 0   ->", ecuacion_cuadratica(1, 1, 1))


# 3. Funcion que reciba una lista de numeros e imprima un histograma.
def histogram(lista):
    """Imprime una fila de 'H' por cada numero de la lista."""
    for numero in lista:
        print("H" * numero)


print("\n3) histogram([3, 5, 1]):")
histogram([3, 5, 1])