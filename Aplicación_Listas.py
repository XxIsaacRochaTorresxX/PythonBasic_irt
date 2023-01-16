'''
Tema: Listas
Fecha: 29 de agosto del 2022
Autor: Isaac Rocha Torres
'''
'''
lista = [
    [18420478, 'Isaac', 0],
    [18420493, 'Ayleen', 100],
    [18420470, 'Isaias', 100],
    [18420400, 'Fernando', 100],
    [18420463, 'Javier', 100],
];

l1 = [18420478, 'Isaac', 0]
l2 = [18420493, 'Ayleen', 100]
l3 =  [18420400, 'Fernando', 100]
lista1 = l1, l2, l2

#print(lista1)

for x in range(len(lista)):
    print(lista[x])


for l in lista:
    print(l[-1])


#Crear una loista con los promedios de la lista
promedio=[]
for l in lista:
    promedio.append(l[-1])
print(promedio)



#Crear lista por compresión de pormedios
promedio2 = [l[-1] for l in lista] #dato_lista, ciclo, dde dónde
print(promedio2)


#Crear lista de estudiantes
#1.- Menu principal: insertar, eliminar, actualizar, imprimir y salir
#2.- Si el usuario teclea otra opción diferente que sea válido
 '''
estudiantes = ['Juan', 'Pedro', 'Carmen','Lucia','José'];

def buscar(nom):
    for estd in estudiantes:
        if(nom == estd[1]):
            return True
        return False
#print(buscar('Juan'))

def insertar (nom):
    estudiantes.append(nom)

def eliminar(nom):
    estudiantes.remove(nom)

def actualizar(op, nom):
    estudiantes.insert(op, nom)

def imprimir (op):
    print(estudiantes[op])


print("xxxxx MENÚ xxxxx")
print("1.- Buscar"+ "\n"+
      "2.- Insertar"+ "\n"+
      "3.- Eliminar"+ "\n"+
      "4.- actualizar"+ "\n"+
      "5.- imprimir"+ "\n"+
      "6.- Salir"+ "\n"
      )

opc = int(input("¿Qué desea realizar?"))
nom=1
op = 1
while opc != 6:

    if opc == 1:
        nom = input("Ingresa nombre a buscar")
        buscar(nom)
    elif opc == 2:
        nom = input("Ingresa nombre a insertar")
        insertar(nom)
    elif opc == 3:
        nom = input("Ingresa nombre a eliminar")
        eliminar(nom)
    elif opc == 4:
        op = input("Posicion a actualizar")
        nom = input("Ingresa nombre a insertar")
        actualizar(op, nom)
    elif opc == 5:
        op = int(input("Posicion a imprimir"))
        imprimir(op)
    elif opc == 6:
        break
    opc = int(input("¿Qué desea realizar?"))


'''@isaakiin'''


