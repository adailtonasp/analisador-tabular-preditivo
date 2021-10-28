
fita = input("Digite a sentença a ser avaliada: ")
pilha = []
simbolo = []

def vAct(a,s): 
    index = actions.index(a)
    listaAcoes = actionsTable[s]
    acao = listaAcoes[index] #retorna o indice onde se encontrou o terminal
    return acao

#empilha o estado inicial
pilha.append('0')

a = fita[0]

while(True):
    s = pilha[-1] #estado do topo da pilha

    acao = vAct(a,s)

    if(acao[0] == 's'):#siginifica que a acao é um empilhamento(shift)

        pilha.append(acao[1]) #empilha o estado

        n = fita.pop(0)#remove o caracter lido da fita

        simbolo.append(n)# coloca na pilha de simbolos

        a = fita[0]#atualiza o proximo caracter de entrada

    else if(acao[0] == 'r'):#siginifica que a acao é uma reducão(reduce)

        numeroRegra = acao[1] #identifica a regra usada para fazer a reducao
        regra = grammar[numeroRegra] #regra utilizada na reducao

        #remove os ultimos n elementos da pilha de simbolo
        #sendo n a quantidade de caracteres do lado direito da regra especificada
        simbolo = simbolo[:len(simbolo) - len(regra[1])]

        #empilha o lado esquerdo da regra
        simbolo.append(regra[0])

        #remove os elementos da pilha
        pilha = pilha[:len(pilha)-len(regra[1])]

        #empilha o novo estado de acordo com a tabela de transicoes
        topo = pilha[-1]
        
        index = transitionsTable.index(regra[0])

        novoEstado = transitionsTable[topo][index]

        pilha.append(novoEstado)

        print(regra[0],"-->",regra[1])
    else if(acao == "$"):
        print("fim")
        break
    else
        print("erro")   
        break