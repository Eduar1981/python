"""Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la sig. tabla:
Tiempo Utilidad
Menos de 1 año 5 % del salario
1 año o mas y menos de 2 años 7% del salario
2 años o mas y menos de 5 años 10% del salario
5 años o mas y menos de 10 años 15% del salario
10 años o mas 20% del"""
Nombre = input("Ingrese el nombre del empleado: ")
Tiempo1 = int(input("Ingrese el tiempo, en años, que el empleado lleva trabajando en la compañia: "))
Salario=float(input("Ingrese el valor del salario mensual: $"))
Tiempo1=0
Tiempo2=0
Salario=0
Utilidad=0

if Tiempo1<=1:
    print("El empleado",Nombre,"tiene de ganancia por tiempo trabajado durante el ultimo año de:$",Utilidad=Salario*0.05)
elif Tiempo1 >1 & Tiempo1<2:
    print("El empleado",Nombre,"tiene de ganancia por tiempo trabajado durante el ultimo año:$",Utilidad=Salario*0.1)
if Tiempo1 >2 & Tiempo1<5:
    print("El empleado ",Nombre," tiene de ganancia por tiempo trabajado durante el ultimo año",Utilidad=Salario*0.07)
elif Tiempo1<=5 & Tiempo1<10:
    print("El empleado",Nombre,"tiene de ganancia por tiempo trabajado durante el ultimo año de:$",Utilidad=Salario*0.15)
if Tiempo1>=10:
    print("El empleado",Nombre,"tiene ganado por tiempo trabajado durante el ultimo año de:$",Utilidad*Salario*0.2)
    #Pendiente, terminarlo
