"""11) Una persona se encuentra con un problema de comprar un automóvil o un terreno,
 los cuales cuestan exactamente lo mismo. Sabe que mientras el automóvil se devalúa, con el terreno sucede lo contrario. 
 Esta persona comprara el automóvil si al cabo de tres años la devaluación de este no es mayor que la mitad del incremento del valor del terreno. 
Ayúdale a esta persona a determinar si debe o no comprar el automóvil."""

precio=float(input("Ingres el valor del automovil y del terreno :$"))
incremento=float(input("Ingresa el incremento anual del terreno : %"))
decremento=float(input("Ingresa la devaluacion anual del automovil : %"))
decremento = ((precio*decremento)/100*3)
incremento = (((precio*incremento)/100*3)/2)

print("La mitad del incremento del terreno en tres años es : $",incremento)
print("La devaluacion del automovil en tres años es de : $",decremento)

if decremento < incremento:
    print("Te conviene comprar el automovil")
else:
    print("Te conviene comprar el terreno")