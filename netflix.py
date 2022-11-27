# Exemplo da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print("Plano inválido")
        

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido")



cliente = Cliente("Gabriel", "gabriel.gmail.com", "basic")

print(cliente.plano)

cliente.mudar_plano("premium")
print(cliente.plano)