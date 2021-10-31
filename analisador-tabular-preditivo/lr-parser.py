# Trabalho de Implementação - Construção de Compiladores - 2021
# Adailton Palhano, Felipe Barros e Maria Theresa.
import os
import csv

goAhead = False  # indicar se o usuário deve prosseguir

# Variáveis utilizadas no programa
countStates = 0  # Quantidade de Estados
countActions = 0  # Quantidade de Ações
countTransitions = 0  # Quantidade de Transições
grammar = []  # Gramática inserida pelo Usuário
actionsTable = []  # Tabela de Ações
actions = []  # Terminais das Ações
transitions = []  # Váriaveis das transições
sentence = ""  # Sentença a ser analisada
statesStack = []  # Pilha de estados
simbolsStack = []  # Pilha de símbolos já processados

# 1. Entrada dos Dados iniciais
while(not goAhead):
    print("------------ Preenchimento dos Dados Iniciais ------------")
    try:
        countStates = int(input("Insira a quantidade de estados: "))

        countActions = int(input("Insira a quantidade de ações: "))

        countTransitions = int(input("Insira a quantidade de transições: "))

        countRules = int(input("Insira a quantidade de regras da gramática: "))

        goAhead = input(
            "\nPressione 1 para continuar. Qualquer outra tecla para voltar: ")
        goAhead = goAhead == "1"
    except:
        input(
            "\nVocê inseriu algum dado incorreto. Pressione qualquer tecla para repetir: ")
        goAhead = False
    os.system('cls' if os.name == 'nt' else 'clear')

# 2. Preenchimento da tabela
# - Dividimos o preenchimento da tabela em duas partes: tabela de ações e tabela de transições.
# - A entrada de cada linha, em ambos os casos, consiste nos elementos separados por vírgula.
# - Entrada com '@' siginifca uma ação ou transição vazia.

# 2.1. Preenchimento da tabela de ações
goAhead = False  # Indicar se o usuário deve prosseguir

while(not goAhead):
    print("------- Preenchimento dos Dados da Tabela de Ações -------")
    print("* entradas separadas por vírgula. @ para entradas vazias *\n")
    try:
        actions = input(
            f"Insira os variáveis({countActions}) das ações: ").split(',')

        actionLine = []
        for i in range(countStates):
            actionLine = input(
                f"Insira as ações({countActions}) da linha {i+1}: ")
            actionLine = actionLine.split(',')
            actionsTable.append(actionLine)

        goAhead = input(
            "\nPressione 1 para continuar. Qualquer outra tecla para repetir: ")
        goAhead = goAhead == "1"
    except:
        input(
            "\nVocê inseriu algum dado incorreto. Pressione qualquer tecla para repetir: ")
        goAhead = False
    os.system('cls' if os.name == 'nt' else 'clear')

# 2.2. Preenchimento da tabela de transições
# - Dividimos o preenchimento da tabela em duas partes: tabela de ações e tabela de transições.
# - A entrada de cada linha, em ambos os casos, consiste nos elementos separados por vírgula.
# - Entrada com '@' siginifca uma ação ou transição vazia.

goAhead = False  # Indicar se o usuário deve prosseguir
transitionsTable = []  # Tabela de transições
while(not goAhead):
    print("-------- Preenchimento dos Dados da Tabela de Transições -----")
    print("*   entradas separadas por vírgula. @ para entradas vazias   *\n")
    try:
        transitions = input(
            f"Insira as variáveis({countTransitions}) das transições: ").split(',')

        transitionLine = []
        for i in range(countStates):
            transitionLine = input(
                f"Insira as transições({countTransitions}) da linha {i+1}: ")
            transitionLine = transitionLine.split(',')
            transitionsTable.append(transitionLine)

        goAhead = input(
            "\nPressione 1 para continuar. Qualquer outra tecla para repetir: ")
        goAhead = goAhead == "1"
    except:
        input(
            "\nVocê inseriu algum dado incorreto. Pressione qualquer tecla para repetir: ")
        goAhead = False
    os.system('cls' if os.name == 'nt' else 'clear')

