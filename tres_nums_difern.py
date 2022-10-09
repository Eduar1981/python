"""Leer tres números diferentes e imprimir el numero mayor de los tres."""
A=int(input("Ingrese un numero:"))
B=int(input("Intrese otro numero"))
C=int(input("Ingrese otro numero"))
if (A>B) and (A>C):
    print("El numero mayor es:",A)
else:
    if (B>A) and (B>C):
        print("El numero mayor es:",B)
    else:
         print("El numero mayor es:",C)