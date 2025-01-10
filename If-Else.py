"""                            Ejercicio
Crea una función llamada es_correcto que dependa de un parámetro codigo. 
Si el código es igual a "1234", la función debe retornar el valor 1, si no, debe retornar el valor 0. """

def es_correcto(codigo):
    if codigo == "1234":
        return 1
    else:
        return 0

print(es_correcto("1234"))
print(es_correcto("3465646"))
