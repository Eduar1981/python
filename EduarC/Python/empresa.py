"""Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida"""
Socio1=float(input("Ingrese la cantidad de dinero del primer inversor:$"))
Socio2=float(input("Ingrese la cantidad de dinero del segundo inversor:$"))
Socio3=float(input("Ingrese la cantidad de dinero del tercer inversor:$"))
Total_company = Socio1+Socio2+Socio3
Socio1=Socio1*100/Total_company
Socio2=Socio2*100/Total_company
Socio3=Socio3*100/Total_company
print("El porcentaje de inversion del primer socio, sobre el total es de : ",Socio1)
print("El porcentaje de inversion del segundo socio, sobre el total es de : ",Socio2)
print("El porcentaje de inversion del tercer socio, sobre el total es de :  ",Socio3)