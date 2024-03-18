def llegir_fitxers(m):
    a = []
    with open (m,"r") as f:
        for e in f:
            c = e.split("\n")
            a.append(c[0])
    print(a)

def afegir(m,llista):
    with open(m,"a+") as f:
        for e in llista:
            f.write(e+ "\n")


#PPrincipal
fitxer = "/home/cicles/AO/PHYTON/Ex11.txt"
llista = ["Fede", "Pepe", "Jordi", "Ayoub", "Marc"]
afegir(fitxer,llista)
llegir_fitxers(fitxer)
