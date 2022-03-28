"""
En un país se utilizan diferentes tasas impositivas según el sueldo bruto anual del contribuyente. 
Los contribuyentes casados suman sus ingresos y pagan impuestos sobre el total.
a.	Diseñe un programa que calcule el impuesto a pagar teniendo en cuenta las siguientes entradas: soltero/a o casado/a, si es casado/a debe indicar dos sueldos, si es soltero/a uno.
b.	El código debe indicar en cual categoría esta el contribuyente, el impuesto que deberá pagar y cuál es el sueldo mensual
c.	Analícelo detenidamente, hay varias formas de resolverlo, puede llegar a resolverlo con 25 líneas de código. Recuerde que la solución además de contener poco código debe ser también también apreciable

"""
print("¿Usted es casado?")
estCivil = input("Ingrese si o no: ")

if estCivil.lower() == "no":
    sueldo = float(input("Por favor declare su sueldo:"))
elif estCivil.lower() =="si":
    sueldo = float(input("Por favor declare el primer sueldo:")) + int(input("Por favor declare el segundo sueldo:"))

if sueldo <= 300000.00 :
    print(f"Su sueldo total es de {sueldo}, por ende pertence a la categoria A, su tasa impositiva es del 3% = {sueldo*0.03}")
elif sueldo > 300000.00 and sueldo <= 450000.00:
    print(f"Su sueldo total es de {sueldo}, por ende pertence a la categoria B, su tasa impositiva es del 8% = {sueldo*0.08}")
elif sueldo > 450000.00 and sueldo <= 700000.00:
    print(f"Su sueldo total es de {sueldo}, por ende pertence a la categoria C, su tasa impositiva es del 13% = {sueldo*0.13}")
elif sueldo > 700000.00 and sueldo <= 1200000.00:
    print(f"Su sueldo total es de {sueldo}, por ende pertence a la categoria D, su tasa impositiva es del 20% = {sueldo*0.20}")
elif sueldo > 1200000.00:
    print(f"Su sueldo total es de {sueldo}, por ende pertence a la categoria E, su tasa impositiva es del 35% = {sueldo*0.35}")

print(f"Su  sueldo mensual es de {sueldo/12}")