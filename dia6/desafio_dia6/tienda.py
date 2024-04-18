from abc import ABC, abstractmethod
from producto import Producto


#Clase Tienda como clase hija de la clase abstracta abc
class Tienda(ABC):
    #Metodos abstractos:
    @abstractmethod
    def ingresar_producto(self, nombre, precio, stock):
        """ingresar producto

        Args:
            nombre (str): nombre del producto
            precio (int): precio del producto
            stock (str): cantidad del producto
        """
        pass
    @abstractmethod
    def listar_productos(self):
        pass
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        """metodo venta

        Args:
            nombre_producto (str): nombre del producto a vender
            cantidad (int): cantidad del producto a vender
        """
        pass

#Clase TiendaRestaurante como clase hija de Tienda
class Restaurante(Tienda):
    tipo = "Restaurante"
    #Constructor
    def __init__(self, nombre, costo_delivery):
        #Inicializar atributos
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    #Metodo ingreso de producto en Tienda Restaurante
    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio)
        #Filtro de busqueda
        encontrados = list(filter(lambda x: x == p, self.__productos))
        #Append en caso de no estar listado
        if len(encontrados) == 0:
            self.__productos.append(p)

    #Listar productos:
    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            for p in self.__productos:
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio} \n"
            return retorno
        else:
            return "No hay stock de productos"

    #Metodo ventas sin implementar
    def realizar_venta(self, nombre_producto, cantidad):
        pass


#Clase TiendaFarmacia como clase hija de Tienda
class Farmacia(Tienda):
    tipo = "Farmacia"
    #Constructor de atributos
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    #Metodo ingresar producto
    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)
        #Filtrado de comprobacion
        encontrados = list(filter(lambda x: x == p, self.__productos))
        #Agregar en caso de no estar
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    #Metodo listar productos farmacia
    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            #Iteracion
            for p in self.__productos:
                m = ""
                if p.precio > 15000:
                    m = " (Producto con Delivery sin costo)"
                retorno += f"NOMBRE: {p.nombre}\t" + f"PRECIO: ${p.precio}{m}\n"
            return retorno
        else:
            return "No hay stock de productos"

    #Metodo para venta sin implementar
    def realizar_venta(self, nombre_producto, cantidad):
        pass


#Clase TiendaSupermercado como clase hija de Tienda
class Supermercado(Tienda):
    tipo = "Supermercado"
    #Constructor de atributos
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    #Metodo ingreso de productos
    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)
        #Filtrado de comprobacion
        encontrados = list(filter(lambda x: x == p, self.__productos))
        #Agregar en caso de no estar
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            #Actualizar stok
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    #Metodo listar productos supermercado
    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            #Iteracion
            for p in self.__productos:
                m = ""
                if p.stock < 10:
                    m = " (Producto con stock bajo)"
                retorno += (
                    f"NOMBRE: {p.nombre}\t"
                    + f"PRECIO: ${p.precio}\t"
                    + f"STOCK: {p.stock}{m}\n"
                )
            return retorno
        else:
            return "No hay stock de productos"
    
    #Metodo ventas sin implementar
    def realizar_venta(self, nombre_producto, cantidad):
        pass
    