"""9) El gobierno del estado de México desea reforestar un bosque que mide determinado numero de hectáreas. 
Si la superficie del terreno excede a 1 millón de metros cuadrados, entonces decidirá sembrar de la sig. manera:
Porcentaje de la superficie del bosque Tipo de árbol
70% pino
20% oyamel
10% cedro
Si la superficie del terreno es menor o igual a un millón de metros cuadrados, entonces decidirá sembrar de la sig. manera:
Porcentaje de la superficie del bosque Tipo de árbol
50% pino
30% oyamel
20% cedro
El gobierno desea saber el numero de pinos, oyameles y cedros que tendrá que sembrar en el bosque, si se sabe que en 10 metros cuadrados caben 8 pinos,
 en 15 metros cuadrados caben 15 oyameles y en 18 metros cuadrados caben 10 cedros. También se sabe que una hectárea equivale a 10 mil metros cuadrados."""

import math

Metros=float
Pinos=float
Oyameles=float
Cedros=float
Hectarea=int(input("Ingrese las hectareas del terreno:"))
Metros=Hectarea*10000

if Metros>1000000:
    Pinos=Metros*.70
    Oyameles=Metros*.20
    Cedros=Metros*.10

elif Metros<=1000000:
      Pinos=Metros*.50
      Oyameles=Metros*.30
      Cedros=Metros*.20 
     
      
      
print("Arboles que se puedan sembrar: Pinos", math.trunc(Pinos/10)*8,"en",Pinos,"m2")
print("Arboles que se puedan sembrar: Oyameles","Oyameles",math.trunc(Oyameles/15)*15,"en",Oyameles,"m2")
print("Arboles que se puedan sembrar: Cedros","Cedros",math.trunc(Cedros/18)*10,"en",Cedros,"m2")


