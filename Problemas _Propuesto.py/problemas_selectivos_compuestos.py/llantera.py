"""2) En una llantera se ha establecido una promoción de las llantas marca “Ponchadas”, dicha promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300 cada una, de $250 si se compran de cinco a 10 y de $200 si se compran mas de 10.
Obtener la cantidad de dinero que una persona tiene que pagar por cada una de las llantas que compra y la que tiene que pagar por el total de la compra."""

compra=int(input("Ingrese la cantidad de llantas a comprar :"))

if compra < 5:
    precio=300
    total = compra * 300
    print("El precio por cada llanta es de : $",precio)
    print("EL total a pagar por la compra de las llantas es de : $",total)
elif compra < 10:
    precio = 250
    total = compra * 250
    print("El precio por cada llanta es de : $",precio)
    print("El total a pagar por la compra de las llantas es de :$",total)
else:
    precio=200
    total = compra * 200
    print("El precio por cada llanta es de : $",precio)
    print("El total a pagar por la compra de las llantas es de : $",total)