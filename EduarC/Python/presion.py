"""La presión, el volumen y la temperatura de una masa de aire se relacionan por la formula:
masa = (presión * volumen)/(0.37 * (temperatura + 460))"""
presion=float(input("Ingrese  la presion:"))
volumen=float(input("Ingrese el volumen:"))
temperatura=float(input("Ingrese la temperatura:"))
print("La masa de aire es igual a",(presion * volumen)/(0.37 * (temperatura + 460) ))