from copy import copy, deepcopy

# # BFS
# def buscaLargura(estados):
#     estados’ = []
#     for s in estados:
#         s’ = [resultado(s, a) for a in acoes(s)]
#         estados’ = estados’ + s’
#     if any(atingiuObj(s) for s in estados’)
#         return solucao(estados’)
#     return buscaLargura(estados’)

def resultado(s, a):
    pass

movimentos = {0:'left', 1: 'down', 2:'direita', 3:'up'}

def acoes(s):
    acoes = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            pos = (i, j)
            a = acoesFactiveis(s, pos)
            if a:
                acoes.append(a)
    return acoes

#retorna acoes factveis para uma posicao pos em um dado estado s
def acoesFactiveis(s, pos):
    acoes = []
    i, j = pos
    if  s[i][j] != 'O':
        return acoes
    for m, n in movimentos.items():
        # Left
        if m == 0 and j-2 < len(s):
            if s[i][j-1] == 'O' and s[i][j-2] == 'X':
                a = pos, n
                acoes.append(a)
        # Down
        elif m == 1 and i-2 < len(s):
            if s[i-1][j] == 'O' and s[i-2][j] == 'X':
                a = pos, n
                acoes.append(a)
        # Right
        elif m == 2 and j+2 < len(s):
            if s[i][j+1] == 'O' and s[i][j+2] == 'X':
                a = pos, n
                acoes.append(a)
        # Up
        elif m == 3 and i+2 < len(s):
            if s[i+1][j] == 'O' and s[i+2][j] == 'X':
                a = pos, n
                acoes.append(a)    
    return acoes
            
                
            




def atingiuObj(s):
    contaPeca = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 'O': 
                contaPeca += 1
                if contaPeca > 1:
                    return False
    return True

# Printa o estado(Tabuleiro)
def printEstado(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            print(s[i][j], end=' ')
        print()

def main():

    # Estado inicial do tabuleiro
    # '-' = espaços inválidos
    # 'O' = espaços que tem uma peça
    # 'X' = espaços vazios
    s0 = [['-', '-', 'O', 'O', 'O', '-', '-'],
          ['-', '-', 'O', 'O', 'O', '-', '-'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'X', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
          ['-', '-', 'O', 'O', 'O', '-', '-'],
          ['-', '-', 'O', 'O', 'O', '-', '-']]
    
    #printEstado(s1)
    printEstado(s0)
    # print(atingiuObj(s0))
    print(acoes(s0))
    
main()