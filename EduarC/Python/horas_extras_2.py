"""Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extras y que estas se pagan al doble de una hora normal cuando no exceden de 8; si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se pagan las horas normales y el resto al triple."""
Ht=int(input("Ingrese la cantidad de horas trabajadas:"))
Pph=float(input("Ingrese el valor de pago por hora  $"))
Triples=0
Dobles=0
Sueldo=0
if Ht > 48:
    Triples = Ht-48
    Dobles = 8
    Sueldo=(40*Pph)+(Dobles*Pph*2)+(Triples*Pph*3)
elif Ht>40:
        Dobles=Ht-40
        Sueldo=(40*Pph)+(Dobles*Pph*2)
else:
        Sueldo=Ht*Pph
print("El sueldo por las horas",Ht,"horas es $",Sueldo)
print("Se pago",Dobles,"horas al dobles es $",Dobles*Pph*2)
print("Se pago",Triples," horas al triple es $",Triples*Pph*3)