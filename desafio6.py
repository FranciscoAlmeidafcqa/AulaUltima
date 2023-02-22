# crie um algoritimo que leia  um numero e
#mostre o seu dobro  e o seu triplo
# e diga qua é sua raiz quadrada
num =int(input('Digite um numero :'))
dobro = num *2
triplo = num *3
raiz = num**(1/2)
print(f'O numero digitado é :{num}\n o dobro desse numero é:{num*2} \n '
      f'o Triplo desse umero é: {num* 3}\n'
      f' a raiz desse numero é :{num **(1/2)}')

print(f'O Dobro é :{dobro}\n'
      f'o triplo é :{triplo}\n'
      f'a raiz e: {raiz:.2f}')
