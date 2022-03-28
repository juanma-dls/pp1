"""
Estás organizando una fiesta para tus amigos y necesitás calcular cuánto vino comprar. Una caja de vino contiene 6 botellas, cada botella contiene 0,75 litros. Una medida estándar de vino es 0.175 litros. Debés invitar a 20 personas a la fiesta
Prepara las constantes y variables para llevar a cabo el cálculo
Responde luego las siguientes preguntas:
    a.	¿Cuántos vasos llenos de vino obtienes por botella?
    b.	¿Cuánto vino queda en cada botella, considerando que no podes llenar copas de vino de distintas botellas?
    c.	Todos han confirmado su asistencia, ¿cuántas personas estarán en la fiesta?
    d.	3 personas no toman alcohol, ahora ¿cuántas personas tenés que considerar?
    e.	Si todas las personas toman 4 copas de vino y solo considera copas llenas. 
        I.	¿Cuántas cajas de vino necesitará? ¿Cuántas botellas de vino necesitara?
        II.	Y si considera las cantidades totales de vino ¿Cuántas cajas de vino necesitará? ¿Cuántas botellas de vino necesitara?
"""

caja = 6
botella = 0.75
medida = 0.175

invitados = int(input("Ingrese el numero de invitados:")) 

vasosLLenos = round(botella/medida)
print(f"a. Se pueden llenar {vasosLLenos} vasos llenos por botella")

vinoVasos = medida * vasosLLenos
restoBotella = round(botella - vinoVasos,2)
print(f"b. En cada botella queda aproximadamente {restoBotella} ml de vino")

presentes = invitados + 1 #se le suma 1 porque son los 20 invitados mas el anfitrion
print(f"c. La cantidad de presentes en la fiesta es de {presentes} personas")

tomanAlcohol = presentes - 3
print(f"d. Si 3 personas no toman alcohol solo se deben considerar {tomanAlcohol} personas")

botellasNec = presentes
cajasNec = botellasNec/caja
totalBotellas = cajasNec * caja
print(f"e. I. Se necesitarán {cajasNec} cajas, es decir que tendremos {totalBotellas} botellas de vino pero solo se utilizarán {botellasNec}")

sobrante = restoBotella*botellasNec
botellasSobrantes = round(sobrante/botella)
botellasReales = botellasNec - botellasSobrantes
cajasReales = round(botellasReales/caja)
print(f"e. II. Si se consideran las cantidades totales de vino necesitariamos {cajasReales}, pero solo usariamos {botellasReales} botellas ")