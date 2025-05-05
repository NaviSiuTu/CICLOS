
def cuadrática(a , b , c): #Definimos la función 
    discriminante = b**2 - 4*a*c #Con el discriminante podemos hayar si una ecuación cuadrática tiene solución o no en los numeros reales
    raizDiscriminante = discriminante ** 0.5
    if discriminante < 0: #Condicional si no hay solución
        print ("==== Resultados ====\033[31mNo hay solución en los números reales\033[0m")
    else: 
        x1 = (-b + raizDiscriminante) / (2 * a) #Ecuación cuadrática
        x2 = (-b - raizDiscriminante) / (2 * a)
        print (f"==== Resultados ====\nLos valores de x para esta cuadrática son \033[35m\nx1= {x1}\nx2= {x2}\033[0m\nEnhorabuena")

a = float(input("Introduce el valor del coeficiente a: ")) #Interacción del usuario con la consola
b = float(input("Introduce el valor del coeficiente b: "))
c = float(input("Introduce el valor del coeficiente c: "))
cuadrática(a , b , c)