# 3. Preenchimento da gramática
# - O preenchimento da gramática utiliza os caracteres '->' para separar os lados esquerdo e direito
# - O espaço deve ser utilizado para separar cada elemento do lado esquerdo
# - Exemplo: E -> E + T

goAhead = False
while(not goAhead):
    print("---------------------- Preenchimento da Gramática ----------------------")
    print("*          regra separadas por ->. espaços devem ser utilizados        *\n")
    try:
        for i in range(countRules):
            rule = input(f"Insira a regra {i+1}: ")

            rule = rule.split('->')
            # Removendo espaçoes em branco
            rule[0] = rule[0].rstrip()
            rule[1] = rule[1].strip()
            rule[1] = rule[1].split(" ")
            grammar.append(rule)

        goAhead = input(
            "\nPressione 1 para continuar. Qualquer outra tecla para repetir: ")
        goAhead = goAhead == "1"
    except:
        input(
            "\nVocê inseriu algum dado incorreto. Pressione qualquer tecla para repetir: ")
        goAhead = False
    os.system('cls' if os.name == 'nt' else 'clear')


# 4. Entrada da sentença
# - O espaço deve ser utilizado para separar cada elemento da sentença
# - Exemplo: id * id + id

sentence = input("Insira a sentença a ser avaliada: ")
sentence = sentence.split(" ")
sentence.append("$")  # anexa $ ao final da entrada

print()
print()

# 5. Análise Preditiva
# Retorna uma ação da tabela, a partir de uma dada variável de ação(a) e estado(s)
listaDerivacao = []

def getCurrentAction(a, s):
    actionIndex = actions.index(a)
    actionsRow = actionsTable[int(s)]
    return actionsRow[actionIndex]  # retorna a ação encontrada


# Empilha o estado inicial
statesStack.append('0')

# Recebe o primeiro símbolo da sentença
firstEle = sentence[0]

print("pilha", "\t", "simbolo", "\t", "entrada", "\t", "acao\n")

while(True):
    currentState = statesStack[-1]  # Estado do topo da pilha

    currentAction = getCurrentAction(firstEle, currentState)

    print(statesStack, "\t", simbolsStack, "\t", sentence, "\t", currentAction)

    listaDerivacao.append([statesStack,simbolsStack,sentence,currentAction])

    if(currentAction[0] == 's'):  # Significa que a ação é um empilhamento (shift)

        statesStack.append(currentAction[1:])  # Empilha o estado

        processedSimbol = sentence.pop(0)  # Remove o simbolo lido da fita

        # Adiciona na pilha de simbolos já processados
        simbolsStack.append(processedSimbol)

        firstEle = sentence[0]  # Atualiza o proximo caracter de entrada

    elif (currentAction[0] == 'r'):  # Siginifica que a acao é uma reducão(reduce)

        # Identificar gancho
        # Identifica a regra usada para fazer a reducao
        ruleNumber = int(currentAction[1:])
        rule = grammar[ruleNumber - 1]  # Regra utilizada na reducao

        # Remove os ultimos n elementos da pilha de símbolos
        # Sendo n a quantidade de caracteres do lado direito da regra especificada
        simbolsStack = simbolsStack[:len(simbolsStack) - len(rule[1])]

        #empilha o lado esquerdo da regra
        simbolsStack.append(rule[0])

        # Remove os elementos da pilha
        statesStack = statesStack[:len(statesStack)-len(rule[1])]

        # Empilha o novo estado de acordo com a Tabela de Transicoes
        top = statesStack[-1]
        index = transitions.index(rule[0])
        newState = transitionsTable[int(top)][index]
        statesStack.append(newState)

        #print(rule[0],"->",rule[1])

    elif(currentAction == "$"):
        print("Fim")
        with open('result.csv', 'w', newline='') as csvfile:
            newFile = csv.writer(csvfile, delimiter=';')
            newFile.writerow(['Pilha', 'Simbolo', 'Entrada', 'Acao'])
            for i in listaDerivacao:
                newFile.writerow([i[0],i[1],i[2],i[3]])
            # newFile.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        break
    else:
        print("Erro")
        break
