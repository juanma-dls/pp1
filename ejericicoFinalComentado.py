# Ordenando cadena de numeros

print("Ingrese una cadena de numeros: ", end="")

numeros = list(map(int, input().split()))
print(numeros)

numeros.sort()

print(numeros)


#ordenando array ingresado por teclado con condiciones


def ordenarArray(arr):
    ordenado = False
    #mientras oodenado sea false vuelve a revisar el array
    while ordenado == False:
        ordenado = True
        #Colocamos -1 porque la comparacion que va a hacer lo hace con el de la derecha hasta el penultimo
        #Con len nos dara el tamaño y el rango numerico va a ser de 0 al tamaño maximo 
        for i in range(len(arr)-1):
            #Comparamos el valor de con el de la derecha incrementado i +1
            if arr[i] > arr[i + 1]:
                #Guardamos el valor de i en una variable
                aux = arr[i]
                #El valor de i va a valer el valor del elemento que estamos iterando a la derecha
                arr[i] = arr[i + 1]
                #El valor de la derecha que estamos iterando va a valer auxiliar
                #aux es el elemento original sobre el que estaba iterando y es mayor al de la derecha
                arr[i + 1] = aux
                #colocamos la variable ordenado con valor false para cada vez que sea falso entre al if porque esta desordenado
                ordenado = False


#Con la funcion list convertimos la lista en una lista iterable
#LLamamos la funcion map para que cree un mapeo, donde todos los datos del input los convirtamos en enteros
#Con la funcion .split() la cual separa los numeros por espacio
#Nos queda una lista de cadena de caracteres con cada uno de los n que digito el usuario. Ese objeto iterable que representan
# los numeros se van a convertir en enteros gracias a la funcion map y luego ese mapa que se crea se convierte a una lista iterable
arr = list(map(int, input("Por favor ingrese los numeros a ordenar: ").split()))
ordenarArray(arr)
print(arr)
