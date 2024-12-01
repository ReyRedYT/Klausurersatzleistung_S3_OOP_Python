# Konto Basisklasse
import random

def typecheck(object, types):
    return any([isinstance(object, t) for t in types])

class Konto:
    def __init__(self, inhaber, startguthaben=0):
        if not typecheck(inhaber, [str]):
            raise TypeError("Der Inhaber muss ein String sein.")
        if not typecheck(startguthaben, [int, float]):
            raise TypeError("Das Startguthaben muss eine Zahl sein.")
        if startguthaben < 0:
            raise ValueError("Das Startguthaben darf nicht negativ sein.")
        
        self.__inhaber = inhaber
        self.__guthaben = startguthaben
        self.__iban = self.generiere_iban()
        self.__buchungen = []
    
    def generiere_iban(self):
        return 'DE' + ''.join([str(random.randint(0, 9)) for _ in range(20)])

    # Zugriffsmethoden
    def inhaber(self):
        return self.__inhaber

    def guthaben(self):
        return self.__guthaben

    def iban(self):
        return self.__iban

    # Buchungsmethoden
    def buchen(self, betrag, verwendungszweck=""):
        if not typecheck(betrag, [int, float]):
            raise TypeError("Der Betrag muss eine Zahl sein.")
        if self.__guthaben + betrag < 0:
            raise ValueError("Das Guthaben darf nicht negativ werden.")
        
        self.__guthaben += betrag
        self.__buchungen.append((betrag, verwendungszweck))

    def einzahlen(self, betrag):
        self.buchen(betrag, "Einzahlung")
    
    def auszahlen(self, betrag):
        self.buchen(-betrag, "Auszahlung")

    def buchungen_anzeigen(self):
        print("Buchungen für:", self.__inhaber, self.__iban)
        for i in range(len(self.__buchungen)):
            print(f"{(i+1):2.0f}. {self.__buchungen[i][0]:8.2f} EUR - {self.__buchungen[i][1]}")
    
    def __str__(self):
        return f"[Konto] Inhaber: {self.__inhaber}, IBAN: {self.__iban}, Guthaben: {self.__guthaben} EUR"


if __name__ == "__main__":
    konto1 = Konto("Arasp Shojai", 1000)
    konto1.einzahlen(500)
    konto1.auszahlen(200)
    konto1.buchungen_anzeigen()