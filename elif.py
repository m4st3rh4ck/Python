"""                                    Ejercicio
Utilizando lo aprendido en ejercicios anteriores, crea una función llamada obtener_dia que 
permita obtener el nombre correspondiente al día de la semana a partir del parámetro día. 
El valor pasado será un número del 0 al 6 que representa el día de la semana. 
Si el día es 0, la función debe retornar "Domingo". Si el día es 1, la función debe retornar "Lunes", 
y así sucesivamente hasta el día 6 que corresponde a "Sábado". Si el día es cualquier otro valor, 
la función debe retornar "Valor inválido". """

 def obtener_dia(dia):
    if dia == 0:
        return "Domingo"
    elif dia == 1:
        return "Lunes"
    elif dia == 2:
        return "Martes"
    elif dia == 3:
        return "Miercoles"
    elif dia == 4:
        return "Jueves"
    elif dia == 5:
        return "Viernes"
    elif dia == 6:
        return "Sabado"
    else:
        return "Valor inválido"

print(obtener_dia(1))
print(obtener_dia(2))
print(obtener_dia(6))
print(obtener_dia(9))
