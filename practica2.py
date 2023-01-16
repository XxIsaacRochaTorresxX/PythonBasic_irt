'''
Tema: Listas
Fecha: 29 de agosto del 2022
Autor: Isaac Rocha Torres
'''

#Estructuras de python que son actualizables

#Listas
'''
nombre_lista = []
otra_lista = list()
'''

#Accesar a elementos de una lista
#nombre_lista[posición]
lista = ['Juan', 'Pedro', 'Carmen','Lucia','José'];
print(lista[1])
for x in range(5):
    print(lista[x])

print(lista)

print("Longitud de la lista: " + str(len(lista)) + "\n");

#4.-Debanado (una parte o rebanadas de la lista)

'''extracción de elementos'''

print(lista[0:2])#'''el limite inferior se incluye, el superior no'''
print(lista[ :2])#al dejar en blanco el primero se entiende que es desde 0
print(lista[2: ])#desde el 2 hasta el último
print(lista[2 : 4])#si no existe en el rango marca error
print(lista[-1])#imrpime el último elemento
print(lista[-5:-3])#listas[inicio:fin]

#2.- Agregar elementos en una posición dada nombre_lista.insert(posicion,elemento)
lista.insert(2,'Navarrete')

#3.-Eliminar el primer elemento que encuentra en la lista, manda un ValueError si no existe
#nombre_lista.remove(elemento)

lista.remove('Juan')
print(lista)


#4.-Quitar el último elemento de la lista, se puede pasar la posición, en caso de no existir IndexError
'''
lista.pop(10)
lista.pop(0) //quita el primero
lista.pop()// quita el último
'''

lista.pop()
print(lista)

#5.-Regresar el índice del primer elemento encontrado, sino existe lanza una excepción
#print(lista.index(3))
print(lista.index('Carmen'))

#6.- Reegresar el número de veces que aparece un elemento en la lista
lista.insert(2,'Juan')
print(lista)
print(lista.count('Juan'))

#7.- Invertir elementos de una lista
#primero lo inviertes, luego imprimes
lista.reverse()
print(lista)



#8.-Listas por compresión
#A.- genera un alista con los primeros 5 numeros

lista2 = [i for i in range(5)]
print(lista2)


#B. Generar una lista cin nueros aleatorios del 1 al 100
import random
lista2 = [random.randint(1,100) for i in range(10)]
print(lista2)

print("\n"+"\n")

lista3 = [[18420478, 'Isaac', 0], [18420493, 'Ayleen', 100], [18420470, 'Isaias', 100],[18420400, 'Fernando', 100],[18420463, 'Javier', 100],];

for x in range(len(lista3)):
    print(lista3[x])


'''@isaakiin'''
