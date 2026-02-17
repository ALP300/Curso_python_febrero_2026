'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes 
se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro 
diccionario con los datos del cliente (nombre, dirección, teléfono, correo). El programa debe preguntar
al usuario por una 
opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, (5) Terminar. En función de 
la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Terminar el programa.

#{Perú:"Mejor gastronomía"}
paises={"Perú":"Mejor gastronomía"}
paises["Italia"]="La mejor pizza"
paises["Mexico"]="El país con mejor música"
print(paises)

'''
#clientes={'2323':{"nombre": Leo, "direccion": av manzanas, "telefono": 2312,"email":leo@gmail.com}, '2323':{"nombre": Leo, "direccion": av manzanas, "telefono": 2312,"email":leo@gmail.com} }
clientes={}
opcion=''
while opcion!="5":
    if opcion=="1":
        nif = input('Introduce NIF del cliente: ') #2323
        nombre = input('Introduce el nombre del cliente: ') #Leo
        direccion = input('Introduce la dirección del cliente: ') #av manzanas
        telefono = input('Introduce el teléfono del cliente: ') #2312
        email = input('Introduce el correo electrónico del cliente: ') #leo@gmail.com
        cliente={"nombre": nombre, "direccion": direccion, "telefono": telefono,"email":email}
        clientes[nif]= cliente

