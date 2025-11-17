import random

def escolher_palavra():
    palavras = ["foca", "tubarao", "golfinho", "arraia", "peixe", "baleia", "polvo", "lula", "orca", "tartaruga"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_descobertas = ["_" for _ in palavra]
    tentativas_restantes = 6
    letras_chutadas = set()

    print("Bem-vindo à Forca!")

    while True:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print("Letras já tentadas:", " ".join(sorted(letras_chutadas)) if letras_chutadas else "(nenhuma)")

        tentativa = input("Digite uma letra (ou 'sair' para finalizar o programa): ").strip().lower()

        if tentativa == "sair":
            print("Jogo encerrado. Até a próxima!")
            return

        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if tentativa in letras_chutadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_chutadas.add(tentativa)

        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_descobertas[i] = tentativa
            print("Parabéns! A letra está na palavra.")
        else:
            tentativas_restantes -= 1
            print("Essa letra não está na palavra, tente novamente.")

        if "_" not in letras_descobertas:
            print("Você adivinhou a palavra:", palavra)
            break

        if tentativas_restantes <= 0:
            print("\nVocê perdeu. A palavra era:", palavra)
            break

if __name__ == "__main__":
    while True:
        jogar_forca()

        resposta = input("\nQuer jogar novamente? (s/n): ").strip().lower()
        if resposta != "s":
            print("Obrigado por jogar!")
            break

