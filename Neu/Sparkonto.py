from Konto import Konto
from Konto import typecheck

class Sparkonto(Konto):
    def __init__(self, inhaber, startguthaben, zinssatz):
        if not typecheck(zinssatz, [int, float]):
            raise TypeError("Der Zinssatz muss eine Zahl sein.")
        if zinssatz < 0:
            raise ValueError("Der Zinssatz darf nicht negativ sein.")
        
        super().__init__(inhaber, startguthaben)
        self.__zinssatz = zinssatz
    
    def zinssatz(self):
        return self.__zinssatz
    
    def zinsen_berechnen(self):
        zinsen = super().guthaben() * self.__zinssatz / 100
        self.buchen(zinsen, "Zinsen")
        return zinsen

if __name__ == "__main__":
    konto = Sparkonto("Max Mustermann", 1000, 1.5)
    konto.buchen(100, "Gehalt")
    konto.auszahlen(50)
    konto.zinsen_berechnen()
    konto.buchungen_anzeigen()
    print(f"Kontoinhaber: {konto.inhaber()}")