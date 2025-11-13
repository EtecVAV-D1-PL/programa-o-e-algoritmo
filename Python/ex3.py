import math

n1 = int(input("Digite um número inteiro: "))

if n1 < 0:
    print("Seu número é inválido, pois não podemos calcular a raiz quadrada de um número negativo.")
else:
   
    r1 = math.sqrt(n1)
    print(f"A raiz quadrada do seu número é {r1}")

input('Pressione Enter para finalizar o programa.')
