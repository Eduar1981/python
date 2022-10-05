"""10) Una fabrica ha sido sometida a un programa de control de contaminación para lo cual se efectúa una revisión de los puntos IMECA,
 generados por la fabrica. El programa de control de contaminación consiste en medir los puntos IMECA que emite la fabrica en cinco días de una semana
  y si el promedio es superior a los 170 puntos entonces tendrá la sanción de parar su producción por una semana
   y una multa del 50% de las ganancias diarias cuando no se detiene la producción. Si el promedio obtenido de puntos IMECA es de 170 o menor entonces,
    no tendrá ni sanción ni multa. El dueño de la fabrica desea saber cuanto dinero perderá después de ser sometido a la revisión."""

"""ALGORITMO PARA CALCULAR PUNTOS IMECA
OZONO (O3)=IMECA DE O3 = (CONCENTRACIÓN DE O3 * 100) / 0.11
MONÓXIDO DE CARBONO (CO) =IMECA DE CO = (CONCENTRACIÓN DE CO * 100) / 11
PARTÍCULAS SUSPENDIDAS FRACCIÓN RESPIRABLE (PM10) DE 0 A 120 µ/m3 = IMECA PM10 = CONCENTRACIÓN DE PM10 * 0.833
DE 121 A 320 µ/m3
IMECA PM10 = (CONCENTRACIÓN DE PM10 * 0.5) + 40
MAYOR A 320 µ/m3
IMECA PM10 = CONCENTRACIÓN DE PM10 * 0.625
BIÓXIDO DE AZUFRE (SO2)
IMECA SO2 = ( CONCENTRACIÓN DE SO2 * 100 ) / 0.13
BIÓXIDO DE NITROGENO (NO2)	
IMECA DE NO2 = ( CONCENTRACIÓN DE NO2 * 100 ) / 0.21"""


LecturaDuno=float(input("Ingrese la lectura del dia uno:"))
LecturaDdos=float(input("Ingrese la lectura del dia dos:"))
LecturaDtres=float(input("Ingrese la lectura del dia tres:"))
LecturaDcuatro=float(input("Ingrese la lectura del dia cuatro:"))
LecturaDcinco=float(input("Ingrese la lectura del dia cinco:"))

promedio=(LecturaDuno+LecturaDdos+LecturaDtres+LecturaDcuatro+LecturaDcinco)/5

GananciaDuno=float(input("Ingresa la ganancia del dia uno:"))
GananciaDdos=float(input("Ingrese la ganancia del dia dos:"))
GananciaDtres=float(input("Ingrese la ganancia del dia tres:"))
GananciaDcuatro=float(input("Ingrese la ganancia del dia cuatro:"))
GananciaDcinco=float(input("Ingrese la ganancia del dia cinco:"))
total = (GananciaDuno)+(GananciaDdos)+(GananciaDtres)+(GananciaDcuatro)+(GananciaDcinco)

if promedio > 170:
    multa = total * .5
    print("El promedio de puntos IMECA es de :",promedio)
    print("La ganancia total de una semana es de:$",total- multa)
    print("La perdida de dinero por la revision es de :$",multa)
else:
    multa = 0

    print("El promedio de puntos IMECA es de :",promedio)
    print("La ganancia total de una semana es de:$",total- multa)
    print("La perdida de dinero por la revision es de :$",multa)