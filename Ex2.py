from functools import reduce

def passar_a_numero(llista):
    b = (list(map(lambda x: str(x), llista)))
    r = reduce(lambda x,y: x+y, b)
    print(int(r))

#Programa principal 
l = [3,4,1,5]
passar_a_numero(l)