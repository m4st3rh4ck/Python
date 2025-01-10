"""Ejercicio
Se ha definido una función llamada mostrar_mensaje_secreto. 
Esta función depende de un parámetro llamado mensaje. 
Si el mensaje es "secreto", mostrará "Mensaje correcto". 
Sin embargo, si el mensaje es cualquier otro, la función finalizará, mostrando "Término de la función".

Para resolver el ejercicio debes llamar a la función dos veces, 
primero, con el mensaje "secreto" y luego con el mensaje "no secreto" 
para verificar que funciona correctamente."""

def mostrar_mensaje_secreto(mensaje):
    if mensaje == "secreto":
        print("Mensaje correcto")
    else:
        print("Término la funcion")

mostrar_mensaje_secreto("secreto")
mostrar_mensaje_secreto("no secreto")
