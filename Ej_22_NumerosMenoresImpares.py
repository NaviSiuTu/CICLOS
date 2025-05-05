def NumerosiMenores(numero): #Definición de función
    for resultado in range (numero - 101 , numero): #Rango de los numeros (se pone primero el negativo ya que si no lo hacemos nos aparecerá "none")
        if resultado % 2 != 0: #Definimos el módulo para definir que lo que queremos definir son numeros impares
            print (resultado) 
    
numero = int(input("==== Bienvenido al la impresora de numeros ====\nIntroduce un numero: "))#Interacción con la consola
NumerosiMenores(numero) #Impresión de los resultados (numeros impares)

#Cabe destacar que definimos un rango, ya que si no sería una operación infinita, por tanto es importante definir un rango
#En este caso el rango son los 100 numeros anteriores a el numero typeado (contando tambien los pares)