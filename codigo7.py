def parouimpar():
    try:
        # entrada do número >inteiro<
        numero = int(input("Digite um número inteiro: "))
        
        # verificação
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

parouimpar()
