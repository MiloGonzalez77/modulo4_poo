from te import Te_artesanal

#Instancias de opciones de preparacion
eleccion1 = Te_artesanal.obt_preparacion_recomendacion(1)
eleccion2 = Te_artesanal.obt_preparacion_recomendacion(3)

#Imprimir tipo de dato
print(type(eleccion1), type(eleccion2))

#Comparacion de similitud
if type(eleccion1) == type(eleccion2):
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
