'''
Tema: Ciclos
Fecha: 26/Agosto/2022
Autor: Isaac Rocha Torres

'''

#For variable in range (valor_inicial, valor_final, dezplazamiento)
#while

#1.-Imprimir del 1 al 100
'''for x in range(0,101, 2):
    print(x)
'''

#2.- Imprimir los número divisibles entre 3 del 500 al 100
'''
for x in range(500, 1000):
    if x%3 == 0:
        print(x)
'''

#3.- Imprime los números del 100 al 1
'''
for x in range(101,0, -1):
    print(x)
'''

# ********* WHILE

'''num = 10
while num > 0:
    num -=num -1
'''

#4.- Pedir números hasta que el usuario digíte un 0

'''
num = 1
while num != 0:
    num = int(input("Ingresa un número: "))
    print(num)
'''

#5.- Pedir números hasta que el usuario digíte un 0, nos detenemos

while True:
    num = int(input("Dame un número"))
    if num == 0:
        break
    print (num)
