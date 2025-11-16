num = []
for contador in range(15):
    lista = int(input(f"Digite o {contador+1}º número da lista: "))
    num.append(lista)

ordenados = sorted(num)
print(f"Essa é sua lista em ordem crescente: {ordenados}")


par = 0
impar = 0
for n in num:
    if n % 2 == 0:
        par +=1
    else:
        impar +=1

print(f"A lista que você montou tem {par} números pares, e {impar} números impares.")
input("Pressione Enter para finalizar o programa.")