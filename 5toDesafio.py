"""
Desarrollar un programa que pida colocar una frase hasta que no se coloque nada
i.	Determine si la frase ingresada por teclado contiene mayúsculas. 
ii.	Si es así entonces el programa debe indicar  en qué posición hay una mayúscula,
iii.Si la frase no presenta mayúsculas entonces el programa deberá mostrar un mensaje mencionando  que la frase no contiene mayúsculas, previo a querer buscar la posición de las mayúsculas. El programa no debe mencionar que la frase presenta 0 mayúsculas

"""

frase = " "

while frase != "":
    frase = input("Ingrese una frase: ")
    mayusc = 0

    for i in frase:
        if i.isupper():
            mayusc = mayusc + 1
    
    if mayusc != 0:
        print(f"La frase tiene {mayusc} mayusculas")
        for i in range(len(frase)):
            if frase[i] != " " and frase[i] == frase[i].upper():
                print(f"Hay una mayuscula en la posicion {i}")
    elif frase == "":
        print("No se ingreso ninguna frase")
    else:
        print("La frase ingresada no tiene mayusculas")