u,i=[float(x) for x in input("Insira dois números inteiros: ").split()]

while u%i!=0:
    u,i=i,u%i
print(f'{i:.1f}')