def zerar_item_pivo(linha_pivo: list, linha_a_zerar: list, constante: float) -> list:
    """
    subtrai uma linha por uma constante * linha pivô
    linha_pivo = linha que terá os elementos zerados abaixo

    isso zera o item abaixo do pivô (degrau) da escadinha


    """
    linha_pivo = [linha_pivo[k] * constante for k in range(len(linha_pivo))]
    return [linha_a_zerar[k] - linha_pivo[k] for k in range(len(linha_pivo))]


def dividir_linha(linha: list, constante: float):
    return [linha[i] / constante for i in range(len(linha))]

    


def zerar_elementos_abaixo(matriz: list, i: int, j: int, reverse: bool = False):
    
    degrau = matriz[i][j] # degrau -> parte da escadinha
    linha_degrau = matriz[i] 
    if reverse:
        inicio = i - 1
        fim = -1
        passo = -1
    else:
        inicio = i+1
        fim = len(matriz)
        passo = 1
    
    for k in range(inicio, fim, passo): # percorrer os itens abaixo do degrau
        if matriz[k][j] == 0: # verifica se o item abaixo já está zerado 
             pass
        else:
            print(matriz[k][j])
            constante = matriz[k][j] / degrau
            matriz[k] = zerar_item_pivo(linha_degrau, matriz[k], constante)
    return matriz
    


def receber_matriz() -> list:
    matriz = input("Digite a matriz aumentada (números separados por espaços são da mesma linha e a vírgula é a quebra de linha)")
    matriz = matriz.split(",")
    for i, item in enumerate(matriz):
        item = item.strip()
        item = list(map(float, item.split()))
        matriz[i] = item
    return matriz


def linhas_validas(matriz: list) -> bool:

    """
    verifica validade das linhas
    """

    tamanho = len(matriz[0])
    if tamanho < 2: # verifica se a matriz pode ser aumentada(pelo menos 1 coluna resultado e outra dos coeficientes)
        return False
    for i in range(1, len(matriz)): # verifica se todas as linhas da matriz possuem o mesmo número de elementos
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


def eh_coluna_nao_nula(matriz: list, j: int) -> bool:

    """
    verifica se a coluna i da matriz recebida é não nula
    """
    saldo = 0

    for i in range(len(matriz)): saldo += matriz[i][j]
    return bool(saldo)
        

matriz = receber_matriz()
        
i=0
for i in range(len(matriz[i])): # deleta as colunas totalmente nulas
    if not eh_coluna_nao_nula(matriz, i): # contraintuitivo, pq i vira j
        for j in range(len(matriz)):
            del matriz[j][i]

#tem que criar uma função de verificação da coluna junto à matriz das incógnitas



for i in range(len(matriz)): #deleta as linhas totalmente nulas
    if not eh_linha_nao_nula(matriz[i]):
        del matriz[i]
    

i=0
j=0

# transforma a matriz em uma triangular superior, com os itens da escada sendo iguais a 1
while i < len(matriz):
    while j < len(matriz[i]) - 1:
        if matriz[i][j] != 0:
            matriz = zerar_elementos_abaixo(matriz, i, j)
            matriz[i] = dividir_linha(matriz[i], matriz[i][j])
            i += 1
            j += 1
            break
        
        else:
            matriz.append(matriz[i])
            del matriz[i]


i = len(matriz) - 1
j = len(matriz[0]) - 2
print("vamo la")
while i > 0:
    matriz[i] = zerar_elementos_abaixo(matriz, i, j, reverse = False)
    i -= 1
    j -= 1

print(matriz)




