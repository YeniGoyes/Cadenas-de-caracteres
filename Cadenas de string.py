#Explicación de dos cadenas de string#

#Cadenas: maketrans y lstrip#

#str.maketrans#

#Reemplzar

#Ejemplo 1#

#Se requiere interpretar los números  por letras#


Número = input("Ingrese un número del 1 al 10: ")

tabla = str.maketrans('1234567890', 'abcdefghij')

Número = Número.translate(tabla)

print(Número, type(Número))
  
#Segundo ejemplo" 

#Se necesita borrar caracteres diferentes de letras#

tabla = str.maketrans('','','0123456789!@#$%^&*()')

Nombre = input("Ingrese su nombre completo: ")

Nombre = Nombre.translate(tabla)

print(Nombre, type(Nombre))

#Ejemplo 3#

#Se necesita únicamante las vocáles en mayúscula#

tabla = str.maketrans('aeiou', 'AEIOU')

Pasatiempo = input("Ingrese su pasatiempo favorito: ")

Pasatiempo = Pasatiempo.translate(tabla)

print(Pasatiempo, type(Pasatiempo))

#str.lstrip#

#Eliminar caráteres#

#Ejemplo 1#

#Se necesita eliminar los espacios en blanco al inicio de una cadena#

Dirección = input("Ingrese su dirección: ")

print(repr(Dirección))

print(repr(Dirección.lstrip()))

print(Dirección, type(Dirección.lstrip))

#Ejemplo 2#

#Eliminar ceros de la izquierda#

Número = input("Ingrese un número sin ceros a la izquierda: ")

print(repr(Número))

print(repr(Número.lstrip('0')))

print(Número, type(Número.lstrip('0')))

#Ejemplo 3#

#Eliminar caracteres específicos al inicio de una cadena#

Frase = input("Ingrese una frase con sin vocales al inicio: ")

print(repr(Frase))

print(repr(Frase.lstrip('aeiou')))

print(Frase, type(Frase.lstrip('aeiou')))



#Parte 2#

#EJEMPLOS DE CADENAS#

#Contar cuenta veces se repite una letra en un texto#

Poema = input("Ingresa un poema corto: ")
letra = input("Ingresa la letra que quiere contar: ")

contador = Poema.count(letra)

print(f"En el poema '{Poema}' la letra '{letra}' aparece {contador} veces.")

print(type(Poema), type(letra), type(contador))

#Identificar si los símbolos de una frase son solo letras#

Frase = input("Ingresa una frase corta: ")

if Frase.replace(" ", "").isalpha():
    print(f"La frase '{Frase}' contiene solo letras.")
else:
    print(f"La frase '{Frase}' contiene otros símbolos además de letras.")

print(type(Frase), type(Frase.isalpha()))


#Contar la cantidad de consonantes en un texto#

Oración = input("Escribe una oración corta: ")

vocales = "aeiouáéíóúüAEIOUÁÉÍÓÚÜ"
consonantes = 0

for letra in Oración:
    if letra.isalpha() and letra not in vocales:
        consonantes += 1

print("Cantidad de consonantes:", consonantes)

print(consonantes, type(consonantes))




#Actividad de clase #

#Como extraer caracteres de un texto#

Palabra = input("coloca una palabra: ")

Letra = int(input("Ingresa en números(comienza en 0), la letra que quieres extraer: "))

print("Esa es la letra: ", Palabra [Letra])











                      

















