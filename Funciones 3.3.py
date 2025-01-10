"""                                                 Ejercicio
Crea la función sumar_y_duplicar que dependa de dos parámetros, a y b, y que devuelva la suma de ambos multiplicada por 2. 
Adicionalmente, antes de retornar el valor, la función debe mostrar el valor de la suma de la siguiente forma: "La suma es X", 
donde X es el resultado de la suma.

Ejemplo: sumar_y_duplicar(2, 2) # La suma es 4 sumar_y_duplicar(3, 3) # La suma es 6 """

def sumar_y_duplicar(a, b):
    suma = a + b
    print("La suma es ",suma)
    return suma * 2

print(sumar_y_duplicar(2, 2)) 
print(sumar_y_duplicar(3, 3)) 
