"""Calcular el total que una persona debe pagar en un llantera,
 si el precio de cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran 5 o mas"""

Compra=float(input("Ingrese la cantidad de llantas a vender:"))

if Compra < 5 :
    Ventatotal=Compra*800
    print("El total a pagar es de $",Ventatotal)
else :
     Compra>5
     Ventatotal=Compra*700
print("El total a pagar es de$",Ventatotal)

