"""esta función comprueba si el pivote es un número igual a uno o diferente de cero (gauss-jordan) """

def comprobarPivote(tam, matriz):
    for i in range(tam):
        for j in range(tam):
            if matriz[j][j] == 1:
                return 1
            else:
                return 0
