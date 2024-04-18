#HERENCIA SIMPLE -> un clase que hereda atributos/metodos desde una sola clase
########################################################
class Padre():
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self) -> str:
        return self.__color

    def imprimir(self):
        print("este metodo pertenece a la clase padre") 

########################################################
class Hija(Padre):
    def mostrar_color(self):
        print(f"Mi color es {self.color}")
    def imprimir1(self):
        print("este metodo pertenece a la clase Hija")
########################################################
class Nieta(Hija):
    def imprimir2(self):
        print("este metodo pertenece a la clase Nieta")

########################################################
papa = Padre("Azul y Blanco")
print(papa.color)
pdf = Hija("Blanco y Negro")

# Salida: Mi color es Blanco y Negro
pdf.mostrar_color()

papa = Padre("Azul y Blanco")
print(papa.color)

#papa.mostrar_color() --> no funciona, ya que la clase padre no hereda el metodo de la hija.
hijita = Hija("Blanco y Negro")
# Salida: Mi color es Blanco y Negro
hijita.mostrar_color()
print(hijita.color)
hijita.imprimir()
print("--------------------------------")

#Googlear metodo: Super()

nietita = Nieta("Verde")
nietita.imprimir()#

print(isinstance(nietita,Hija),isinstance(hijita,Padre), isinstance(nietita,Padre),isinstance(hijita,Nieta))
#True True True False