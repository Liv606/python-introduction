x1 = int(input("Digite o tamanho do primeiro lado: "))
x2 = int(input("Digite o tamanho do segundo lado: "))
x3 = int(input("Digite o tamanho do terceiro lado: "))

if x1 + x2 > x3 and x2 + x3 > x1 and x1 + x3 > x2:
    #print("É um triângulo")
    if x1 == x2 and x2 == x3 and x1 == x3:
        print("É um triângulo equilátero")
    elif x1 == x2 or x2 == x3 or x1 == x3:
        print("É um triângulo isósceles")
    else:
        print("É um triângulo escaleno")
else:
    print("Não é um triângulo")