#8- Faça um algorítmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou impar, e se é
#positivo ou negativo.

n=int(input('Insira um número: '))
print()

if n%2 == 0:
    num=n
    print(n)
    print('O número é par!')
    if n>= 0:
        print('O número é positivo!')
    else:
        print('O número é negativo!')
else:
    print(n)
    print('O número é impar!')
    if n>= 0:
        print('O número é positivo!')
    else:
        print('O número é negativo!')