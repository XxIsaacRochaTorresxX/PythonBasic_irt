'''
# Tema: Tuplas
# Fecha: 31 de agosto del 2022
# Autor: Isaac Rocha Torres
'''
# 1. Definición. Es una colección de elementos inmutables.
#             Las tuplas son immutables y normalmente contienen una secuencia heterogénea
#             de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuplas
# tupla1 = tuple()
# tupla2 = ()
# tupla3 = (2, 'Jose Luis', True, 4.5)

# 3. Accesar a elementos de la tupla, igual que en las listas
# print(tupla3[1])
#
# for e in tupla3:
#     print(e)

# 4. Operaciones.
# 4.A. Son inmutables
#tupla3[1] = 'Otra cadena'

# 4.B. Las tuplas pueden ser anidadas
# grupo_a = ('Jose Luis', 'Carmen', 'Esthela')
# grupo_b = ('Karyna', 'Luis', 'Karyna')
# grupo_c = (grupo_a, grupo_b)
# print (grupo_c)
# numeros = ( (3,4), (4,7), (7,90) )
# print(numeros)

# 4.C. Las listas se pueden convertir en tuplas  haciendo uso de la función tuple()
# lista = ['A', 'B', 'G', 'Z', 'C']
# tupla_letras = tuple(lista)
# print(tupla_letras)

# 4.D. Se puede asignar el valor de una tupla con n elementos a n variables
# alumno = (420100,'Jose Luis Abarca')
# control, nombre = alumno
# print("Control: ",  control, " Nombre: ", nombre)

# 5. Métodos de tuplas
# count() , regresa el numero de elementos existenctes en la tupla
# print(grupo_c.count(('Jose Luis', 'Carmen', 'Esthela')))

# index() Regresa el índice donde se ha encontrado, tambien puede pasarle un segundo
#          es a partir de que posición quieres buscar
# print("Posición: ", tupla_letras.index('G', 1))

'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el estado al que pertencen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''
from funciones_practica4 import *

pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Gualupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Nulvy Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]


ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

def menu_principal():
    while True:
        print(" =======================  Menú Principal =================================")
        print(" 1. Agregar pasajero ")
        print(" 2. Agregar ciudad ")
        print(" 3. Ciudad a la que viaja un pasajero ")
        print(" 4. Cantidad de pasajeros que viajan a la Ciudad ")
        print(" 5. A que estado viaja el pasajero ")
        print(" 6. Cantidad de pasajeros que viajan a un Estado ")
        print(" 7. Salir ")

        opcion = int(input("Dame tu opcion: "))

        # Evaluar la variable opcion
        if opcion == 1:
            print (" Agregar Pasajeros ")
            agregar_pasajeros(pasajeros)
            print(pasajeros)
        elif opcion == 2:
            print(" Agregar Ciudades ")
            agregar_ciudades(ciudades)
            print(ciudades)
        elif opcion == 3:
            print(" Ciudad a la que viaja el pasajero ")
            clave = int(input("Dame la clave del pasajero: "))
            ciudad = buscar_ciudad(clave,pasajeros)
            print(" El Pasajero: ", clave, " viaja a la ciudad de: ", ciudad )
        elif opcion == 4:
            print(" Cantidad de pasajeros que viajan a una ciudad ")
            ciudad = input ("Dame la ciudad: ")
            print("La cantidad de pasajeros que viajan a la ciudad: ", ciudad, " son: ",contar_pasajeros(ciudad,pasajeros))
        elif opcion == 5:
            print(" Estado al que viaja un pasajero " )
            clave = int(input("Dame la clave del pasajero: "))
            print(" El estado al que viaja es: ", regresa_estado(clave, pasajeros, ciudades))
        elif opcion == 6:
            pass
        elif opcion == 7:
            break
        else:
            print(" Opción no válida ")

# Mandar llamar el menu principal
menu_principal()


'''@isaakiin'''
