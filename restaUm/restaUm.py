from copy import copy, deepcopy

# # BFS
def buscaLargura(estados):
    estados_new = []
    for s in estados:
        s_new = [resultado(s, a) for a in acoes(s)]
        estados_new = estados_new + s_new
    if any(atingiuObj(s) for s in estados_new)
        return solucao(estados_new)
    return buscaLargura(estados_new)

# Gera um novo estado a partir de uma ação a
def resultado(s, a):
   s_new = deepcopy(s)
   pos, acao = a
   i, j = pos
   s_new[i][j] = 'X'
   if movimentos[acao] == 'up':
       s_new[i-1][j] = 'X'
       s_new[i-2][j] = 'O'
   elif movimentos[acao] == 'left':
       s_new[i][j-1] = 'X'
       s_new[i][j-2] = 'O'
   elif movimentos[acao] == 'down':
       s_new[i+1][j] = 'X'
       s_new[i+2][j] = 'O'
   else:
       s_new[i][j+1] = 'X'
       s_new[i][j+2] = 'O'	
   return s_new

movimentos = {0:'left', 1: 'down', 2:'direita', 3:'up'}

# Retorna todas as ações possíveis de um estado s
#def acoes(s):
#    acoes = []
#    for i in range(len(s)):
#        for j in range(len(s[i])):
#            pos = (i, j)
#            for a in acoesFactiveis(s, pos): 
#                acoes.append(a)
#    return acoes

# Retorna acoes factveis para uma posicao pos em um dado estado s
def acoesFactiveis(s, pos):
    acoes = []
    i, j = pos
    if  s[i][j] != 'O':
        return acoes
    for m, n in movimentos.items():
        # Left
        if m == 0 and j-2 < len(s):
            if s[i][j-1] == 'O' and s[i][j-2] == 'X':
                a = (pos, m)
                acoes.append(a)
        # Down
        elif m == 1 and i+2 < len(s):
            if s[i+1][j] == 'O' and s[i+2][j] == 'X':
                a = (pos, m)
                acoes.append(a)
        # Right
        elif m == 2 and j+2 < len(s):
            if s[i][j+1] == 'O' and s[i][j+2] == 'X':
                a = (pos, m)
                acoes.append(a)
        # Up
        elif m == 3 and i-2 < len(s):
            if s[i-1][j] == 'O' and s[i-2][j] == 'X':
                a = (pos, m)
                acoes.append(a)    
    return acoes        
                   
# Verifica se um estado s é objetivo
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
    #printEstado(s0)
    # print(atingiuObj(s0))
       

main()

    print(bfs(s0))
