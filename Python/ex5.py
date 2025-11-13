entrada = input("Digite os números separados por espaço: ")


n = list(map(float, entrada.split()))


print(f"Sua lista de números: {n}")


maior = max(n)
print(f"O maior número de sua lista: {maior}")

input("Pressione Enter para finalizar o programa.")
