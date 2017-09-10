"""Esta función vuelve 1 el pibote de un renglón (gauss-jordan)"""


def UnificarRenglon(tam, matriz, r):
    for j in range(tam):
        if (matriz[r][j]!=0):
            aux = matriz[r][j]
            for i in range(tam):
                matriz[r][i] = (matriz[r][i]/aux)
