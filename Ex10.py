def div(a,b):
    try:
        c = a//b
        print("La divisio de {} entre {} és {}".format(a,b,c))

    except ZeroDivisionError:
        print("El segon paramentre de la funcio no pot ser zero")

#Pprincipal
a = int(input("Introdueix el numerador: "))
b = int(input("Introdueix el denominador: "))
c = div(a,b)