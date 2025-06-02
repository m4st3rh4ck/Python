"""Programa que cambi los archivos con extencion .txt a .py"""

#Lista a modificar
lista = ["programa1.txt","programa2.txt","programa2.py","programa3.py"]

#Lista donde se guardaran los elementos modificados
nueva_lista = []

#Con un for, recorro todos los elementos de la lista a modificar
for elemento in lista:
    #Si se encunetra un elemento con txt...
    if elemento.endswith(".txt"):
        #Entonces se borran los ultimos 4 elementos y en su lugar se agrega py
        nueva_lista.append(elemento[:-4] + ".py")
        #Si no, los elementos se dejan igual
    else:
        nueva_lista.append(elemento)
        
#Se imprime la lista a modificar
print(lista)

#Se imprime la lista modificada
print(nueva_lista)
