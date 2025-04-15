i = 0
soma = 0
quant = int(input("Digite quantos números vocÊ quer usar para tirar a média: "))
while i < quant:
    somatotal=float(input(f"Digite o {i+1}° valor: "))
    soma+=somatotal
    i+=1
media = soma/quant
print(" ")
print(media)