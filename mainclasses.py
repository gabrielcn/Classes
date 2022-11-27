class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
    # características:
    # - cor
    # - altura
    # profundidade
    # largura

    def passar_canal(self, botao):
        if botao == "+":
            print("aumentar canal")
        elif botao == "-":
            print("diminuir canal")

    # métodos do controle remoto
    # - passar de canal
    # mexer no volume # abrir a netflix
    # desligar a tv

controle_remoto = ControleRemoto("preto", "10cm", "2cm", "2cm") # -> instancia 
#print(controle_remoto.cor)

botao = str(input("Digite: "))

controle_remoto.passar_canal(botao)

#controle_remoto2 = ControleRemoto("cinza", "10cm", "2cm", "2cm")
#print(controle_remoto2.cor)

