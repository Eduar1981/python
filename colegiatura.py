"""En una escuela la colegiatura de los alumnos se determina según el numero de materias que cursan. El costo de todas las materias es el mismo.
Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el ultimo 
periodo es mayor o igual que 9, se le hará un descuento del 30% sobre la colegiatura y no se le cobrara IVA; 
si el promedio obtenido es menor que 9 deberá pagar la colegiatura completa, la cual incluye el 10% de IVA.
Obtener cuanto debe pagar un alumno."""

materias=float(input("Ingresa el total de materias que cursas:"))
costo=float(input("Ingresa el costo de una de las materias:$"))
promedio=float(input("Ingrese el promedio del ultimo periodo:"))
colegiatura=materias*costo

if promedio >= 9:
    descuento = colegiatura*.30
    total = colegiatura-descuento
    print("El total a pagar por",materias,"materias es $",total)
    print("El descuento aplicado es de :$",descuento)
    
else:
    descuento=0
    total =colegiatura + (colegiatura*.10)
    print("El total a pagar por",materias,"materias es $",total)
    print("El descuento es de :$",descuento)