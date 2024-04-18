from dia7.chocolate.sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    @abstractmethod
    def validar_porc_cacao(self, porc: float) -> float:
        pass
    
    def __init__(self, porc_cacao: float):
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)
        
class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc: float):
        return min(max(0.75, porc), 0.85)

class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass

#Argumentos de  ejecucion del programa:
c = ChocolateAmargo(0.3)
# Salida: 0.75
print(c.porc_cacao)
