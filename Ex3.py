def igual_inicial(x,a,b):
    l = list(filter(lambda y: y[0] == a.lower() or y[0] == b.upper(), x))
    return l

#PPrograma Principal
x = ['Maria', 'Manta', 'Preu', 'Ma', 'Caca']
a = 'm'
b = 'p'
print(igual_inicial(x,a,b))