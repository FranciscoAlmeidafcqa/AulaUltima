#faça um algoritimo que leia o preço de um  produto
#e mostre seu novo preço. com 5% de desconto

produto =float(input('Digite o valor do Produto ?  R$:'))
desconto = produto - produto *(5/100)
print(f'O desconto do produto é de {desconto}')