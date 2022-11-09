"""3) En un juego de preguntas a las que se responde “Si” o “No” gana quien responda correctamente las tres preguntas. 
Si se responde mal a cualquiera de ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:
1. Colon descubrió América?
2. La independencia de México fue en el año 1810?
3. The Doors fue un grupo de rock Americano?"""


input("En el siguente juego, de preguntas, gana quien responda correctamente las tres preguntas, si te equivocas en cualquiera de las tres pierdes y se termina el juego")

input("Responda si o no a las siguientes preguntas")

respuesta1=str(input("1. Colon descubrió América?:"))

if respuesta1 == "si":
   respuesta2=str(input("2. La independencia de México fue en el año 1810?:"))
if respuesta2 == "si":
   respuesta3=str(input("3. The Doors fue un grupo de rock Americano?:"))
if respuesta3 == "si":
    print("Respuesta correcta",end=", ")
    print("felicidades has ganado el juego")
else:
 print("Respuesta equivocada, vuelve a intentarlo")
 print("Fin del juego")

