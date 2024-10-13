def multiplicar_linhas(linha: list, constante: float):
    return [linha[i] * constante for i in range(len(linha))]
    


def zerar_elementos_abaixo(matriz: list, i: int, j: int):
    
    degrau = matriz[i][j]

    if degrau != 0:
        for k in range(i+1, len(matriz)):
            if matriz[k][j] == 0:
                pass
            else:
                constante = matriz[k][j]



def receber_matriz() -> list:
    matriz = input("Digite a matriz aumentada (números separados por espaços são da mesma linha e a vírgula é a quebra de linha)")
    matriz = matriz.split(",")
    for i, item in enumerate(matriz):
        item = item.strip()
        item = list(map(float, item.split()))
        matriz[i] = item
    return matriz


def linhas_validas(matriz:list) -> bool:

    """
    verifica validade das linhas
    """

    tamanho = len(matriz[0])
    if tamanho < 2: #verifica se a matriz pode ser aumentada(pelo menos 1 coluna resultado e outra dos coeficientes)
        return False
    for i in range(1, len(matriz)): #verifica se todas as linhas da matriz possuem o mesmo número de elementos
        if len(matriz[i]) != tamanho: 
            return False
    return True


def eh_linha_nao_nula(linha: list) -> bool:

    """
    verifica se a linha é composta apenas por elementos 0
    """

    saldo = 0
    for item in linha: saldo += item
    return bool(saldo)

matriz = receber_matriz()


while not eh_linha_nao_nula(matriz[0]):
    aux = matriz[0]
    del matriz[0]
    matriz.append(aux)
    

for i in range(len(matriz)):
    j=0
    while matriz[i][j] == 0:
        j += 1
    matriz[i] = dividir(matriz[i], matriz[i][j])

if matriz[i][j] != 0:
    k = 



