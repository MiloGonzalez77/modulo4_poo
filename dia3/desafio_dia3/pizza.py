from ingredientes import proteinas, vegetales, masa

#Clase Pizza
class Pizza():
    #atributos/variabnles ya establecidos:
    tamanio = "Familiar"
    precio = 10000
    
    #Validar elemento en la lista
    @staticmethod
    def validar(texto , lista):
        return texto in lista
    
    #Constructor
    def __init__(self):
        # Atributos de instancia
        self.proteina = ()
        self.vegetal_1 = ()
        self.vegetal_2 = ()
        self.masa = ()
        self.es_valido = False
    
    #Realizar el pedido
    def pedido(self):
        #Solicitar ingreso de ingredientes
        print('Escriba cual carne/proteina desea en la pizza: ')
        print('Las opciones son: \n[Pollo], [Vacuno] o [Carne Vegetal] \n')
        self.proteina = input('Carne/Proteina: ').lower()
        print("")
        print('Escriba el vegetal que desea en la pizza: ')
        print('Las opciones son: \n[Tomate], [Aceitunas] o [Champiñones] \n')
        self.vegetal_1 = input('Primer vegetal: ').lower()
        print("")
        self.vegetal_2 = input('Segundo vegetal: ').lower()
        print("")
        print('Escriba el tipo de masa base que desea en la pizza: ')
        print('Las opciones son: \n[Tradicional] o [Delgada] \n')
        self.masa = input('Masa: ').lower()
        print("")
        
        #Verificar ingredientes
        self.es_valido = (
            self.validar(self.proteina, proteinas) and
            self.validar(self.vegetal_1, vegetales) and
            self.validar(self.vegetal_2, vegetales) and
            self.validar(self.masa, masa)
        )
        
if __name__ == "__main__":
    pizza1 = Pizza()
    pizza1.pedido()
    if pizza1.es_valido:
        print('Pizza ingresada y solicitada correctamente')
    else:
        print('Error: La pizza no es valida')
