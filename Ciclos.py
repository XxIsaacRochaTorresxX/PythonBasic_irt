'''
Tema: Estructura de datos
Fecha: 26/Agosto/2022
Autor: Isaac Rocha Torres

If
If-else
If-else anidado
elif

se debe cerrar con :
'''

#Pedir un número del teclado y mostrar el valor absoluto

'''
numero = int(input("Dame un número: ")); #input recibe del teclado strings
if numero <0:
    numero = numero*(-1);
print("Valor absoluto", numero); 
'''

#Pedir 2 nombres, si la primera letra coincide o la última coinciden, entonces existe coincidencia
#de lo contrario no hay. (con len se obtiene la longitud de una cadena o -1)

'''
nombre1 = input("Dame el primer nombre");
nombre2 = input("Dame el segundo nombre");
pos1= len(nombre1)-1;
pos2= len(nombre2)-1;

podemos acceder directo a las posiciones

if nombre1[0] == nombre2[0] or nombre1[pos1] == nombre2[pos2]: #nombre1[-1] == nombre2[-1]
    print("Existe coincidencia")
else:
    print("No existe la coincidencia")
'''

#Crear un programa que permita al usuario elegir un candidato por el cual votar, las posibilidades son
'''
    Candidato A
    Candidato B
    Candidato C
    Candidato D
    
    Según el candidato(A,B, o B) se le debe permitir imprimir un mensaje Usted ha votado
    muestra opcion no válida
'''

'''
voto = (input("Ingresa el candidato: ")).upper();

if voto == 'A':
    print("Usted votó por ROJO");
elif voto == 'B':
        print("UAsted votó por VERDE")
elif voto == 'C':
        print("Usted votó por AZUL")
elif voto == 'D':
        print("Usted votó por MORENA")
elif voto != 'A' or voto!= 'B' or voto != 'C' or voto != 'D':
        print("Opción Erronéa")
'''

#4.- Pedir una letra y si es una vocal ¿, mostrar el mensaje de que es una vocal, validar que se haya introducido una letra
# con IN  se verifica si un caracter se encuentra dentro de una cadena

'''
letra = input("Dame una cadena").upper();
#Verificar que solo sea una letra
if len(letra) ==1:
    if letra in "AEIOU":
        print("Es una vocal");
    else:
        print("No es una vocal");
else:
    print("Debe ser solo una letra");
'''