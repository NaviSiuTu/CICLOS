def AlgoritmoDeEuclides(a , b): #Definición de función

    while b != 0: #Ciclo que se rompe cuando b valga 0
        a, b = b, a % b #Algoritmo de euclides
    return a #Resultado (mcd cuando b valga 0)

a = int(input("\033[35m==== Bienvenido al Algoritmo de Euclides ====\n==== DATOS ====\033[0m\nIntroduce un numero: "))
b = int(input("Introduce el segundo numero: ")) #Interacción del usuario con consola
print (f"\033[35m==== MCD ==== \033[0m\nEl mcd entre {a} y {b} es {AlgoritmoDeEuclides(a , b)}") #Impresión del mcd mediante algoritmo de Euclides