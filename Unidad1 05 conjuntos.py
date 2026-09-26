# -*- coding: utf-8 -*-
"""
Unidad 1 - Repaso de CONJUNTOS (set)
Electiva IV - Gestion de Datos con Python
"""

# =====================================================================
# Definicion de conjuntos
# =====================================================================
print("=== Definicion de conjuntos ===")
s = {True, 3.14, None, False, "Hola mundo", (1, 2)}
print(s, type(s))

# Un conjunto NO puede contener objetos mutables como listas o diccionarios:
# s = {[1, 2]}   -> lanza TypeError: unhashable type: 'list'

s_vacio = set()
print("conjunto vacio:", s_vacio)

s1 = set([1, 2, 2, 3, 4])   # los repetidos se eliminan automaticamente
s2 = set(range(10))
print(s1)
print(s2)

# Un conjunto a partir de un string: los caracteres repetidos se eliminan
a = set("Hola Pythonista".upper())
print(a)


# =====================================================================
# Recorrer un conjunto (no tiene indices, es una coleccion desordenada)
# =====================================================================
print("\n=== Recorrer un conjunto ===")
mi_conjunto = {1, 3, 2, 9, 3, 1}
for numero in mi_conjunto:
    print(numero)
# mi_conjunto[0]  -> lanza TypeError, los sets no admiten indexacion


# =====================================================================
# Metodos principales
# =====================================================================
print("\n=== add(), clear(), copy() ===")
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
print(set_mutable1)
set_mutable1.add(22.000001)
print("add(22.000001) ->", set_mutable1)

copia_set = set_mutable1.copy()
print("copia == original ->", copia_set == set_mutable1)

set_mutable1.clear()
print("clear() ->", set_mutable1)

print("\n=== difference() / difference_update() ===")
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8, 2])
print("A.difference(B) ->", set_mutable1.difference(set_mutable2))
print("B.difference(A) ->", set_mutable2.difference(set_mutable1))
print("A - B (equivalente) ->", set_mutable1 - set_mutable2)

proyecto1 = {'python', 'Zope2', 'ZODB3', 'pytz'}
proyecto2 = {'python', 'Plone', 'diazo'}
proyecto2.difference_update(proyecto1)   # actualiza proyecto2 in-place
print("difference_update() ->", proyecto2)

print("\n=== discard() ===")
paquetes = {'python', 'zope', 'plone', 'django'}
paquetes.discard('django')   # no falla aunque el elemento no exista
print("discard('django') ->", paquetes)

print("\n=== intersection() ===")
set_mutable1 = set([4, 3, 11, 7, 5, 2, 1, 4])
set_mutable2 = set([11, 5, 9, 2, 4, 8])
print("intersection() ->", set_mutable1.intersection(set_mutable2))
print("& (equivalente) ->", set_mutable1 & set_mutable2)


# =====================================================================
# EJERCICIOS RESUELTOS
# =====================================================================
print("\n" + "=" * 60)
print("EJERCICIOS")
print("=" * 60)

# 1) Diferencia entre set y frozenset
print("""
1) set vs frozenset:
   - set:       es MUTABLE. Se pueden agregar/quitar elementos (add,
                remove, discard, update, etc.).
   - frozenset: es INMUTABLE. Una vez creado no se puede modificar (no
                tiene add/remove). Por ser inmutable y "hasheable", un
                frozenset SI puede colocarse dentro de otro set o usarse
                como clave de un diccionario; un set normal NO puede.
""")

fs = frozenset([1, 2, 3])
print("   ejemplo frozenset:", fs)
# fs.add(4)  -> lanza AttributeError, frozenset no tiene ese metodo

# 2) Demostrar: intersection_update, isdisjoint, issubset, issuperset,
#    pop, remove, symmetric_difference, symmetric_difference_update,
#    union, update
print("2) Otros operadores de conjuntos:")
conj_a = {1, 2, 3, 4}
conj_b = {3, 4, 5, 6}

# intersection_update(): deja en conj_a solo lo que tiene en comun con conj_b
copia_a = conj_a.copy()
copia_a.intersection_update(conj_b)
print("   intersection_update() ->", copia_a)

# isdisjoint(): True si los conjuntos NO comparten ningun elemento
print("   isdisjoint()          ->", conj_a.isdisjoint({10, 11}))

# issubset(): True si todos los elementos del primero estan en el segundo
print("   issubset()            ->", {1, 2}.issubset(conj_a))

# issuperset(): True si conj_a contiene todos los elementos del otro
print("   issuperset()          ->", conj_a.issuperset({1, 2}))

# pop(): elimina y retorna un elemento arbitrario (no se puede elegir cual)
copia_pop = conj_a.copy()
elemento = copia_pop.pop()
print("   pop()                 -> saco:", elemento, "| queda:", copia_pop)

# remove(x): elimina el elemento x; lanza KeyError si no existe
copia_remove = conj_a.copy()
copia_remove.remove(2)
print("   remove(2)             ->", copia_remove)

# symmetric_difference(): elementos que estan en uno u otro, pero no en ambos
print("   symmetric_difference() ->", conj_a.symmetric_difference(conj_b))

# symmetric_difference_update(): igual, pero modifica conj_a directamente
copia_sd = conj_a.copy()
copia_sd.symmetric_difference_update(conj_b)
print("   symmetric_difference_update() ->", copia_sd)

# union(): todos los elementos de ambos conjuntos, sin repetidos
print("   union()               ->", conj_a.union(conj_b))

# update(): agrega a conj_a todos los elementos de conj_b (in-place)
copia_update = conj_a.copy()
copia_update.update(conj_b)
print("   update()              ->", copia_update)