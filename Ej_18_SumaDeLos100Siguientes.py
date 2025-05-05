def suma(): #Definición de la función
    numero = int(input("Bienvenido a esta calculadora\n----- DATOS -----\nIntroduce un número: ")) #Interacción del usuario con la consola
    resultado = 0 #Contador de inicio
    for x in range(numero , numero + 101): #Rango de el numero consultado (100 numeros siguientes al numero consultado)
        resultado += x

    print(f"---- Resultado ----\nEl resultado de la suma es {resultado}") #Impresión del resultado

suma()