"""1) Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
Inicio
Leer num1, num2
si num1 = num2 entonces
resul = num1 * num2
si no
si num1 > num2 entonces
resul = num1 - num2
si no
resul = num1 + num2
fin-si
fin-si
fin"""
Num1=int(input("Ingrese un numero:"))
Num2=int(input("Ingrese un numero:"))

if Num1 == Num2:
    print(Num1,"x",Num2,"=",Num1*Num2)
else: 
    if Num1 > Num2:
        print(Num1,"-",Num2,"=",Num1-Num2)
    else:
         print(Num1,"+",Num2,"=",Num1+Num2)
