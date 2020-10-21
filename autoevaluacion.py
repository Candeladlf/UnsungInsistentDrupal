# Autoevalucuacion - Tema 1

# Ejercicio 1
import math
print(round(2 * 3 / math.pi, 2))
print(round(4*3*math.pi/2))
print(abs(0.01 * (-253) * math.pi))
print(round(4*3**2 * math.pi/2))

# Ejercicio 2
lado1 = float(input("introduce lado 1 rectángulo : "))
lado2 = float(input("introduce lado 2 rectángulo : "))
print("El perímetro del rectángulo es : " +str(2*lado1 + 2*lado2)+ " metros")
print("El área del rectángulo es : " +str(lado1*lado2)+ " m2")
print("\n")

# Ejercicio 3
base = float(input("introduce base triangulo : "))
altura = float(input("introduce altura triangulo : "))
print("El área del triangulo es " +str(base*altura/2)+ " m2")
print("\n")

# Ejercicio 4
d = float(input("Introduce diametro del circulo : "))
print("El longitud del circulo es de " +str(round(d*math.pi, 2))+ " metros")
print("El área del circulo es " +str(round(math.pi * (d/2)**2, 2))+ " m2")
print("\n")

# Ejercicio 5
valor=float(input("Introduce un valor con dos decimales: "))
print("la raiz cuadrada es: " +str(round(math.sqrt(valor),2)))
print("\n")