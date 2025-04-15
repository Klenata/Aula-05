i = 0
soma = 0
quant = int(input("Digite a quantidade de alunos na sala: "))
while i < quant:
    somatotal=float(input(f"Digite o {i+1}° valor: "))
    soma+=somatotal
    i+=1
media = soma/quant
print(" ")
print(f"A média da turma é {media:.2f}!")