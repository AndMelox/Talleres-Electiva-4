# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de OPERADORES
Electiva IV - Gestion de Datos con Python

Este script es interactivo: al ejecutarlo te pedira que ingreses
valores por teclado (usa input()). Es fiel al cuadernillo original.
"""

# =====================================================================
# Operadores Aritmeticos
# =====================================================================
# (+) Suma        (-) Resta        (*) Multiplicacion
# (/) Division    (//) Division entera    (**) Potencia

print("=== Operadores aritmeticos ===")
a = input("Ingresa un numero: ")
print(type(a))          # 'a' llega como str, aunque escribas un numero
print(a + '3')           # concatenacion de strings
print(int(a) + 3)        # suma numerica real
print(a + str(3))        # otra forma de concatenar


# =====================================================================
# Operadores logicos o booleanos: and, or, not
# =====================================================================
print("\n=== Operadores logicos ===")
a = input("Ingresa a: ")
b = input("Ingresa b: ")
c = input("Ingresa c: ")

if int(a) == 0 and int(b) == 0 and int(c) == 0:
    print('Cumple')
else:
    print('No Cumple')


# =====================================================================
# Operadores de comparacion
# =====================================================================
# ==, !=, >, <, >=, <=  -> siempre devuelven True o False
# [Imagen ilustrativa de la tabla de operadores de comparacion omitida,
#  ver el documento original de la unidad]

print("\n=== Operadores de comparacion ===")
print("5 > 3   ->", 5 > 3)
print("5 == 5  ->", 5 == 5)
print("5 != 4  ->", 5 != 4)


# =====================================================================
# Operadores de Identidad: is / is not
# =====================================================================
# is       -> True si dos variables apuntan al MISMO objeto en memoria
# is not   -> True si NO apuntan al mismo objeto

print("\n=== Operadores de identidad ===")
x = y = 1
print("x is y     ->", x is y)
print("x is not y ->", x is not y)

w = 3
z = 3
print("w is z     ->", w is z)
print("w is not z ->", w is not z)

# 'who' es un comando magico de Jupyter/IPython (lista variables definidas);
# no existe como funcion en un script plano de Python, por eso queda comentado:
# who

# '%reset -f' tambien es un comando magico de Jupyter, no de Python puro.

# Tipo de variable segun el valor asignado o calculado
r = 0.7071
print(type(r))
r = 45
print(type(r))
r = "casa"
print(type(r))

# Ejercicio de codificacion propuesto en el cuadernillo (flujograma de la
# ecuacion cuadratica, ver imagen "cuadratica.jpg" del documento original):
# la solucion como funcion queda resuelta en el archivo
# "Unidad1_02_Funciones.py" -> funcion ecuacion_cuadratica()