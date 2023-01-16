'''
TIPOS DE DATO
24/08/2022
ISAAC ROCHA TORRES
'''
producto ='Monitor Samsung de 27 pulgadas'
precio = 4599.8
descuento = 10 #Descuento del 1%
oferta = True

precio_oferta= precio -(precio * descuento)



'''
CONDICIONALES

1.- If
2.- If-else
3.- If Anidado
'''

if oferta:
    precio_oferta = precio - (precio * descuento / 100)
    print("Producto de oferta")
else:
    precio_oferta = oferta
    print("Producto sin oferta")

print("Producto: " + producto + "Precio: ", precio, "Oferta: "+str(precio_oferta))

op = 1

if op == 1:
    print("Domingo")
elif op == 2:
        print("Lunes")
elif op == 3:
        print("Martes")
elif op == 4:
        print("Miercoles")
elif op == 5:
        print("Jueves")
elif op == 6:
        print("Viernes")
elif op == 7:
        print("Sábado")
















'''
@isaakiin
'''