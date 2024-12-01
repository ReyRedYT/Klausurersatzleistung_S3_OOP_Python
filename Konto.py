# Konto (kann importiert werden)
class Konto:  # Definiere die Basisklasse Konto
    def __init__(self, inhaber, startguthaben=0):  # Initialisierungsmethode
        self.inhaber = inhaber  # Setze den Kontoinhaber
        self.guthaben = startguthaben  # Setze das Startguthaben
        self.iban = self.generiere_iban()  # Generiere eine IBAN für das Konto


    def generiere_iban(self):  # Methode zur Generierung einer IBAN
        return 'DE' + ''.join([str(random.randint(0, 9)) for _ in range(20)])  # Erzeuge eine zufällige IBAN


    def einzahlen(self, betrag):  # Methode zum Einzahlen eines Betrags
        self.guthaben += betrag  # Erhöhe das Guthaben um den Betrag


    def auszahlen(self, betrag):  # Methode zum Auszahlen eines Betrags
        if betrag <= self.guthaben:  # Überprüfe, ob genügend Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das Guthaben um den Betrag
        else:
            print("Nicht genügend Guthaben")  # Gib eine Fehlermeldung aus


    def ueberweisen(self, empfaenger, betrag):  # Methode zur Überweisung eines Betrags
        if betrag <= self.guthaben:  # Überprüfe, ob genügend Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das Guthaben um den Betrag
            empfaenger.einzahlen(betrag)  # Zahle den Betrag auf das Empfängerkonto ein
        else:
            print("Nicht genügend Guthaben")  # Gib eine Fehlermeldung aus


    def __str__(self):  # Dunder-Methode zur String-Repräsentation des Kontos
        return f'Inhaber: {self.inhaber}, IBAN: {self.iban}, Guthaben: {self.guthaben} EUR'  # Rückgabe der Kontoinformationen