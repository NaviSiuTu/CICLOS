def AreaRectangulo(b , h): #Definición de función
    return b * h #Una forma mas compacta de definir el cuerpo de la función

b = float(input("Bienvenido al calculador de area y altura\n==== Datos ====\n\033[92mIntroduce la medida de la base (en metros): "))
h = float(input("Introduce la medida de la altura (en metros): \033[0m")) #Interacciones del usuario con la consola
print (f"==== Resultado ====\n\033[94mEl area del rectángulo será {AreaRectangulo(b , h)} metros cuadrados \033[0m")

#Descrubri que puedes poner colores a las partes de la ejecución!!, tan solo basta con poner \033[92m (por ejemplo para el verde)
#Tambien es importante decirle hasta donde poner el color y se hace colocando \033 [0m (para que el texto que siga sea blanco) cuando querramos que se acabe