"""Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aerobico;
 la formula que se aplica cuando el sexo es femenino es:
num. pulsaciones = (220 - edad)/10
y si el sexo es masculino:
num. pulsaciones = (210 - edad)/10"""

edad=int(input("Ingrese su edad:"))
numero=int(input("Ingrese un numero de acuerdo a tu genero, 1 es para  sexo femenino y 2 es para sexo masculino :"))
pulsaciones=float

if numero == 1:
    pulsaciones=(220-edad)/10

elif numero == 2 :
    
    pulsaciones=(210-edad)/10
else:
    input("Escribe un numero correcto:")
print("El numero de tus pusaciones de acuerdo a tu edad es: ",pulsaciones)