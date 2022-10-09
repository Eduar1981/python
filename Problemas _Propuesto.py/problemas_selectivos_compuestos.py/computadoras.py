"""1) En una fabrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del numero de computadoras que compre.
 Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; 
 si el numero de computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o mas se
  les da un 40% de descuento. El precio de cada computadora es de $11,000"""

compra=int(input("Ingrese la cantidad de computadoras a comprar :"))

if compra < 5:
    total = compra * 11000
    descuento = total *.10
    print("El total a pagar por",compra," computadoras es de : $",total-descuento)
    print("El descuento aplicado por el total de la compra es de : $",descuento,"%")

elif compra < 10:
    total = compra * 11000
    descuento = total *.20
    print("El total a pagar por",compra," computadoras es de : $ ",total-descuento)
    print("El descuento aplicado por el total de la compra es de : $",descuento)
else:
    compra >= 10
    total = compra * 11000
    descuento = total *.40
    print("El total a pagar por",compra,"computadoras es de : $ ",total-descuento)
    print("El descuento aplicado por el total de la compra es de : $",descuento)
