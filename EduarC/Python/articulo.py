"""El dueño de una tienda compra un articulo a un precio determinado. Obtener el precio en que lo debe vender para obtener una ganancia del 30%."""
NewBuy = float(input("Ingrese el valor del nuevo articulo:$"))  
Porcentaje_aumento = 30
Increace=NewBuy*(Porcentaje_aumento)/NewBuy
NewPrice_with_Increace = NewBuy+Increace
print("Nuevo valor de venta para el articulo:$",NewPrice_with_Increace)