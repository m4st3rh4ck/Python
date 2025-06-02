#Programa que cambia las extenciones .hpp por c usando for y comprension de listas

lista = ["programa1.c","programa2.hpp","programa3.c","programa4.hpp"]


#Uando for
"""
nueva_lista = []

for nombre in lista:
    if nombre.endswith("hpp"):
        nueva_lista.append(nombre[:-4] + ".c")
    else:
        nueva_lista.append(nombre)
"""

#Usando comprensión de listas
nueva_lista = [nombre[:-4] + ".c" if nombre.endswith(".hpp") else nombre for nombre in lista]

print(lista)
print(nueva_lista)
