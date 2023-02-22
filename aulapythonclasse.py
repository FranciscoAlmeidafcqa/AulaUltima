class ControleRemoto:
   def __init__(self, cor,altura,profundidade,largura):
       self.cor=cor
       self.altura=altura
       self.profundidade=profundidade
       self.largura=largura

controle_remoto=ControleRemoto("preto","10","2cm","2cm")
print(controle_remoto.cor)

controle_remoto2=ControleRemoto("Branco","10","2cm","2cm")
print(controle_remoto2.cor)
