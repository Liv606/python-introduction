n = int(input("Digite o número a ser verificado: "))

divs = 0


for div in range(1, n):
    if n % div == 0:
        divs = divs + 1

if divs > 1 or n == 1 or n == 0:
  print("Não é primo")
else:
  print("É primo")