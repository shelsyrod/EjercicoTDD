def menor(arreglo):
    menor = arreglo[0]
    for i in arreglo:
        if i < menor:
            menor = i
    return menor


print(menor([1,2,3,4]))