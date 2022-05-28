import numpy as np

ExA = np.array([[12,9,4,1],[11,5,8,1],[1,2,3,1]])
ExC = ExA

print("ExC = ")
print(ExC)

lc = int(input("Digite a linha que deseja utilizar da matriz C: "))
cc = int(input("Digite a coluna que deseja utilizar da matriz C: "))

mdlC = ExC[lc,:].mean()
mdcC = ExC[:,cc].mean()
dvlC = ExC[lc,:].std()
dvcC = ExC[:,cc].std()

print("(ExC)Média linha ", lc, ": ", mdlC)
print("(ExC)Média coluna ", cc, ": ", mdcC)
print("(ExC)Desvio padrão linha ", lc, ": ", dvlC)
print("(ExC)Desvio padrão coluna ", cc, ": ", dvcC)