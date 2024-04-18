from ingredientes import vegetales, proteicos, masas
#import ingredientes

class Pizzas:
    #atributos
    vegetales = ["tomate","champiñon","aceitunas"]
    proteicos = ["pollo","vacuno","carne vegetal"]
    masas = ["tradicional","delgada"]
    precio = 10000
    tamanio = "familiar"

    @staticmethod
    def validar_elemento(elemento, posibles_valores):
        return elemento.lower() in posibles_valores

    def realizar_pedido(self):
        self.proteicos = input("""
            Ingrese el ingrediente proteico
            las opciones son:\n
            Pollo\nVacuno\nCarne Vegetal 
            """)
        val_pro =self.validar_elemento(self.proteicos, proteicos )

        self.vegetales = []
        vegetal1 = input(""" Ingrese el primer ingrediente vegetal
            las opciones son:\n
            Tomate,\nChampiñon,\nAceitunas 
            """)
        self.vegetales.append(vegetal1)

        val_veg1 = self.validar_elemento(vegetal1,vegetales)
        
        self.vegetales.append(input(""" Ingrese el segundo ingrediente vegetal
            las opciones son:\n
            Tomate,\nChampiñon,\nAceitunas
            """))
        
        val_veg2 = self.validar_elemento(self.vegetales[1],vegetales)

        self.masas = input("""Ingrese la masa a utilizar
            las opciones son:\n
            Tradicional\nDelgada
        """)
        #val_masa = self.validar_elemento(self.masas,masas)

        #validacion de pizza     
        self.pizza_valida = val_pro and val_veg1 and val_veg2 and self.validar_elemento(self.masas,masas)

if __name__ == "__main__":
    pizza1 = Pizzas()
    pizza1.realizar_pedido()
    if pizza1.pizza_valida:
        print("La Pizza es valida")
    else:
        print("La Pizza no es valida")
