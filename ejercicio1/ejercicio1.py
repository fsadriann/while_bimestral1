# While-Bucle

import math

n = int(input("Digite un número: "))

while n<0:
    print("Error -> Debería ser un número positivo")
    n = int(input("Digite un número: "))

print(f"\nla raíz cuadrada es: {(math.sqrt(n)):.2f}")