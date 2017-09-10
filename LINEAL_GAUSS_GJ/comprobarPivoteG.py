"""esta función comprueba si el pivote es un número distinto de cero(gauss)"""

def comprobarPivote(tam, matriz):
    for i in range(tam):
        for j in range(tam):
            if matriz[j][j] != 0:
                return 1
            else:
                return 0