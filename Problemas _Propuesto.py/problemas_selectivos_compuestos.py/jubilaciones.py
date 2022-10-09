"""6) El IMSS requiere clasificar a las personas que se jubilaran en el año de 1997. Existen tres tipos de jubilaciones: por edad, 
por antigüedad joven y por antigüedad adulta. Las personas adscritas a la jubilación por edad deben tener 60 años o mas y una antigüedad
 en su empleo de menos de 25 años. Las personas adscritas a la jubilación
  por antigüedad joven deben tener menos de 60 años y una antigüedad en su empleo de 25 años o mas.
Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o mas y una antigüedad en su empleo de 25 años o mas.
Determinar en que tipo de jubilación, quedara adscrita una persona."""

edad=int(input("Ingrese su edad:"))
antiguedad=int(input("Ingrese su antiguedad en el empleo:"))

if edad >=60 and antiguedad<25 :
    print("A usted le corresponde una jubilacion por edad")
elif edad<60 and antiguedad>=25:
    print("A usted le corresponde una jubilacion joven" )
elif  edad>=60 and antiguedad>=25:
    print("A usted le corresponde la jubilacion por vejes")
else:
    print("Todavia no estas en edad o tiempo de jubilacion")