import numpy as np

#EX1
print("EX 1:")
print()

s1 = input("Digite a String: ")

cont = {}

for letra in s1:
    cont[letra] = cont.get(letra, 0) + 1

for chave, valor in cont.items():
    print(f"{chave}: {valor}x")

print()

#EX2
print("EX 2:")
print()

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posicao = segunda.find(letra)
        if posicao != -1:
            resultado += terceira[posicao]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(f"Os caracteres {segunda} foram substituidos por "
              f"{terceira} em {primeira}, gerando: {resultado}")
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")

print()

#EX3
print("EX 3:")
print()

primeira = []
segunda = []
while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar):"))
    if e == 0:
        break
    primeira.append(e)
while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar):"))
    if e == 0:
        break
    segunda.append(e)
terceira = []
duas_listas = primeira[:]
duas_listas.extend(segunda)
x = 0
while x < len(duas_listas):
    y = 0
    while y < len(terceira):
        if duas_listas[x] == terceira[y]:
            break
        y = y + 1
    if y == len(terceira):
        terceira.append(duas_listas[x])
    x = x + 1
x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x = x + 1


print()

#EX4
print("EX 4:")
print()

ExA = np.array([[12,9,4,1],[11,5,8,1],[1,2,3,1]])

print("ExA = ")
print(ExA)

lc = int(input("Digite a linha que deseja utilizar da matriz A: "))
cc = int(input("Digite a coluna que deseja utilizar da matriz A: "))

mdlA = ExA[lc,:].mean()
mdcA = ExA[:,cc].mean()
dvlA = ExA[lc,:].std()
dvcA = ExA[:,cc].std()

print("Média linha ", lc, ": ", mdlA)
print("Média coluna ", cc, ": ", mdcA)
print("Desvio padrão linha ", lc, ": ", dvlA)
print("Desvio padrão coluna ", cc, ": ", dvcA)

print()

#EX5
print("EX 5:")
print()

Set1 = {'A', 'B', 'C', 'D'}
Set2 = {'C', 'D', 'E', 'F'}
Set3 = {}
Set4 = {}
Set5 = {}

print("Set1 = ", Set1)
print("Set2 = ", Set2)

Set3 = Set1 | Set2
print("Set3 = ", Set3)
Set3 = Set1.union(Set2)
print("Set3 = ", Set3)

Set4 = Set1 & Set2
print("Set4 = ", Set4)
Set4 = Set1.intersection(Set2)
print("Set4 = ", Set4)

Set5 = Set1 - Set2
print("Set5 = ", Set5)
Set5 = Set1.difference(Set2)
print("Set5 = ", Set5)