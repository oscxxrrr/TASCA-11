class animal():
    def __init__(self,atribut,edat):
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        pass
    def mourem(self):
        pass
    def quisoc(self):
        print("Sóc un animal ")

class Cavall(animal):
    def xerrar(self):
        print("Iiiiiiiiiiiiiiiii")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Sóc un cavall ")

class Dofi(animal):
    def xerrar(self):
        print("IchIchIchIchIch")
    def mourem(self):
        print("Em moc nedant")
    def quisoc(self):
        print("Sóc un Dofi")

class Abella(animal):
    def xerrar(self):
        print("Tttsssssssss")
    def mourem(self):
        print("Em moc volant")
    def quisoc(self):
        print("Sóc una abella")
    def picar(self):
        print("Si m'emprenyes et picare")

class Huma(animal):
    def __init__(self, nom, atribut, edat):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
    def xerrar(self):
        print("Hola! Nosaltres emprem un idioma per xerrar")
    def mourem(self):
        print("Em moc caminant")
    def quisoc(self):
        print("Sóc un Humà")

class Centaura(Huma, Cavall):
    def xerrar(self):
        print("Hola! Nosaltres emprem un idioma per xerrar")
    def mourem(self):
        print("Em moc a trot")
    def quisoc(self):
        print("Sóc una centaure")

class Fiet(Huma):
    def __init__(self, nom, atribut, edat,llpares):
        self.nom=nom
        self.atribut=atribut
        self.edat=edat
        self.pares=llpares
    def xerrar(self):
        print("Ueeeeeeeee")
    def mourem(self):
        print("Em moc gatetjant")
    def quisoc(self):
        print("Sóc un fiet")
    def nompares(self):
        for e in self.pares:
            print("e.nom")

class xou():
    def xerrar(self):
        print("Xou")
    def mourem(self):
        print("Em moc fent xou")
    def quisoc(self):
        print("Sóc un xou")

#Programa Principal
a = [Cavall("Marro","4"),Dofi("Gris","10"),Abella("Negra y Groga", "0,5"),Huma("Sibila","Cristia","7"),Centaura("Fiona","Marron","18"),Fiet("Jordi", "Moreno","9",["Fiona","Marc"]),xou()]
for e in a:
    e.xerrar()
    e.mourem()
    e.quisoc()


