class Studente:
    def __init__(self, nome, cognome, anno_nascita):
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita

    def eta(self):
        print("Sei nato nel", self.anno_nascita, "quindi hai",
              2025-self.anno_nascita,"anni")

    def scheda(self):
        anni = 2025-self.anno_nascita
        print("Mi chiamo",self.nome,self.cognome,"e ho",anni,"anni")

stas = Studente("Mario", "Rossi", 2007)
stas.eta()
stas.scheda()