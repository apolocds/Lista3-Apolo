#Elabore um fluxograma que receba duas notas e calcule a média do aluno. Caso a média for igual ou maior a 7, o fluxograma exibe que o aluno foi aprovado. Caso a média for menor que 7, o aluno realiza uma prova final. A média de aprovação após a prova final é 5. Caso o aluno não atinja esta média, o fluxograma exibe que o aluno foi reprovado.

n1 = float(input("Digite a sua 1° nota: "))
n2 = float(input("Digite a sua 2° nota: "))

media = (n1 + n2) / 2

if media >= 7:
    print(f"Aluno aprovado com média: {media:.2f}")
elif media >= 5:
    print(f"Média {media:.2f}: é insuficiente para aprovação direta, será necessário realizar a prova final.")
    n3 = float(input("Digite a sua nota final: "))
    media_final = (n1 + n2 + n3) / 3

    if media_final >= 5:
        print(f"Aluno aprovado com média: {media_final:.2f}.")
    else:
        print(f"Aluno reprovado com média: {media_final:.2f}.")
else:
    falta = 15-n1-n2 #como a média é 5 e o cálculo vai precisar de 3 notas, 15(5*3) seria o valor total da nota necessária pra aprovação depois de dividir por 3, tirando a diferença a partir da 1° e 2° nota o programa informa ao usuário a nota necessária.
    print(f"Média {media:.2f} é insuficiente. Você precisa de mais {falta:.2f} pontos para atingit a média 5.")
    n3 = float(input("Digite a sua nota final: "))
    media_final = (n1 + n2 + n3) / 3

    if media_final >= 5:
        print(f"Aluno aprovado com média: {media_final:.2f}.")
    else:
        print(f"Aluno reprovado com média: {media_final:.2f}.")
