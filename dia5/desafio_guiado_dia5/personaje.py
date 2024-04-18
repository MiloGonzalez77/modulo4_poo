#Creación de la clase 'Personaje'
class Personaje:
    #Constructor personaje
    def __init__(self,nombre: str):
        self.nombre = nombre
        self.nivel  = 1
        self.exp    = 0
        
    @property    
    def estado (self):
        return f"\n Nombre personaje : {self.nombre}\n Nivel : {self.nivel}\n Experiencia : {self.exp}\n "
    @estado.setter
    def estado(self, exp_recibida: int):
        exp_valor = self.exp + exp_recibida
    
        #Verificar si la experiencia acumulada supera o iguala los 100 puntos
        if exp_valor >= 100:
        #Calcular cuántos niveles sube el personaje y cuánta experiencia queda
            niveles_subidos = exp_valor // 100
            exp_restante = exp_valor % 100
        
        #Ajustar el nivel y la experiencia acumulada
            self.nivel += niveles_subidos
            self.exp = exp_restante
        
        #Verificar si la experiencia acumulada es negativa
        elif exp_valor < 0:
        #Calcular la nueva experiencia acumulada
            exp_restante = self.exp + exp_recibida
        
            #Verificar si personaje baja de nivel
            if exp_restante < 0:
                #Si nivel es mayor que 1, reducir el nivel en 1
                if self.nivel > 1:
                    self.nivel -= 1
                    self.exp = 100 + exp_restante  
                else:
                    self.exp = 0  
            else:
                self.exp = exp_restante 
        else:
            self.exp = exp_valor
            #Sino, establecer la experiencia acumulada directamente
    
        #Verificar si el nivel es menor que 1 y ajustarlo a 1
        if self.nivel < 1:
            self.nivel = 1
        
    #Metodo especial para comparar si un personaje es mayor que otro (sobrecarga del operador ">")
    def __gt__(self,other):
        return self.nivel > other.nivel
    #Metodo especial para comparar si un personaje es menor que otro (sobrecarga del operador "<")
    def __lt__(self,other):
        return self.nivel < other.nivel
    
    #Metodo que calcula la probabilidad de que el personaje actual gane en una batalla contra otro personaje
    def probabilidad(self, other):
        if self.nivel > other.nivel:
            return 0.66
        elif self.nivel < other.nivel:
            return 0.33
        elif self.nivel == other.nivel:
            return 0.5
    
    #Metodo estático que muestra un diálogo de enfrentamiento al orco
    @staticmethod
    def dialogo_batalla(probabilidad):
        print(f"Tienes una probabilidad de {probabilidad*100} % de ganar")
        print("En caso de ganar, recibiras 50 puntos de experiencia y el orco perdera 30 puntos")
        print("En caso de perder, perderas 30 puntos de experiencia y el orco ganar 50 puntos")