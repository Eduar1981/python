"""El gobierno ha establecido el programa SAR (Sistema de Ahorro para el Retiro) que consiste en que los dueños de la empresa deben obligatoriamente
 depositar en una cuenta bancaria un porcentaje del salario de los trabajadores; adicionalmente los trabajadores pueden solicitar
  a la empresa que deposite directamente una cuota fija o un porcentaje de su salario en la cuenta del SAR, la cual le será descontada de su pago.
Un trabajador que ha decidido aportar a su cuenta del SAR desea saber la cantidad total de dinero que estará depositado a esa cuenta cada mes,
 y el pago mensual que recibirá."""

salario=float(input("Ingrese el valor del salario mensual:$"))
x=int(input("Ingresa una opcion: opcion 1= cuota fija, opcion 2= porcentaje:"))

sar=float
porcentaje=float

if x ==1 or x == 2:

 if x ==1:
     
  sar=float(input("Ingresa la cuaota fija para el SAR:$"))
  print("La cantida de dinero para el SAR cada mes es de: $",sar)
  print("Tu salario mensual es de: $",salario-sar)
else:
      porcentaje=(float(input("Ingresa un porcentaje para el SAR:$")))
      sar=(salario*porcentaje)/100
      print("La cantida de dinero para el SAR es de: $",sar)
      print("Tu salario mensual es de: $",salario-sar)

