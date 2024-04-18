import os

#MANIPULAR ARCHIVOS
#log_file1 = open(os.path.abspath("dia11/logs/error.log"))
#FileNotFoundError: [Errno 2] No such file or directory: 'F:\\Bootcamp_Python\\0044-2\\POO\\logs\\error.log'
#FileNotFoundError: [Errno 2] No such file or directory: 'F:\\Bootcamp_Python\\0044-2\\POO\\dia11\\logs\\error.log'

#Lectura de un archivo existente con read()
log_file2 = open(os.path.abspath("dia11/index.html"),'r')
#FileNotFoundError: [Errno 2] No such file or directory: 'F:\\Bootcamp_Python\\0044-2\\POO\\dia11\\logs\\error.log'
#print(log_file2.read())
print("---------")
print(log_file2.readlines())
print("---------")
#Lectura linea a linea
with open(os.path.abspath("dia11/index.html"), "r") as archivo:
    print(archivo)
    for linea in archivo:
        print(linea.strip())
        
#SOLO ESCRITURA
