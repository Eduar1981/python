"""En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un numero que se escoge al azar.
 Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra, 
si es mayor o igual a 74 el descuento es del 20%. Obtener cuanto dinero se le descuenta."""

Compra=float(input("Ingrese el valor de la compra :$"))
Numero=float(input("Ingresa un numero :"))

if Numero < 74:
     descuento = Compra *.15
     print("El total a pagar por la compra es : $",Compra-descuento)
     print("El descuento aplicado en la compra es de",descuento)
else:
      descuento = Compra *.20
      print("El total a pagar por la compra es : $",Compra-descuento)
      print("El descuento aplicado en la compra es de",descuento)