#Creacion clase Te_artesanal
class Te_artesanal():
    #caducidad del te
    duracion = "365 días o 1 año"
        
    #metodo preparacion del te
    @staticmethod
    def obt_preparacion_recomendacion(n):
        menu =  {
            1 : ['Té negro' , '3 min' , 'Desayuno'] ,
            2 : ['Té verde' , '5 min' , 'Medio Día'] ,
            3 : ['Agua de hierbas' , '6 min' , 'Atardecer']
        }
        return tuple(menu[n])
    
    #metodo precio y formato presentacio del te
    @staticmethod
    def obt_precio_formato(precio):
        menu =  {
            300 : 3000 ,  # 300 gramos a $3000
            500 : 5000   # 500 gramos a $5000
        }
        return menu[precio]