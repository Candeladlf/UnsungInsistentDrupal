
lado1 = float(input("introduce lado 1 rectángulo : "))
lado2 = float(input("introduce lado 2 rectángulo : "))

print("El perímetro del rectángulo es : " +str(2*lado1 + 2*lado2)+ " metros")
print("El área del rectángulo es : " +str(lado1*lado2)+ " m2")
print("\n")

base = float(input("introduce base triangulo : "))
altura = float(input("introduce altura triangulo : "))

print("El área del triangulo es " +str(base*altura/2)+ " m2")
print("\n")

import math
d = float(input("Introduce diametro del circulo : "))

print("El longitud del circulo es de " +str(round(d*math.pi, 2))+ " metros")
print("El área del circulo es " +str(round(math.pi * (d/2)**2, 2))+ " m2")
print("\n")

valor=float(input("Introduce un valor con dos decimales: "))
print("la raiz cuadrada es: " +str(round(math.sqrt(valor),2)))
print("\n")