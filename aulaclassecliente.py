class Cliente:
    def __init__(self,nome,email,plano):
        self.nome=nome
        self.email=email
        self.lista_planos =["basic","premium"]
        if plano in self.lista_planos:
            self.plano=plano
        else:
          raise Exception ("Plano invalido")


    # def mudar_plano(self,novo_plano):
    #     if novo_plano in self.lista_planos:
    #         self.plano = novo_plano
    #      else:
    #        print("Plano invalido ")

cliente=Cliente('lira','lira@gmail.com','basic')



print(cliente.nome)
print(cliente.plano)

