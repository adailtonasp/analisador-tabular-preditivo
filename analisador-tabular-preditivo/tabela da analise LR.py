 #quantidade de estados
 #quantidades de terminais
 #quantidades de transicoes
 #quantidade de regras da gramática 

countState = int(input("Digite a quantidade de estados:"))

states = range(countState)

countAction = int(input("Digite a quantidade de ações:"))

actions = []
actionLine = []

#o usuario deve entrar com uma tabela utilizando ',' para separar os elementos
#de uma mesma linha
for i in range(0,countAction):
    actionLine = input("Entra com a tabela de acoes:\n<Utilize ',' para separar elementos de uma mesma linha>\n<Entre @ para ação vazia>\n")
    actionLine = actionLine.split(',')
    print(actionLine)
    actions.append(actionLine)

# countTransition = input("Digite a quantidade de transicoes:")

# transitions = []

# for i in range(0,countTransition):
#     action.append(input("Digite as transicoes:"))

