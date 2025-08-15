# class Itenditade :
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#
#     def Saudar (self):
#         print(f"Olá,Me chamo {self.nome} e tenho {self.idade} Anos.")
#
#
# p1 = Itenditade("Jhon", 31)
# p1.Saudar()

class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adc_notas(self, notas):
        self.notas.append(notas)

    def Media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

    def reportar(self):
        print(f"{self.nome} e a media das minhas notas: {self.Media():.2f}")


est = Estudante("jhon santos")
est.adc_notas(7)
est.adc_notas(10)
est.adc_notas(4)
est.adc_notas(6.5)
est.reportar()