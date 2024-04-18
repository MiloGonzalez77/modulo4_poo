from medicamento import Medicamento
import time

opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
ingresados = []


while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)

    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
    
    precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
    m.precio = precio_bruto 

    print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    print(f"STOCK: {m.stock}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
        print(f"PRECIO FINAL: ${m.precio_final}")
        
    
    print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    for med_ingresado in ingresados:
        print(med_ingresado)
        print("")

    time.sleep(3)
    opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
