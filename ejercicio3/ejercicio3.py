#Ejemplo de un menú

n = int(input("Menú: 1(Ver números), 0(salir) "))
while n !=0:
    x = 0

    while x<10:
        print("el valor de x es: ",x)
        x += 1

    print("Saliendo,,,")
    n = int(input("Menú: 1(Ver números), 0(Salir) "))

print("Gracias")