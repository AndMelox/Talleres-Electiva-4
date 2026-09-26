# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de CADENAS (strings)
Electiva IV - Gestion de Datos con Python
"""

from datetime import date

# =====================================================================
# Indexacion basica
# =====================================================================
print("=== Indexacion ===")
asignatura = "Gestion de Datos"
print(type(asignatura))
print(asignatura[4])
print(asignatura[11])

# [Imagen ilustrativa del arreglo de caracteres de un string omitida,
#  ver el documento original de la unidad]

longitud = len(asignatura)
print("longitud:", longitud)
print("ultima letra (indice longitud-1):", asignatura[longitud - 1])
print("ultima letra (indice -1):", asignatura[-1])
print("penultima letra (indice -2):", asignatura[-2])


# =====================================================================
# Slicing (rebanadas)
# =====================================================================
print("\n=== Slicing ===")
s = 'Gestión de Datos'
print(s[0:5])
print(s[8:11])
print(s[:3])
print(s[3:])
print("s[3:3] (vacio) ->", repr(s[3:3]))


# =====================================================================
# Los strings son inmutables
# =====================================================================
print("\n=== Inmutabilidad ===")
fac = 'Ingeniería'
# fac[0] = 'J'   -> esto lanza TypeError, los strings no se pueden mutar
nueva_fac = 'J' + fac[1:]
print(nueva_fac)


# =====================================================================
# Operador in / comparacion de strings
# =====================================================================
print("\n=== Operador in y comparacion ===")
print("'ni' in fac ->", 'ni' in fac)
print("'b' in fac  ->", 'b' in fac)

if fac == 'Ingeniería':
    print('las cadenas son iguales')


# =====================================================================
# Metodo upper() y concatenacion
# =====================================================================
print("\n=== upper() y concatenacion ===")
print(fac.upper())

mensaje_fac = 'Facultad Ingeniería' + ' ' + 'Tunja'
print(mensaje_fac)


# =====================================================================
# format()
# =====================================================================
print("\n=== format() ===")
print("El valor es {}".format(69))
print("El valor es {}".format(12.3456))
print("Los valores son {}, {} y {}".format(1, 2, 3))
print("Los valores son {2}, {1} y {0}".format(1, 2, 3))


# =====================================================================
# Fecha del sistema
# =====================================================================
print("\n=== Fecha del sistema ===")
hoy = date.today()
print(hoy, type(hoy))


# =====================================================================
# EJERCICIOS RESUELTOS
# =====================================================================
print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

# 1) Consultar y explicar con un ejemplo: replace, find, count, capitalize,
#    title, rstrip, index, casefold
print("\n1) Metodos de manejo de cadenas:")
texto_demo = "gestion de datos"

# replace(viejo, nuevo): reemplaza TODAS las ocurrencias de 'viejo' por 'nuevo'
print("   replace()   ->", texto_demo.replace("datos", "python"))

# find(sub): retorna el indice de la primera aparicion, o -1 si no existe
print("   find()      ->", texto_demo.find("de"))

# count(sub): cuenta cuantas veces aparece una subcadena
print("   count()     ->", texto_demo.count("a"))

# capitalize(): pone en mayuscula solo la primera letra de toda la cadena
print("   capitalize()->", texto_demo.capitalize())

# title(): pone en mayuscula la primera letra de CADA palabra
print("   title()     ->", texto_demo.title())

# rstrip(): elimina espacios en blanco (u otros caracteres) al FINAL
print("   rstrip()    ->", "'" + "  hola mundo   ".rstrip() + "'")

# index(sub): igual que find(), pero lanza ValueError si no encuentra la subcadena
print("   index()     ->", texto_demo.index("datos"))

# casefold(): normaliza a minusculas de forma mas agresiva que lower(),
#             pensado para comparaciones (util con caracteres especiales
#             de otros idiomas, como la 'ß' alemana)
print("   casefold()  ->", "GESTIÓN".casefold())


# 2) Dividir una frase en palabras, en letras, reemplazar, fusionar/unir
print("\n2) Division/union de una frase:")
frase = "Gestión de Datos"
print("   Entrada:", frase)
print("   split()                        ->", frase.split())
print("   replace('Gestión','Analítica') ->", frase.replace("Gestión", "Analítica"))
print("   '-'.join(frase)                ->", "-".join(frase))
print("   '-'.join(frase.split())        ->", "-".join(frase.split()))


# 3) Obtener la fecha actual, pasarla a cadena y extraer el mes
print("\n3) Fecha actual -> mes:")
hoy_str = str(date.today())   # formato 'AAAA-MM-DD'
mes = hoy_str.split("-")[1]
print(f"   Fecha actual: {hoy_str} -> Mes {mes}")