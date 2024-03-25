import os

companys = ["Fede", "Pepe", "Jordi", "Ayoub", "Marc", "Hugo", "Joan", "Leiner", "Claudia", "Ian", "Sergi", "Anas", "Paula", "David", "Pisha","Selu","Joselu"]
os.mkdir("/home/cicles/AO/PHYTON/Prova1")
os.chdir("/home/cicles/AO/PHYTON/Prova1")
with open("Ex12.txt","w") as f:
    print("Fitxer creat correctament!")
    for e in companys:
        f.write(e+"\n")

professors = ["Joan", "David", "Fela", "Lluis", "Pep"]
with open("/home/cicles/AO/PHYTON/Prova1/Ex12.txt","a+") as f:
    for e in professors:
        f.write(e+"\n")

a = []
with open("/home/cicles/AO/PHYTON/Prova1/Ex12.txt", "r") as f:
    for e in f:
        c = e.split("\n")
        a.append(c[0])
print(a)