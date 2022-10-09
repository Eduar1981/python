"""5) En una tienda de descuento se efectúa una promoción en la cual se hace un descuento sobre el valor de la compra total
 según el color de la bolita que el cliente saque al pagar en caja. Si la bolita es de color blanco no se le hará descuento alguno,
  si es verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si es roja un 100%. 
  Determinar la cantidad final que el cliente deberá pagar por su compra. se sabe que solo hay bolitas de los colores mencionados."""

compra=float(input("Ingrese le valor de la compra $"))
bolita=str(input("Ingresa el color de la bolita,: blanca,verde,amarilla,azul,roja : "))


if bolita=="blanca":
    descuento = 0
    print("El valor total a pagar ya con el descuento aplicado es : $",compra-descuento)
    print("El descuento aplicado es del:",descuento,"%")
elif bolita == "verde":
    descuento=compra*.10
    print("El valor total a pagar ya con el descuento aplicado es : $",compra-descuento)
    print("El descuento aplicado es del:",descuento,"%")
elif bolita =="amarilla":
    descuento=compra*.25
    print("El valor total a pagar ya con el descuento aplicado es :$",compra-descuento)
    print("El descuento aplicado es del:",descuento,"%")
elif bolita =="azul":
    descuento=compra*.50
    print("El valor total a pagar ya con el descuento aplicado es :$",compra-descuento)
    print("El descuento aplicado es del:",descuento,"%")
elif bolita=="roja":
     descuento=compra*1
     print("El valor total total a pagar ya con el descuento aplicado es :$",compra-descuento)
     print("El descuento aplicado es del:",descuento,"%")
else:
    print("El color de la bola no existe")




