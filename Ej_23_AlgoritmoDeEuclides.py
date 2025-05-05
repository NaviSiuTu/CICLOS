def AlgoritmoDeEuclides(a , b): #Definición de función

    while b != 0: #Ciclo que se rompe cuando b valga 0
        a, b = b, a % b #Algoritmo de euclides
    return a #Resultado (mcd cuando b valga 0)

a = int(input("Bienvenido al Algoritmo de Euclides\nIntroduce un numero: "))
b = int(input("Introduce el segundo numero: ")) #Interacción del usuario con consola
print (f"El mcd entre {a} y {b} es {AlgoritmoDeEuclides(a , b)}") #Impresión del mcd mediante algoritmo de Euclides