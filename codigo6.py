def solicitar_emprestimo():
    try:
        # entrada da renda do usuário
        renda = float(input("Digite sua renda mensal (em R$): "))
        if renda <= 0:
            print("A renda deve ser um valor positivo.")
            return

        # verifica faixa de renda e define o limite de empréstimo
        if renda < 1000:
            limite_emprestimo = 5000
        elif 1000 <= renda <= 5000:
            limite_emprestimo = 10000
        else:
            limite_emprestimo = 15000

        valor_desejado = float(input("Digite o valor do empréstimo desejado (em R$): "))
        if valor_desejado <= 0:
            print("O valor do empréstimo deve ser positivo.")
            return

        # verificando se o valor solicitado está dentro do limite
        if valor_desejado <= limite_emprestimo:
            print(f"Empréstimo aprovado! Você retirou R${valor_desejado:.2f}.")
        else:
            print(f"Empréstimo negado. O valor solicitado excede seu limite de R${limite_emprestimo:.2f}.")

    except ValueError:
        print("Entrada inválida. Digite valores numéricos válidos.")

solicitar_emprestimo()