"""Ejercicio
Crea la función suma que reciba tres parámetros y muestre la suma de estos. 
Si no se le pasa un valor a alguno de los parámetros, este debe tomar el valor por defecto de 0.

Ejemplo:

suma(5, 3) # Es igual a suma(5, 3) # 8
suma(10) # Es igual a suma(10, 0) # 10
suma() # Es igual a suma(0, 0) # 0 """

def suma(num1 = 0, num2 = 0, num3 = 0):
    print(num1 + num2 + num3)

suma(10, 5, 2)
suma(3)
suma(9, 4)
