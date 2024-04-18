
from pizza import Pizza
import ingredientes 


#Obtener los valores de atributos de clase
tamanio, precio = Pizza.tamanio, Pizza.precio
print(f"El tamaño de la pizza es: {tamanio} y su precio es: ${precio}")

#Validar un ingrediente usando el metodo Pizza.validar()
texto = 'Salsa de tomate'
lista = ['Salsa de tomate', 'Salsa BBQ']
test = Pizza.validar(texto, lista)
if test:
    print(f"El ingrediente {texto}, está disponible.")
    print("---------------------------")
else:
    print("Lo sentimos, ingrediente no disponible")


#Instancia de clase pizza para realizar pedido
realizar_pedido = Pizza()
realizar_pedido.pedido()

#Imprimir resumen de pedido
print(f'''
Resumen de Pedido en su Pizza:
Carne/Proteina: {realizar_pedido.proteina}
Vegetales: {realizar_pedido.vegetal_1} y {realizar_pedido.vegetal_2}
Tipo de masa: {realizar_pedido.masa}
''')

#Verificar pedido
if realizar_pedido.es_valido:
    print("Su pedido es válido. Su pizza estará lista en seguida.")
    print("####### FIN DE PROGRAMA #######")
else:
    print("Su pedido no es válido! \nIntente nuevamente.")
    print("####### FIN DE PROGRAMA #######")
