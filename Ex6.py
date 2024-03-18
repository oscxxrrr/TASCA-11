def coincideix(llista):
    a = []
    for i,e in enumerate(llista):
        if e == i:
            a.append(e)
    return a

#PP
a = [1,1,4,5,6,5,6,7,4,3]
resultado = coincideix(a)
print(resultado)
         