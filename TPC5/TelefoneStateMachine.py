class TelefoneStateMachine:
    def __init__(self):
        self.state = "off"
        self.saldo = 0
        self.numero_discado = ""
        self.moedas_inseridas = []
        self.moedas_validas = [5, 10, 20, 50, 100, 200]

    def inserir_moedas(self, valores):
        for valor in valores:
            if valor not in self.moedas_validas:
                print("maq: " + str(valor) + "c - moeda inválida; saldo = " + self.formatar_moedas(self.saldo))
            else:
                self.moedas_inseridas.append(valor)
                self.saldo += valor / 100
        print("maq: saldo = " + self.formatar_moedas(self.saldo))

    def discar_numero(self, numero):
        self.numero_discado = numero
        if self.numero_discado.startswith("601") or self.numero_discado.startswith("641"):
            print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
            self.numero_discado = ""
            self.state = "ocupado"
        elif self.numero_discado.startswith("00"):
            if self.saldo >= 1.5:
                self.saldo -= 1.5
                print("maq: Chamada internacional realizada. Saldo restante = " + self.formatar_moedas(self.saldo))
                self.state = "ocupado"
            else:
                print("maq: Saldo insuficiente para chamada internacional. Saldo = " + self.formatar_moedas(self.saldo))
                self.numero_discado = ""
                self.state = "esperando"
        elif self.numero_discado.startswith("2"):
            if self.saldo >= 0.25:
                self.saldo -= 0.25
                print("maq: Chamada nacional realizada. Saldo restante = " + self.formatar_moedas(self.saldo))
                self.state = "ocupado"
            else:
                print("maq: Saldo insuficiente para chamada nacional. Saldo = " + self.formatar_moedas(self.saldo))
                self.numero_discado = ""
                self.state = "esperando"
        elif self.numero_discado.startswith("800"):
            print("maq: Chamada verde realizada. Saldo restante = " + self.formatar_moedas(self.saldo))
            self.state = "ocupado"
        elif self.numero_discado.startswith("808"):
            if self.saldo >= 0.1:
                self.saldo -= 0.1
                print("maq: Chamada azul realizada. Saldo restante = " + self.formatar_moedas(self.saldo))
                self.state = "ocupado"
            else:
                print("maq: Saldo insuficiente para chamada azul. Saldo = " + self.formatar_moedas(self.saldo))
                self.numero_discado = ""
                self.state = "esperando"
        else:
            print("maq: Número inválido. Digite novo número!")
            self.numero_discado = ""
            self.state = "esperando"

    def abortar_interacao(self):
        troco = self.saldo
        self.saldo = 0
        self.estado = "IDLE"
        if troco > 0:
            moedas = self.calcular_troco(troco)
            mensagem = f"troco={self.formatar_moedas(troco)}; Volte sempre!"
            if moedas:
                mensagem += f" Troco: {', '.join(moedas)}."
            print("maq: " + mensagem)

    def formatar_moedas(self, valor):
        """
        Converte um valor em cêntimos para uma string formatada em euros.
        """
        return f"{valor // 100}e{valor % 100:02d}c"

    def calcular_troco(self, valor):
        """
        Calcula as moedas a devolver como troco.
        """
        moedas_disponiveis = [("2e", 200), ("1e", 100), ("50c", 50), ("20c", 20), ("10c", 10), ("5c", 5)]
        moedas_troco = []
        for moeda, valor_moeda in moedas_disponiveis:
            while valor >= valor_moeda:
                valor -= valor_moeda
                moedas_troco.append(moeda)
        return moedas_troco


# def main():
#     maquina_estados = TelefoneStateMachine()
#
#     while True:
#         if maquina_estados.state == "off":
#             print("Telefone desligado.")
#             break
#         elif maquina_estados.state == "esperando":
#             print("maq: Insira moedas ou digite um número para discar.")
#             entrada = input("> ")
#             if entrada.isnumeric():
#                 maquina_estados.discar_numero(entrada)
#             elif entrada.startswith("ins"):
#                 moedas = entrada.split()[1:]
#                 valores = [int(moeda[:-1]) for moeda in moedas]
#                 maquina_estados.inserir_moedas(valores)
#             elif entrada.startswith("desligar"):
#                 maquina_estados.abortar_interacao()
#                 break
#             else:
#                 print("Comando inválido.")
#         elif maquina_estados.state == "ocupado":
#             print("maq: Chamada em andamento. Digite 'desligar' para terminar a chamada.")
#             entrada = input("> ")
#             if entrada.startswith("desligar"):
#                 maquina_estados.abortar_interacao()
#                 break
#             else:
#                 print("Comando inválido.")
#         else:
#             print("Estado inválido.")
#             break
#
# if __name__ == "__main__":
#     main()