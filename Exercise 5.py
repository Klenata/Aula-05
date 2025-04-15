num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2 == 0:
    print("0 não dá pode dividir")
    num2 = int(input("Digite o novo número: "))

div = num1/num2
print(div)