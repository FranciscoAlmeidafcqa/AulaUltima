#crie um programa  que leia  quanto  dinheiro uma
#pessoa tem  na carteira  e mostre quantos
#dolares  ela  pode ter para comprar
#considere que o dola Us$ 1,00= R$ 3,27
real=float(input('Digite a quantidade de dinheiro em sua carteira R$ :'))
converter= real / 3.27
print(f'você tem em dorlar o seguinte valor U$ {converter:.2f}')