
def busquedaBinaria(list, objetivo):
    izq = 0
    der = len(list)-1

    while izq <= der:
        medio = (izq + der) // 2
        if (list[medio] == objetivo):
            return True
        elif list[medio] < objetivo:
            izq = medio+1
        else:
            der = medio-1
    return False


numeros = [1, 3, 5, 6, 7, 9, 10, 14, 20]
# True  → solo necesita ~3-4 pasos aunque haya 9 elementos
print(busquedaBinaria(numeros, 5))
