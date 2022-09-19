"""Calcular el numero de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la formula es:
num. pulsaciones = (220 - edad)/10"""
edad=int(input("Ingrese su edad:"))
beats=int(input("Ingrese las pulsaciones por minuto:"))
print("Las pulsaciones por minuto son:",(220-edad)/10)