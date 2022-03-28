"""
La longitud de los lados a y b es de 2 cm, el ángulo    15°
Desarrolle un programa para resolver la figura
Y obtener:
	el resto de las longitudes de los lados
	las medidas de los ángulos
	resultados con dos dígitos decimales

"""

import math

def ptgrs (c1,c2): #Funcion para agilizar pitagoras.
    c3 = round(math.sqrt(c1**2 + c2**2) , 2)
    return c3

a=b=2 #Valore del lado A y B. Dados por la consigna.    

c = ptgrs(a,b) #Calcular lado C mediante pitagoras.

lambd =15 #Valor del angulo Lambda, dado por la consigna.

alfa =180-90+15 #Valor del angulo Alfa, obtenido mediante despeje de los angulos restantes del triangulo.

tanLambd = round(math.tan(math.radians(lambd)),2) #Tangente del angulo Lambda.

i = round(c/tanLambd , 2) #Calculo del lado i mediante T=O/A

j = round(ptgrs(i,c),2) #Despeje del lado C mediante pitagoras.

tetha = (180 - alfa - 45) #Calculo del angulo tetha o tita.

delta = 90-tetha #Calculo del angulo delta.

gamma = (90-delta-lambd) #calculo del angulo gamma.

senDelta = round(math.sin(math.radians(delta)),2) #Calculo SENO del angulo Delta.

h = round(senDelta * j,2) #Calculo lado h mediante S=O/H

g = round(math.sqrt(j**2-h**2),2) #Calculo lago g mediante pitagoras. 

cosGamma=round(math.cos(math.radians(gamma)),2) #Calculo Coseno de Gamma

senGamma=round(math.sin(math.radians(gamma)),2) #Calculo Seno de Gamma

e = round(cosGamma*i,2) #Calculo lado e con coseno de gamma y lado i.

beta = 180-(90+gamma) #Calculo angulo Beta.

d = round(senGamma * i,2) #Calculo lado d con seno de gamma y lado i. 

print (f'''Los valores de los lados son:

    Lado a: {a}cm
    Lado b: {b}cm
    Lado c: {c}cm
    Lado d: {d}cm
    Lado e: {e}cm
    Lado i: {i}cm
    Lado j: {j}cm
    Lado h: {h}cm
    Lado g: {g}cm
    
    ~~~~~~~~~~~~~~~~~~ 

Los valores de los ángulos son: 

    Ángulo ᶐ: {alfa}º
    Ángulo β: {beta}º
    Ángulo ϴ: {tetha}º
    Ángulo ɣ: {gamma}º
    Ángulo λ: {lambd}º ''')
    


#SenA = O/H # CosA = A/H # TanA = O/A