"""Una empresa de bienes raíces ofrece casas de interés social, bajo las siguientes condiciones: Si los ingresos del comprador 
son menores de $8000 o mas el enganche será del 15% del costo de la casa y el resto se distribuirá en pagos mensuales,
 a pagar en diez años. Si los ingresos del comprador son menos de $8000 o mas el enganche será del 30% del costo de la casa y 
 el resto se distribuirá en pagos mensuales a pagar en 7 años.
La empresa quiere obtener cuanto debe pagar un comprador por concepto de enganche y cuanto por cada pago parcial."""

costo=float(input("Ingresa el costo de la casa:$"))
ingreso=float(input("Escriba los ingresos del comprador :$"))

if ingreso < 8000 :
    enganche = costo * .15
    parcial = (costo-enganche)/(12*10)
    print("Se aplico un 15% de enganche")
    print("El enganche a pagar es de :$",enganche)
    print("Los parciales a pagar son :$",parcial)

else:
    enganche = costo * .30
    parcial = (costo-enganche)/(12*7)
    print("Se aplico un 30% de enganche")
    print("El enganche a pagar es de :$",enganche)
    print("Los parciales a pagar son :$",parcial)