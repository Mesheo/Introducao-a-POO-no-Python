class ContaBancaria:
    def __init__(self, numero, titular, saldo=0, limite=0):
        # Atributos da conta
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # Método para sacar um certo valor
    def sacar(self, valor):
        print("\nRealizando saque...")
        if (self.saldo - valor) < 0:  
            print(f"Saque não realizado, dinheiro insuficiente na conta")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado, agora seu saldo é de R${self.saldo}")
    
    # Método para sacar um certo valor
    def depositar(self, valor):
        print("\nRealizando depósito...")
        self.saldo += valor
        print(f"Deposito de R${valor} realizado, agora seu saldo é de R${self.saldo}\n")
     
    # Método para visualizar o saldo 
    def extrato(self):
        print("\nColetando extrato...")
        print(f"Seu saldo atual é de R${self.saldo}")
    
conta1 = ContaBancaria(111, "Roberto")
conta1.extrato()
conta1.sacar(200)
conta1.depositar(250)
