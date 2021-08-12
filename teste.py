class ContaBancaria:
    def __init__(self, numero, titular, saldo=0, limite=0):
        self.numero = numero
        self.titular = titular
        self.saldo = float(saldo)
        self.limite = float(limite)

conta451 = ContaBancaria(451, "Michel xd", 400.0, 1000.0)
print(conta451.titular) #Michel xd