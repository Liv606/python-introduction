s1 = input("Digite a primeira String: ")
s2 = input("Digite a segunda String: ")
s3 = input("Digite a terceira String: ")
s = 0
troca = ""

for letra in s1:
    if letra in s2[s]:
        troca = troca + s3
    else:
        troca = troca + s1
    s = s + 1

print(troca)