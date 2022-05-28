s1 = input("Digite a primeira String: ")
s2 = input("Digite a segunda String: ")
s3 = ""

for letra in s1:
    if letra not in s2:
        s3 += letra

if s3 == "":
    print("Todos os caracteres foram removidos.")
else:
    print(s3)