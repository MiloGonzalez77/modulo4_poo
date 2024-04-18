#Creacion clase Producto
class Producto:
    #Constructor de la clase
    def __init__(self, nombre, precio, stock=0):
        """Constructor

        Args:
            nombre (String): nombre de producto
            precio (Int): precio de producto
            stock (int, optional): si no se especifica por default será 0
        """
        
        #Inicializacion atributos
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = (stock if stock > 0 else 0)

    #Metodos getter para los atributos encapsulados
    @property  
    def nombre(self):
        return self.__nombre  
    @property
    def precio(self):
        return self.__precio
    @property
    def stock(self):
        return self.__stock

    #Metodos setter para los atributos
    @stock.setter
    def stock(self, stock):
        self.__stock = (
            stock if stock > 0 else 0
        )  
    def __add__(self, other):
        return (
            self.stock + other.stock
        )
    
    #Metodo para actualizar stock 
    def __sub__(self, other):
        return (
            self.stock - other.stock
        )

    #Metodo para comparar nombres de productos
    def __eq__(self, other):
        return (
            self.nombre == other.nombre
        ) #resultado boleano.
