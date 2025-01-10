"""                                                Ejercicio
Marco Polo es un juego de niños que consiste en que un jugador grita "Marco" y los demás jugadores responden "Polo". 
El jugador que grita "Marco" debe tratar de encontrar a los demás jugadores usando solo el sonido de sus voces.

Crea la función marcoPolo que reciba un texto. Si el texto es "Marco" la función debe retornar "Polo". """

def marcoPolo(texto):
    if texto == "Marco":
        return "Polo"
print(marcoPolo('Marco'))
