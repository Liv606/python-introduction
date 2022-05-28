s1 = input("Digite a String: ")

cont = {}

for letra in s1:
    cont[letra] = cont.get(letra, 0) + 1

for chave, valor in cont.items():
    print(f"{chave}: {valor}x")