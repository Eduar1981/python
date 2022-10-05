"""8) Una persona desea iniciar un negocio, para lo cual piensa verificar cuanto dinero le prestara el banco por hipotecar su casa.
 Tiene una cuenta bancaria, pero no quiere disponer de ella a menos que el monto por hipotecar su casa sea muy pequeño. 
 Si el monto de la hipoteca es menor que $1 000 000 entonces invertirá el 50% de la inversión total y un socio invertirá el otro 50%. 
 Si el monto de la hipoteca es de $ 1 000 000 o mas, entonces invertirá el monto total de la hipoteca y el resto del dinero que se necesite para cubrir
  la inversión total se repartirá a partes iguales entre el socio y el."""

Negocio=float(input("Ingresa el monto total del valor del negocio:$"))
Prestamo=float(input("Ingrese el monto de la hipoteca:$"))

if Prestamo < 1000000:
    inversion = Negocio*.5
    print("El 50 por ciento de la inversion de cada socio es:",inversion)

elif  Prestamo < Negocio:
    inversion = (Negocio - Prestamo)/2
   
    print("La inversion total del prestamo",Prestamo)
    print("La inversion que le corresponde a cada socio es:$",inversion)
else:
    print("Reconcidera la inversion")