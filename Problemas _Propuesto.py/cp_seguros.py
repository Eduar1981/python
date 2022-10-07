"""Una compañía de seguros esta abriendo un depto. de finanzas y estableció un programa para captar clientes,
 que consiste en lo siguiente: Si el monto por el que se efectúa la fianza es menor que $50 000 la cuota a pagar será por el 3% del monto,
  y si el monto es mayor que $50 000 la cuota a pagar será el 2% del monto. 
La afianzadora desea determinar cual será la cuota que debe pagar un cliente."""

monto=float(input("Ingrese el monto de la fianza : $"))
if monto < 50000:
    interes = monto*.03
    print("Se aplico el 3% de interes")
    print("El interes a pagar es:$",interes)
    print("La cuaota total a pagar es de :$",monto+interes) 
else:
    interes = monto*.02
    print("Se aplico el 2% de interes")
    print("El interes a pagar es:$",interes)
    print("La cuaota total a pagar es de :$",monto+interes)