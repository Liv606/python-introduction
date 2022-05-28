import numpy as np

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
pares = []

vmax = max(lista)
vmin = min(lista)
for valor in lista:
    if valor % 2 == 0:
        pares.append(valor)
ocorrencias = lista.count(12)
media = np.mean(lista)
negativo = sum(n for n in lista if n < 0)

print()
print("Lista: ", lista)
print()
print("O maior elemento é: ", vmax)
print("O menor elemento é: ", vmin)
print("Os valores pares da lista são: ", pares)
print("O número de ocorrências do primeiro elemento da lista é: ", ocorrencias)
print("A média dos valores da lista é: ", media)
print("A soma dos negativos é: ", negativo)
print()