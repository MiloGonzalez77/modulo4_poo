from abc import ABC

#clase padre/abstracta
class Membresia(ABC):
    def __init__(self, correo: str, numero_tarjeta: str):
        """metodo cosntructor de clase mebresia

        Args:
            correo (str): correo de usuario
            numero_tarjeta (str): tarjeta de credito de usuario
        """
        self._correo = correo
        self._numero_tarjeta = numero_tarjeta      
    #metodo cambiar suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in range(1, 5):
            if nueva_membresia == 1:
                return Basica(self._correo, self._numero_tarjeta)
            elif nueva_membresia == 2:
                return Familiar(self._correo, self._numero_tarjeta)
            elif nueva_membresia == 3:
                return SinConexion(self._correo, self._numero_tarjeta)
            elif nueva_membresia == 4:
                return Pro(self._correo, self._numero_tarjeta)
        else:
            return self
        
    #metodo cancelar suscripcion
    def cancelar_suscripcion(self):
        return Gratis(self._correo, self._numero_tarjeta)


class Gratis(Membresia):
    #constructor de clase
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)
        self._costo = 0
        self._max_dispositivos = 1
    #metodo cambio suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        return super().cambiar_suscripcion(nueva_membresia)


class Basica(Membresia):
    #constructor de clase
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)
        self._costo = 3000
        self._max_dispositivos = 2
    #metodo cambio suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        return super().cambiar_suscripcion(nueva_membresia)


class Familiar(Basica):
    #constructor de clase
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)
        self._costo = 5000
        self._max_dispositivos = 5
        self._dias_regalo = 7
    #metodo cambio suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        return super().cambiar_suscripcion(nueva_membresia)
    #Metodo para control parental, sin implementar
    def modificar_control_parental(self):
        pass


class SinConexion(Basica):
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)
        self._costo = 3500
        self._max_dispositivos = 2
        self._dias_regalo = 7
    #metodo cambiar suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        return super().cambiar_suscripcion(nueva_membresia)
    #metodo aumentar contenido, sin implementar
    def aumentar_contenido_sin_conexion(self):
        pass


class Pro(Basica):
    #constructor de atributos
    def __init__(self, correo, numero_tarjeta):
        super().__init__(correo, numero_tarjeta)
        self._costo = 7000
        self._max_dispositivos = 6
        self._dias_regalo = 15
    #metodo cambio suscripcion
    def cambiar_suscripcion(self, nueva_membresia):
        return super().cambiar_suscripcion(nueva_membresia)


g = Gratis("correo@prueba.cl", "13 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
print("-----------")
print("Fin de Programa.")