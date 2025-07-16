class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def movimentar(self):
        return f"O veículo {self.marca} {self.modelo} está se movendo."

class Carro(Veiculo):
    def movimentar(self):
        return f"O carro {self.marca} {self.modelo} está dirigindo."

class Moto(Veiculo):
    def movimentar(self):
        return f"A moto {self.marca} {self.modelo} está acelerando."

carro1 = Carro(marca="Toyota", modelo="Corolla")
moto1 = Moto(marca="Honda", modelo="CB500")

print(carro1.movimentar())
print(moto1.movimentar())
