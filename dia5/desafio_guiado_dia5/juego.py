from personaje import Personaje
import random

print("¡¡Bienvenido valiente jugador, a Gran Fantasía!! \n")
nombre = str(input("Ingresa un nombre para su personaje: \n"))

#Instancia de personaje
p_jugador = Personaje(nombre)

#mostar estado
print(p_jugador.estado)

# Crear una instancia de la clase 'CrearPersonaje' para crear el personaje orco
p_orco = Personaje("Orco")

probabilidad = p_jugador.probabilidad(p_orco)
#Mensaje de aparición del orco
print("¡CUIDADO! HA APARECIDO UN [ORCO]\n")
p_jugador.dialogo_batalla(probabilidad)
#Decision
print("¿Deseas Atacar o Huir?")
opcion=int(input("Ingresar 1 para Atacar o 2 para huir : "))

#Buce de combate
while opcion == 1:
    
    num_aleatorio= round(random.uniform(0, 1), 2)
    
    #revision de RNG o generacion de numero aleatorio
    if num_aleatorio <= probabilidad:
        print("------------------------------------")
        print("\nVenciste al orco, felicidades")
        #Información al jugador de la recompensa
        print(f"{p_jugador.nombre} a ganado 50 puntos de experiencia\n")
        p_jugador.estado = 50
        p_orco.estado = -30
    else:
        print("------------------------------------")
        print("\n\n¡Oh no! ¡El orco te ha ganado!")    
        print(f"{p_jugador.nombre} a perdido 30 puntos de experiencia\n")
        p_jugador.estado = -30
        p_orco.estado = 50
    
    print(f"Estado actual de personajes :")
    print(p_jugador.estado)
    print(p_orco.estado)
    print("------------------------------------")
    probabilidad = p_jugador.probabilidad(p_orco)
    p_jugador.dialogo_batalla(probabilidad)
    print("¿Deseas Atacar o Huir?")
    opcion=int(input("Ingresar 1 para Atacar o 2 para huir : \n"))