s1 = input("Digite a primeira String: ")
s2 = input("Digite a segunda String: ")
s3 = ""

for letra in s1:
    if letra in s2 and letra not in s3:
        s3 += letra

if s3 == "":
    print("Caracteres comuns não encontrados.")
else:
    print(s3)