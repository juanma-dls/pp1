""" 
Se ha colocado una nueva cámara de velocidad en una ruta, donde el lıḿ ite de velocidad es de 110 km/h. La cámara detecta la velocidad de cada automóvil que pasa e indica el número de puntos que se deducirán de la licencia de conducir si van demasiado rápido. 
Escriba una función para verificar la velocidad de cada automóvil y determine las deducciones de puntos, si las hubiera. 
Su función debe incluir un argumento (velocidad). 
Utilizar un generador de números aleatorios (enteros positivos con un rango coherente de velocidades para vehículos). 
Los puntos se deducen siguiendo estas condiciones: 
1.- Si el auto está yendo al lıḿ ite de velocidad (110 km/h) o más lento, debe imprimir “Ok” 
2.- Después de eso, por cada 5 km/h por encima del lıḿ ite de velocidad (110 km/h), debe indicar que un punto debe deducirse de la licencia de conducir. 
Por ejemplo, si la velocidad está entre 110 - 115 km/h (mayor a 110 y menor igual a 115), su función debe imprimir: “Puntos a deducir: 1”. 
El siguiente rango sería mayor a 115km/h y menor igual a 120 km/h y así sucesivamente hasta llegar a 6 puntos 
3.- Si se deben deducir 6 o más puntos, la función debe imprimir:”¡Suspender la licencia!” 

"""

import random

def verificarVel(velocidad):
    puntos = 0
    while puntos <= 5:
        velocidad = random.randint(100, 140)
        print("Su velocidad es de: ", velocidad)
        if velocidad <= 110:
            print("Velocidad OK.")
        elif velocidad > 110 and velocidad <= 115:
            print("Puntos a deducir: 1")
            puntos += 1
            print("Puntos acumulados: ", puntos)
        elif velocidad > 115 and velocidad <= 120:
            print("Puntos a deducir: 2")
            puntos += 2
            print("Puntos acumulados: ", puntos)
        elif velocidad > 120 and velocidad <= 125:
            print("Puntos a deducir: 3")
            puntos += 3
            print("Puntos acumulados: ", puntos)
        elif velocidad > 125 and velocidad <= 130:
            print("Puntos a deducir: 4")
            puntos += 4
            print("Puntos acumulados: ", puntos)
        elif velocidad > 130 and velocidad <= 135:
            print("Puntos a deducir: 4")
            puntos += 5
            print("Puntos acumulados: ", puntos)
        elif velocidad > 135:
            print("Puntos a deducir: 6")
            puntos += 6
            print("Puntos acumulados: ", puntos)

        if puntos >= 6:
            print("Se ha exedido el limite de puntos. ¡Suspender la licencia!")

velocidad = 0
verificarVel(velocidad)