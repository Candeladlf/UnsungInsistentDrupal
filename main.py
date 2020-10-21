# Actividad 2 - Ejercicio 3
kilometros = float(input("¿Cuandos kilometros ha recorrido? "))
litros = float(input("¿Cuantos litros ha consumido? "))
print(f"El consumo ha sido : {round(100*litros/kilometros,2)}  litros cada 100 kms")
# Actividad 2 - Ejercicio 4
IVA = float(input("¿Cuanto IVA vas a pagar (sin porcentaje) ? "))
precio = float(input("¿Cuanto IVA vas a pagar (sin porcentaje) ? "))
print("El precio final es " +str((IVA/100)*precio+precio))