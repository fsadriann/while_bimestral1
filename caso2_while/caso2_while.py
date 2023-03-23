# Caso 2 while

c = int(input("Digite el capital: "))

interes = 0
mes = 0
c2 = c + c

while c < c2:
    interes = c*0.05
    c = c+interes
    mes = mes + 1
print("los meses en el que la capital se duplica son " +str(mes)+ " meses")