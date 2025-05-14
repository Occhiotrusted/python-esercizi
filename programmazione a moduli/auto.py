class Auto:
    def __init__(self, marca, modello, velocita):
        self.marca = marca
        self.modello = modello
        self.velocita = velocita  # velocità attuale

    def accelera(self, n):
        self.velocita += n  # aumenta la velocità

    def stato(self):
        print(f"{self.marca} {self.modello} sta andando a {self.velocita} km/h")
