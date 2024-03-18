def lenp(frase):
    a = frase.split(" ")
    b = list(map(len, a))
    return b

#Programa Principal
a = input("Introduce una frase: ")
resultado = lenp(a)
print("La longitud de las palabras de la frase '{}' és: {}".format(a,resultado))
