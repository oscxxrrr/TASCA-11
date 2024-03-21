def menu():
    op = 0
    while op > 1 or op < 14:
        print("""
            Programa exmane:
            1-Estructuras condicionals, if
            2-Estructuras condicionals, match
            3-Estructuras iterativas, for e in b
            4-Estructuras iterativas, for i in range(x)
            5-Estructuras iteratives, for i,e in enumerate(a)
            6-Funcio amb parametres
            7-Funció lambda
            8-Funcio list compehension
            9-Funcio map
            10-Funcio zip
            11-Funcio filter
            12-Classes i objectes
            13-Fitxers
            14-Sortir
            """)
        
        op = int(input("Introdueix una opcio: "))
        if op < 1 or op > 14:
            print("La opcio no es valida, torni a elegir una opcio: ")
        else: 
            return op

def ex1(): 
    a = int(input("Introdueix un numero: "))
    b = int(input("Introdueix altre numero: "))
    if a > b:
        print("{} és major que {}".format(a,b))
    elif b > a:
        print("{} és major que {}".format(b,a))
    else:
        print("{} y {} són dos numeros iguals".format(a,b))

def ex2():
    vocal = input("Introdueix una lletra: ")
    match(vocal):
        case 'a':
            print("La lletra insertada es 'a'. Es a dir es vocal.")
        case 'e':
            print("La lletra insertada es 'e'.Es a dir es vocal.")
        case 'i':
            print("La lletra insertada es 'i'.Es a dir es vocal.")
        case 'o':
            print("La lletra insertada es 'o'.Es a dir es vocal.")
        case 'u':
            print("La lletra insertada es 'u'.Es a dir es vocal.")
        case other:
            print("No es vocal")

def ex3():
    a = []
    b = []
    for i in range(3):
        a.append (input("Introdueix una paraula: "))
    for e in a:
        b.append(len(a))
    print("Les longituds de la llsta {} són {}".format(a,b))

def ex4():
    a = []
    for e in range(1,10,2):
        a.append(e)
    print("Els 5 primers nombres impars són: {}".format(a))

def ex5():
    a = [1,2,3,4,5]
    dic = {}
    for i,e in enumerate(a):
        dic[i] = e
    print("De la llista {} hem creat el diccionari {}".format(a, dic))

def ex6(llista,a):
    b = []
    for e in llista:
        if a in e:
            b.append(e)
    print("La llista {} que conte la lletra {} són {}".format(llista,a,b))

def ex7():
    a = [2,6,8,20,32]
    c = list(map(lambda x: x+10, a))
    print(c)

def ex8():
    a = [2,6,3,4,8]
    r = [x ** 2 for x in a if x%2==1]
    print("El quadrat dels numeros impars és {}".format(r))

def ex9(): 
    a = ["Oscar", "Llordy", "GitClone"]
    c = list(map(lambda x: x[::-1], a))
    print(c)

def ex10():
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    c = zip(a,b)
    print(c)

def ex11():
    a = [1,2,3,4,5]
    b = list(filter(lambda x: x%2==1, a))
    print("Los numeros impares de la lista {} són: {}".format(a,b))


    class Ordinador():
        def __init__(self,tipus,pantalla):
            self.tipus = tipus
            self.pantalla = pantalla
        def getTipus(self):
            print(self.tipus)
        def getPantlla(self):
            print(self.pantalla)

    class Portatil(Ordinador):
        def getTipus(self):
            print("Soc un portatil")
        def getPantalla(self):
            print('15"')

    class Tablet(Ordinador):
        def getTipus(self):
            print("Soc una tablet")
        def getPantalla(self):
            print('9"')

    class Servidor(Ordinador):
        def getTipus(self):
            print("Soc un servidor")
        def getPantalla(self):
            print('21"')

    class PC(Ordinador):
        def getTipus(self):
            print("Soc un PC")
        def getPantalla(self):
            print('27"')

def ex12():
    class Ordinador():
        def __init__(self, tipus, pantalla):
            self.tipus = tipus
            self.pantalla = pantalla
        
        def getTipus(self):
            print(self.tipus)
        
        def getPantalla(self):
            print(self.pantalla)

    class Portatil(Ordinador):
        def getTipus(self):
            print("Soc un portatil")
        
        def getPantalla(self):
            print('15"')

    class Tablet(Ordinador):
        def getTipus(self):
            print("Soc una tablet")
        
        def getPantalla(self):
            print('9"')

    class Servidor(Ordinador):
        def getTipus(self):
            print("Soc un servidor")
        
        def getPantalla(self):
            print('21"')

    class PC(Ordinador):
        def getTipus(self):
            print("Soc un PC")
        
        def getPantalla(self):
            print('27"')

    llista = [Portatil('soc un portatil', '15"'), Tablet('Soc una tablet', '9"'), Servidor('Soc un servidor', '21"'), PC('Soc un PC', '27"')]
    for e in llista:
        e.getTipus()
        e.getPantalla()

def ex13():
    with open("/home/cicles/AO/TASCA-11/EXAMEN2/ex20txt", "w") as f:
        for e in range(10):
            f.writte(e)
    a = []
    with open("/home/cicles/AO/TASCA-11/EXAMEN2/ex20txt", "r") as f: 
        for e in f:
            a.append(e)
        print(a)

#Programa Principal
op = 1
while op != 14:
    op = menu()
    match(op):
        case 1:
            print("Has entrado en el ex1!")
            ex1()
        case 2:
            print("Has entrado en el ex2!")
            ex2()
        case 3:
            print("Has entrado en el ex3!")
            ex3()
        case 4:
            print("Has entrado en el ex4!")
            ex4()
        case 5:
            print("Has entrado en el ex5!")
            ex5()
        case 6:
            print("Has entrado en el ex6!")
            l = ["Hola","Adeu","Hello","bye","alt","Baix"]
            c = "a"
            ex6(l,c)
        case 7:
            print("Has entrado en el ex7!")
            ex7()
        case 8:
            print("Has entrado en el ex8!")
            ex8()
        case 9:
            print("Has entrado en el ex9!")
            ex9()
        case 10:
            print("Has entrado en el ex10!")
            ex10()
        case 11:
            print("Has entrado en el ex11!")
            ex11()
        case 12:
            print("Has entrado en el ex12!")
            ex12()
        case 13:
            print("Has entrado en el ex13!")
            ex13()
        case 14:
            print("Programa acabat, que ho passi molt be i gracies per utilitzar el programa. ")