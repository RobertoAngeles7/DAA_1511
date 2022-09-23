def cubetas(arreglo):
    datos = max(arreglo)
    slots = len(arreglo)
    num = datos/slots
    cubetas = [[] for i in range(slots)]
    for i in range(slots):
        index = int(arreglo[i]/num)
        if index != slots:
            cubetas[index].append(arreglo[i])
        else:
            cubetas[slots - 1].append(arreglo[i])
    for i in range(len(arreglo)):
        cubetas[i] = sorted(cubetas[i])
    resultado = []
    for i in range(slots):
        resultado = resultado + cubetas[i]
    return resultado
 
 
arreglo_desordenado = [10, 5, 4, 2, 7, 22, 90, 130, 40, 54, 11, 2021]
arreglo_ordenado = cubetas(arreglo_desordenado)
print(arreglo_ordenado)