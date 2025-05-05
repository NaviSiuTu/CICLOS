def convertidorMoneda(x): #Definición de función para convertir una moneda
    TasaConversión = x * 1.13 #Tasa de conversión de la moneda actualmente
    print (f"---- Conversión ----\n{x}€ son ${TasaConversión} dolares") #Impresión de la conversión

x = float(input("---- Datos ----\nDisponga sus euros aquí: ")) #Interacción del usuario con la consola 
convertidorMoneda(x)
  