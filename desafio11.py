#faça um programa que leia  a largura e a autura  de uma
#parede  em metros . calcule a sua area  e a quantidade de tinta
#necessaria  para pintar-la , Sabendo  que cada litro
#de tinta  pinta uma area de m²

largura=float(input('Digite a largura '))
altura=float(input('Digite a Altura '))
area =largura* altura
tinta =area/2
print(f"sua parede tem a dimensao de {altura} x{largura}  e sua area é de {area:.0f}m² ")
print(f' A quantidade de tinta para pintar {area} de area e de :{tinta} litros de tinta ')