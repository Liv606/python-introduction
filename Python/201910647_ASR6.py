print("")
print("      Jogo da Velha")
print("")

tabela ="""               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
\n"""

posicoes = [
       None,
      (5, 1),
      (5, 5), 
      (5, 9), 
      (3, 1), 
      (3, 5), 
      (3, 9), 
      (1, 1), 
      (1, 5), 
      (1, 9), 
    ]

ganhar = [
          [ 1, 2, 3], 
          [ 4, 5, 6],
          [ 7, 8, 9],
          [ 7, 4, 1], 
          [ 8, 5, 2],
          [ 9, 6, 3],
          [ 7, 5, 3], 
          [ 1, 5, 9]
        ]

jogo = []
for linha in tabela.splitlines():
    jogo.append(list(linha))

jogador = "X" 
jogando = True
jogadas = 0 
while True:
    for t in jogo:  
        print("".join(t))
    if not jogando: 
        break
    if jogadas == 9:
        print("       Deu velha!\n")
        break
    jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
    print("")
    if jogada<1 or jogada>9:
        print("     Posição inválida\n")
        continue

    if jogo[posicoes[jogada][0]][posicoes[jogada][1]] != " ":
        print("     Posição ocupada\n");
        continue

    jogo[posicoes[jogada][0]][posicoes[jogada][1]] = jogador

    for p in ganhar:
        for x in p:
            if jogo[posicoes[x][0]][posicoes[x][1]] != jogador:
                break
        else:
            print("   O jogador %s ganhou!\n "%(jogador))
            jogando = False
            break
    jogador = "X" if jogador == "O" else "O"
    jogadas +=1 