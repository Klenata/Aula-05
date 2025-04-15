pin = 1234
tentativa = 0
mensagem = "Acesso Bloqueado"
while tentativa < 3:
    senha = int(input("Qual a sua senha: "))
    if senha == pin:
        mensagem = "Acesso Liberado"
        break
    tentativa += 1
    print("Senha Incorreta")
print(mensagem)