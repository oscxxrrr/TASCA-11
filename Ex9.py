def potencia(p):
    r = [x**p for x in range(1,10)]
    print("Les potencies elevades a {} dels 10 primers numeros és {}".format(p,r))

#PP
p = int(input("Introdueix un numero que vulguis elevar a la resta: "))
potencia(p)