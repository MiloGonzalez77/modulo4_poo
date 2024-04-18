from te import Te_artesanal

# Solicita al usuario que elija un tipo de te
tipo_te = int(input('''
Por favor elija con [numero] un tipo de té:
[1] Té negro
[2] Té verde
[3] Agua de hierbas \n
'''))

# Solicita al usuario que elija un tamanio de te. El usuario tendrá que escribir 300 o 500
formato = int(input('''
Escriba en [numero] el formato de presentacion del te: 
[300] gramos
[500] gramos \n
'''))

#Instancia de informacion del te elegido
sabor, tiempo, recomendacion = Te_artesanal.obt_preparacion_recomendacion(tipo_te)
precio = Te_artesanal.obt_precio_formato(formato)

#Impresion de datos
print(f'''
Detalles del Té elegido:
Sabor del té: [{sabor}].
Tamaño del té: [{formato}] gramos.
Precio: [${precio}].
Tiempo de preparación recomendado: [{tiempo}].
Recomendación: [{recomendacion}].
Duracion: [{Te_artesanal.duracion}].
\n''')
print("Fin de Programa.")