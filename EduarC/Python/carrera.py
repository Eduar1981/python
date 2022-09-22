"""Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera."""
Monday=float(input("Ingresa los datos de tu tiempo,lunes:"))
Tuesday=float(input("Ingresa los datos de tu tiempo,martes:"))
Wednesday=float(input("Ingresa los datos de tu tiempo,miercoles:"))
Average_time=(Monday+Tuesday+Wednesday)/3
print("El promedio de tiempo que estas tardando en recorrer tu ruta a la semana es de:",Average_time)