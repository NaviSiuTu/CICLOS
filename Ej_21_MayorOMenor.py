def MayorMenor(a , b): #Defininición de la función
    return a if a > b else b #Función compacta que compare dos numeros

a = float(input("==== Datos ====\n\033[94mIntroduce un numero: \033"))
b = float(input("\033[93mIntroduce otro numero: \033")) #Interacción del usuario con consola
print (f"\033[0m==== Resultado ====\nEl numero mayor es {MayorMenor(a , b)}\033") #Resultado