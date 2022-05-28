último = 5
último2 = 5
fila = list(range(1, último + 1))
fila2 = list(range(1, último2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila 1 e {len(fila2)} na fila 2\n")
    print(f"Fila 1 atual: {fila}")
    print(f"Fila 2 atual: {fila2}")
    print("Digite F para adicionar um cliente ao fim da fila 1 ou G para adicionar ao fim da fila 2,")
    print("ou A para realizar o atendimento na fila 1 e B para o atendimento na fila 2. S para sair.")
    operação = input("Operação (F, G, A, B ou S):")
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"\nCliente {atendido} atendido.")
        else:
            print("\nFila 1 vazia! Ninguém para atender.")
    elif operação == "B":
        if len(fila2) > 0:
            atendido = fila2.pop(0)
            print(f"\nCliente {atendido} atendito.")
        else:
            print("\nFila 2 vazia! Ninguém para atender.")
    elif operação == "F":
        último += 1  # Incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "G":
        último2 += 1
        fila2.append(último2)
    elif operação == "S":
        break
    else:
        print("\nOperação inválida! Digite apenas F, G, A, B ou S!")
