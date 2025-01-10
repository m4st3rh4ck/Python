"""                          Ejercicio
Crea una función llamada es_par que dependa de un parámetro numero. 
Si el número es par, la función debe retornar el valor 1, si no, debe retornar el valor 0. """# Escribe tu código aquí
def es_par(numero):
    if numero % 2 == 0:
        return 1
    else:
        return 0
      
print(es_par(4))
print(es_par(5))
print(es_par(1))
