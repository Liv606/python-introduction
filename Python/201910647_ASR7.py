#o código não apresentou erros, mas foram colocadas linhas de prevenção

agenda = []                                                                      #lista que armazena os dados


def pede_nome():                                                                 #função solicita o nome
    return input("Nome: ")                                                       #retorna o pedido de incersão do nome


def pede_telefone():                                                             #função que solicita o telefone
    return input("Telefone: ")                                                   #retorna o pedido de incersão do telefone


def mostra_dados(nome, telefone):                                                #função mostra nome e telefone
    print(f"Nome: {nome} Telefone: {telefone}")                                  #pede a incersão do nome e telefone a ser registrado


def pede_nome_arquivo():                                                         #função solicita nome do arquivo
    return input("Nome do arquivo: ")                                            #retorna o pedido de incersão do nome do arquivo


def pesquisa(nome):                                                              #função busca nome nos dados armazenados
    mnome = nome.lower()                                                         #pega o nome em letras minúsculas
    for p, e in enumerate(agenda):                                               #busca os pelos dados inseridos na agenda
        if e[0].lower() == mnome:                                                #se o e for igual ao mnome ele retorna p
            return p                                                             #mostra o valor p
    return None                                                                  #sai do for


def novo():                                                                      #define comando novo
    global agenda                                                                #chama variavel global agenda para alteração
    nome = pede_nome()                                                           #solicita a inserção do nome
    telefone = pede_telefone()                                                   #solicita a incersão do telefone
    agenda.append([nome, telefone])                                              #adiciona nome e telefona na lista agenda


def apaga():                                                                     #define comando apaga
    global agenda                                                                #chama variável global para alteração
    nome = pede_nome()                                                           #solicita o nome da lista criada
    p = pesquisa(nome)                                                           #variável de pesquisa do nome
    if p is not None:                                                            #se p for encontrado na lista
        del agenda[p]                                                            #apaga p
    else:                                                                        #se não encontra p na lista
        print("Nome não encontrado.")                                            #retorna que p não foi encontrado


def altera():                                                                    #define comando altera
    p = pesquisa(pede_nome())                                                    #solicita nome a ser pesquisado para alteração
    if p is not None:                                                            #se p não for nulo
        nome = agenda[p][0]                                                      #busca nome na agenda
        telefone = agenda[p][1]                                                  #busca telefone na agenda
        print("Encontrado:")                                                     #retorna que p foi encontrado
        mostra_dados(nome, telefone)                                             #imprime os dados encontrados a partir da busca feita
        nome = pede_nome()                                                       #solicita novo nome
        telefone = pede_telefone()                                               #solicita novo telefone
        agenda[p] = [nome, telefone]                                             #armazena novos nome e telefone
    else:                                                                        #caso p seja nulo
        print("Nome não encontrado.")                                            #retorna que p não foi encontrado


def lista():                                                                     #define lista
    print("\nAgenda\n\n------")                                                  #imprime agenda
    for e in agenda:                                                             #repete quantas vezes for o tamanho da agenda
        mostra_dados(e[0], e[1])                                                 #imprime os dados da agenda
    print("------\n")                                                            #imprime uma linha de separação -----


def le():                                                                        #define le
    global agenda                                                                #chama variável global para alteração
    nome_arquivo = pede_nome_arquivo()                                           #pede a incersção do nome do arquivo
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:                   #comando para abrir o arquivo solicitado
        agenda = []                                                              #cria lista agenda
        for l in arquivo.readlines():                                            #retorna a lista com as linhas do arquivo
            nome, telefone = l.strip().split("#")                                #remove espaços inutilizados do início e fim e divide a string l em uma lista
            agenda.append([nome, telefone])                                      #adiciona nome e telefone de volta na lista
        arquivo.close()                                                          #foi adicionada está linha para não correr risco de erros


def grava():                                                                     #define grava
    nome_arquivo = pede_nome_arquivo()                                           #recebe o nome do arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:                   #comando para abrir o arquivo solicitado
        for e in agenda:                                                         #repete quantas vezes for o tamanho da agenda
            arquivo.write(f"{e[0]}#{e[1]}\n")                                    #salva a lista contendo nome e telefone, com separação por #
        arquivo.close()                                                          #foi adicionada está linha para não correr risco de erros


def valida_faixa_inteiro(pergunta, início, fim):                                 #define tamanho menu
    while True:                                                                  #repete enquanto for verdadeiro
        try:                                                                     #tenta o código dentro da função
            valor = int(input(pergunta))                                         #valor recebe o que foi digitado
            if início <= valor <= fim:                                           #se estiver dentro da condição executa
                return valor                                                     #retorna valor
        except ValueError:                                                       #se estiver fora da função
            print(f"Valor inválido, favor digitar entre {início} e {fim}")       #printa valor inválido inserido


def menu():                                                                      #define menu
    print("""
  1 - Novo
  2 - Altera
  3 - Apaga
  4 - Lista
  5 - Grava
  6 - Lê

  0 - Sai
""")                                                                            #printa menu
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)                    #retorna a opção escolhida


while True:                                                                     #enquanto verdadeiro
    opcao = menu()                                                              #confere opção escolhida
    if opcao == 0:                                                              #verifica se for 0
        break                                                                   #sai do programa
    elif opcao == 1:                                                            #verifica se for 1
        novo()                                                                  #executa novo()
    elif opcao == 2:                                                            #verifica se for 2
        altera()                                                                #executa altera()
    elif opcao == 3:                                                            #verifica se for 3
        apaga()                                                                 #executa apaga()
    elif opcao == 4:                                                            #verifica se for 4
        lista()                                                                 #executa lista()
    elif opcao == 5:                                                            #verifica se for 5
        grava()                                                                 #executa grava()
    elif opcao == 6:                                                            #verifica se for 6
        le()                                                                    #executa le()
