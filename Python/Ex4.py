n1 = float(input('informe sua primeira nota: '))
n2 = float(input('informe sua segunda nota: '))


m1 = (n1 + n2) / 2


if 0.0 <= n1 <= 10.0 and 0.0 <= n2 <= 10.0:
   print(f'Sua média é {m1}')
else:
    print('Uma de suas notas é invalida. Digite valores entre 0.0 e 10.0.')

input('pressiona Enter para finalizar o programa.')