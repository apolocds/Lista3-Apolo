luz = float(input("Digite o valor da conta de luz: "))
agua = float(input("Digite o valor da conta de água: "))
internet = float(input("Digite o valor da conta de internet: "))

contas_basicas = luz + agua + internet

fatura = float(input("Digite o valor da fatura: "))

despesas = contas_basicas + fatura

# loop para adicionar despesas
while True:
    print("\nDeseja adicionar uma nova despesa? \n[1] Sim\n[2] Não")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome_despesa = input("Digite o nome da despesa: ")
        valor_despesa = float(input(f"Digite o valor da despesa de {nome_despesa}: "))
        despesas += valor_despesa  # adiciona a nova despesa ao total
    elif opcao == "2":
        break
    else:
        print("Opção inválida. Por favor, escolha [1] para Sim ou [2] para Não.")

saldo = float(input("Digite o seu saldo: "))

if saldo > despesas:
    resto = saldo - despesas
    print(f"Com as despesas pagas, seu saldo restante é: {resto}.")
else:
    debito = despesas - saldo
    print(f"O seu saldo é insuficiente, faltam {debito} para pagar a despesa.")
