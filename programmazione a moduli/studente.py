import util

class Studente:
    def __init__(self, nome, cognome, anno_nascita):
        self.nome = nome
        self.cognome = cognome
        self.anno_nascita = anno_nascita
        self.voti = []

    def eta(self):
        return 2025 - self.anno_nascita

    def scheda(self):
        print(f"Mi chiamo {self.nome} {self.cognome} e ho {self.eta()} anni.")

    def aggiungi_voto(self, voto):
        if isinstance(voto, (int, float)):
            self.voti.append(voto)
        else:
            print("Errore: il voto deve essere un numero.")

    def media(self):
        if not self.voti:
            return 0
        return util.media(self.voti)
