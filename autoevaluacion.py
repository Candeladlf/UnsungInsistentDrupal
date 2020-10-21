

kilometros = float(input("¿Cuandos kilometros ha recorrido?"))
litros = float(input("¿Cuantos litros ha consumido?"))
print("El consumo ha sido :" +str(100*litros/kilometros)+ " litros cada 100 kms")

print("¿Cuanto IVA vas a pagar (sin porcentaje) ?")
IVA = float(input())
print("¿Cuanto cuesta el producto sin IVA?")
precio = float(input())
print("El precio final es " +str((IVA/100)*precio+precio))


import math
print(round(2 * 3 / math.pi, 2))
print(round(4*3*math.pi/2))
print(abs(0.01 * (-253) * math.pi))
print(round(4*3**2 * math.pi/2))