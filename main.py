import random

# Lista de palavras
palavras = ["python", "computador", "programacao", "jogo", "teclado"]

# Escolhe uma palavra aleatória
palavra = random.choice(palavras)

letras_descobertas = ["_"] * len(palavra)
tentativas = 6
letras_usadas = []

print("🎮 Bem-vindo ao Jogo da Forca!")

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Tentativas restantes:", tentativas)
    print("Letras usadas:", ", ".join(letras_usadas))

    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já tentou essa letra!")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        print("✅ Acertou!")
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
    else:
        print("❌ Errou!")
        tentativas -= 1

if "_" not in letras_descobertas:
    print("\n🎉 Parabéns! Você descobriu a palavra:", palavra)
else:
    print("\n💀 Você perdeu! A palavra era:", palavra)