# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de LISTAS
Electiva IV - Gestion de Datos con Python
"""

# =====================================================================
# Definicion y acceso
# =====================================================================
print("=== Definicion y acceso ===")
lista = [1, 2.5, 'SQL/PLSQL', [5, 6], 4]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[3][0])
print(lista[3][1])
print(lista[1:3])
print(lista[1:5])


# =====================================================================
# Listas son mutables
# =====================================================================
print("\n=== Mutabilidad ===")
nombres = ["Ana", "Bernardo"]
edades = [22, 21]
lista2 = [nombres, edades]
nombres += ["Cristina"]
print(lista2)
print("len(lista2):", len(lista2))
print("lista2[-1]:", lista2[-1])

lista2[1] = 'Electronica'
print(lista2)


# =====================================================================
# Metodos principales
# =====================================================================
print("\n=== append(), count(), extend() ===")
distribuciones_linux = ['Ubuntu', 'CentOS8.0', 'Debian', 'Debian']
distribuciones_linux.append('Redhat')
print(distribuciones_linux)
print("len:", len(distribuciones_linux))
print("count('Debian'):", distribuciones_linux.count('Debian'))

distribuciones_linux.extend(['Oracle Linux8.0'])
print("extend(['Oracle Linux8.0']):", distribuciones_linux)

print("\n=== index(), insert(), pop(), sort() ===")
distribuciones_linux = ['Ubuntu', 'CentOS8.0', 'Debian', 'Debian']
print("index('Ubuntu'):", distribuciones_linux.index('Ubuntu'))

distribuciones_linux.insert(2, 'Linux Mint')
print("insert(2,'Linux Mint'):", distribuciones_linux)

print("pop():", distribuciones_linux.pop())
print("lista tras pop():", distribuciones_linux)

distribuciones_linux.sort()
print("sort():", distribuciones_linux)

distribuciones_linux.sort(reverse=True)
print("sort(reverse=True):", distribuciones_linux)


# =====================================================================
# Otras particularidades
# =====================================================================
print("\n=== Otras particularidades ===")
numeros = [1, 2, 3]
numeros *= 3
print("[1,2,3]*3 ->", numeros)

letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
letras[1:4] = ["X"]
print("reemplazo de rango por lista ->", letras)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("count('apple'):", fruits.count('apple'))
print("index('banana'):", fruits.index('banana'))
print("index('banana', 4):", fruits.index('banana', 4))  # busca desde el indice 4


# =====================================================================
# EJERCICIOS RESUELTOS
# =====================================================================
print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)


# 3) Funcion que reciba la lista de empleados y muestre su informacion
def mostrar_empleados(empleados):
    """Recibe [nombres, edades, pesos] y muestra cada empleado enumerado."""
    nombres_e, edades_e, pesos_e = empleados
    for i in range(len(nombres_e)):
        print(f"Empleado_{i + 1}:{nombres_e[i]}, Edad: {edades_e[i]}, "
              f"Peso: {pesos_e[i]}")


nombres_emp = ['Luis', 'Pedro', 'Lucia']
edades_emp = [20, 18, 30]
peso_emp = [55.6, 60, 65.8]
empleados = [nombres_emp, edades_emp, peso_emp]

print("\n3) Informacion de empleados:")
mostrar_empleados(empleados)


# 4) Consultar: copy, remove, del, clear, in; diferencia append/extend
print("\n4) Metodos y operadores de listas:")
lista_demo = [1, 2, 3, 4]

# copy(): crea una copia superficial, independiente de la lista original
copia = lista_demo.copy()
print("   copy()    ->", copia)

# remove(valor): elimina la PRIMERA ocurrencia del valor indicado
lista_demo.remove(3)
print("   remove(3) ->", lista_demo)

# del lista[i]: elimina el elemento en la posicion (indice) dada
del lista_demo[0]
print("   del [0]   ->", lista_demo)

# in: verifica si un valor existe dentro de la lista (True/False)
print("   2 in lista_demo ->", 2 in lista_demo)

# clear(): vacia la lista (queda []), pero el objeto lista sigue existiendo
lista_demo.clear()
print("   clear()   ->", lista_demo)

# Diferencia entre append y extend:
lista_a = [1, 2, 3]
lista_a.append([4, 5])   # agrega TODO el argumento como UN solo elemento
print("   append([4,5]) ->", lista_a)   # [1, 2, 3, [4, 5]]

lista_b = [1, 2, 3]
lista_b.extend([4, 5])   # agrega cada elemento del iterable POR SEPARADO
print("   extend([4,5]) ->", lista_b)   # [1, 2, 3, 4, 5]


# 5) Funcion que revise si una lista tiene duplicados (sin modificarla)
def tiene_duplicados(lista):
    """Retorna True si hay algun elemento repetido, sin modificar la lista."""
    return len(lista) != len(set(lista))


lista_prueba = [1, 2, 2, 3, 4, 4, 5]
print(f"\n5) ¿{lista_prueba} tiene duplicados? -> {tiene_duplicados(lista_prueba)}")
print(f"   La lista original sigue igual -> {lista_prueba}")


# 6) Funcion que elimine duplicados de una lista
def eliminar_duplicados(lista):
    """Retorna una nueva lista sin elementos repetidos, conservando el orden."""
    sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados


print(f"\n6) Lista sin duplicados -> {eliminar_duplicados(lista_prueba)}")