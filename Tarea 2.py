filas = int(input("Introduce numero de filas: "))
columnas = int(input("Introduce numero de columnas: "))

matriz = []
for i in range(filas):
    matriz.append([0] * columnas)

mayor = None  # Mayor valor encontrado hasta el momento.
fila = 0      # Fila de `mayor`
columna = 0   # Columna de `mayor`
for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = int(input("Fila {}, columna {} : ".format(i + 1, j + 1)))
        if mayor is None: # Inicializamos mayor aqui.
            mayor = matriz[i][j] - 1
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
            fila = i
            columna = j

print("El numero mayor de habitantes es: ")
print(mayor)
print("Puerta", fila + 1, ", Piso", columna + 1)
print("La matriz es:")
print(matriz)


