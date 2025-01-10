"""                               Ejercicio
Crea una función que se llame adivinaNumero y que dependa de un parámetro numero.

Si el número es 7, la función debe retornar "Adivinaste el número secreto".

Si el número es 6, la función debe retornar "Casi, pero no es el número secreto".

Cualquier otro número debe retornar "Estás equivocado, el número secreto no es " 
seguido del número que se ingresó. Por ejemplo: Si el número ingresado es 8, la función debe retornar 
"Estás equivocado, el número secreto no es 8". """

def adivinaNumero(numero):
    if numero == 7:
        return "Adivinaste el número secreto"
    elif numero == 6:
        return "Casi, pero no es el número secreto"
    else:
        return "Estás equivocado, el número secreto no es " + str(numero)
      
print(adivinaNumero(7))
print(adivinaNumero(8))
print(adivinaNumero(6))
