from pizzas import Pizzas

#a
print(Pizzas.tamanio, Pizzas.precio)

#b
print(Pizzas.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))

#c
pizza = Pizzas()
pizza.realizar_pedido()

#d
print(pizza.vegetales,pizza.proteicos,pizza.masas)
print(pizza.pizza_valida)

#e
#print(Pizzas.pizza_valida)
#AttributeError: type object 'Pizzas' has no attribute 'pizza_valida'