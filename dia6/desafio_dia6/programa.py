from tienda import Tienda, Restaurante, Farmacia, Supermercado
from producto import Producto

#Creacion de tienda:
nombre = input("\nEscriba un nombre al comercio: \n")
precio_delivery = int(input("\nIngrese el precio del servicio de delivery: \n"))
while precio_delivery < 0 and precio_delivery > 20000:
    precio_delivery = int(input("Dato incorrecto ingrese un valo válido \n"))

#Solicitar al usuario el comercio al que quiere entrar
while True:
    tipo = int(
        input(
            "Por favor, ingrese la [Opcion] de tienda que desea ingresar:\n"
            "[1] Restaurante \n[2] Supermercado \n[3] Farmacia \n"
        ))
    if tipo == 1 or tipo == 2 or tipo == 3:
        break
    else:
        print("Opcion invalida. Intenta nuevamente.")
    

#Asignar instancia segun tipo de tienda
if tipo == 1:
    tienda = Restaurante(nombre, precio_delivery)
if tipo == 2:
    tienda = Supermercado(nombre, precio_delivery)
elif tipo == 3:
    tienda = Farmacia(nombre, precio_delivery)


opcion = 1

#Agregar producto a tienda
while True:
    opcion = int(input("¿Desea agregar otro producto?\n [1]Sí __ [2]No\n"))
    
    if opcion == 1:
        print("")
        nombre_producto = input("Ingrese el nombre del producto que desea agregar: \n")
    
        print("")
        precio = int(input("Ingrese el precio del producto: \n"))
    
        print("")
        stock = int(input("Ingrese el stock del producto: \n"))
    
        print("")
        tienda.ingresar_producto(nombre_producto, precio, stock)
        print("-----------")
    
    if opcion == 2:
            break
    else:
        opcion = print("Opcion no valida")

#Menu de opciones para interactuar con los productos de la tienda
while True:
    opcion_productos = int(
        input(
        "Que desea hacer, escriba el numero de [opcion] \n"
        "[1] Listar productos disponibles en la tienda \n"
        "[2] Realizar una venta de producto \n"
        "[3] Salir \n")
    )
    if opcion_productos == 1:
        #Mostrar lista
        print(tienda.listar_productos())
    elif opcion_productos == 2:
        #Realizar venta
        nombre_producto = input("\nIngrese el nombre del producto que desea vender:\n")
        cantidad = int(input("\nIngrese la cantidad que desea comprar:\n"))
        tienda.realizar_venta(nombre_producto, cantidad)
    elif opcion_productos == 3:
        print("Fin de programa")
        break
    else:
        print("Opcion no valida, intenta nuevamnte.")
