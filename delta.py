#delta = b² -4 . a.c

print('Vamos calcular o Delta.. b² -4 . a.c')
while True:
    print()
    print('-='*20)
    a = float(input('Me informe o valor de a:  '))
    b = float(input('Me informe o valor de b:  '))
    c = float(input('Me informe o valor de c:  '))
    print('-='*20)

    b *= b
    v1 = (a*c)*-4

    if v1 < 0:
        delta = b + v1
    if v1 > 0:
        delta = b - v1
    print(f'O valor de delta é: {delta} ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja fazer mais uma operação ? ')).strip().upper()[0]
    if continuar == 'N':
        print('Te vejo daqui um tempo então...')
        break
print('Tchau')
        
