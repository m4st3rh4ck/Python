"""Programa que extrae el nombre de usuario de una cadena usando EXPRESIONES REGULARES"""
import re #Libreria para trabajar con expresiones regulares

def extraccion(cadena): #Funcion para extraer el nombre de usuario
    resultado = re.search(r"\[([a-zA-Z0-9_.]+\]",cadena)
    if resultado is None:
        return ""
    return resultado[1] #Devuelve el nombre de usuario
  #Si hubiera puesto return[0] hubiera devuelto [juan.perez]

#Cadena a manipular
cadena = "INFO 2025-06-04: Usuario [juan.perez] ha iniciado sesión."

print("Cadena sin manipular")
print(cadena)
print("\nCadena manipulada")
print(extraccion(cadena))

