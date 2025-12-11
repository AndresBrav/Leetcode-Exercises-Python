# Búsqueda binaria (el ejemplo clásico de O(log n))
def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return True
        elif lista[medio] < objetivo:
            izquierda = medio + 1      # descarta la mitad izquierda
        else:
            derecha = medio - 1        # descarta la mitad derecha

    return False


# Uso (¡lista ordenada!)
numeros = [1, 3, 5, 6, 7, 9, 10, 14, 20]
# True  → solo necesita ~3-4 pasos aunque haya 9 elementos
print(busqueda_binaria(numeros, 7))
# print(busqueda_binaria(numeros, 15))  # False
