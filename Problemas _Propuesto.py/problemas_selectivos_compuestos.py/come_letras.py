# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word=input("Ingresa una palabra: ")
user_word=user_word.upper()
consonantes="BCDFGHJKLMNÑPQRSTVWXYZ"

for letter in user_word:
    if letter not in consonantes:
        continue
    print(letter)
    # Completa el cuerpo del bucle for.
    # Otra forma de hacerlo
    
# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word=input("Ingresa una palabra:")
user_word=user_word.upper()
word_without_vowels="BCDFGHJKLMNÑPQRSTVWXYZ"

for letter in user_word:
    if letter not in word_without_vowels:
        continue
    print(letter)
   # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.