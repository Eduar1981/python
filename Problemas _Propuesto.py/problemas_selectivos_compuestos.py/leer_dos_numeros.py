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

num1=int(input("Ingresa un numero :"))
num2=int(input("Ingresa un numero :"))

if num1 == num2:
    print(num1,"x",num2,"=",num1*num2)
elif num1>num2:
    print(num1,"-",num2,"=",num1-num2)
else:
    print(num1,"+",num2,"=",num1+num2)