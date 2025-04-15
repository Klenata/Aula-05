num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
while num2 == 0:
    num2 = int(input("Não dá para dividir por 0, digite o novo número: "))
print(" ")
div = num1/num2
print(f"{div:.2f}")