import random

def executar_musica():
    def entrada(pergunta):
        while True:
            try:
                resposta = int(input(pergunta))
                if resposta in [1, 2]:
                    return resposta == 1
                else:
                    print("\nEntrada inválida. Escolha [1] para Sim ou [2] para Não.")
            except ValueError:
                print("\nEntrada inválida. Digite um número válido.")

    # perguntas
    usuario_premium = entrada("\nVocê é um usuário premium?\n[1] Sim\n[2] Não\nEscolha: ")
    musica_baixada = entrada("\nA música está baixada no dispositivo?\n[1] Sim\n[2] Não\nEscolha: ")
    conectado_internet = entrada("\nO dispositivo está conectado à internet?\n[1] Sim\n[2] Não\nEscolha: ")

    if usuario_premium:
        if conectado_internet or musica_baixada:
            print("\nReproduzindo a música escolhida!")
        else:
            print("\nErro: Não é possível reproduzir a música. Conecte-se à internet ou baixe a música no dispositivo.")
    else:
        print("\nVocê não pode reproduzir músicas específicas no modo gratuito.")
        print("\nTocando uma playlist do artista no modo aleatório...")
        
        # playlist: Blonde :D
        playlist = [
            "Nikes",
            "Ivy",
            "Pink + White",
            "Skyline to",
            "White Ferrari",
        ]
        musica_aleatoria = random.choice(playlist)
        print(f"\nTocando agora: {musica_aleatoria}")

executar_musica()
