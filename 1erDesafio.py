## Cadenas, Operadores matemáticos, Sentencias de Control Condicionales y Repetitivas, Funciones y Listas ##

""" Dada la variable python, nombredelestudiante = “Este es el trabajo de: apellido, nombre”
Escriba un programa para editar la variable, de modo que contenga su nombre, en el formato ‘apellido, nombre’
Utilice las funciones para la modificación de cadenas de caracteres provistas por Python. 
A continuación debe imprimir la variable.
Ejemplo: “Este es el trabajo de: Juan Perez” """ 


nombredelestudiante = "Este es el trabajo de: apellido, nombre"

nombre = input("Por favor ingrese su Apellido: ")
apellido = input("Por favor ingrese su Nombre: ")
nombreModificacdo = nombredelestudiante.replace("apellido, nombre" , apellido + ", " + nombre)
print(nombreModificacdo)







