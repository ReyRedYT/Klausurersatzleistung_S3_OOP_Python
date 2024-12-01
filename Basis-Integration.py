import random  # Importiere das Modul random, um zufällige IBANs zu generieren
from Konto import Konto # Importiere das Modul Konto, um die Basisklasse Konto zu verwenden

# Sparkonto (erbt von Konto)
class Sparkonto(Konto.Konto):  # Definiere die Klasse Sparkonto, die von Konto erbt
    def __init__(self, inhaber, startguthaben=0, zinssatz=0.0375):  # Initialisierungsmethode
        super().__init__(inhaber, startguthaben)  # Rufe die Initialisierungsmethode der Basisklasse auf
        self.zinssatz = zinssatz  # Setze den Zinssatz


    def zinsen_berechnen(self):  # Methode zur Berechnung der Zinsen
        self.guthaben += self.guthaben * self.zinssatz  # Erhöhe das Guthaben um die Zinsen




class Multiwaehrungskonto(Konto.Konto):  # Definiere die Klasse Multiwaehrungskonto, die von Konto erbt
    def __init__(self, inhaber, startguthaben=0, usd_guthaben=0):  # Initialisierungsmethode
        super().__init__(inhaber, startguthaben)  # Rufe die Initialisierungsmethode der Basisklasse auf
        self.usd_guthaben = usd_guthaben  # Setze das USD-Guthaben


    def usd_einzahlen(self, betrag):  # Methode zum Einzahlen eines Betrags in USD
        self.usd_guthaben += betrag  # Erhöhe das USD-Guthaben um den Betrag


    def usd_auszahlen(self, betrag):  # Methode zum Auszahlen eines Betrags in USD
        if betrag <= self.usd_guthaben:  # Überprüfe, ob genügend USD-Guthaben vorhanden ist
            self.usd_guthaben -= betrag  # Verringere das USD-Guthaben um den Betrag
        else:
            print("Nicht genügend USD-Guthaben")  # Gib eine Fehlermeldung aus


    def usd_in_eur(self, betrag, wechselkurs=0.94):  # Methode zur Umrechnung von USD in EUR
        if betrag <= self.usd_guthaben:  # Überprüfe, ob genügend USD-Guthaben vorhanden ist
            self.usd_guthaben -= betrag  # Verringere das USD-Guthaben um den Betrag
            self.guthaben += betrag * wechselkurs  # Erhöhe das EUR-Guthaben um den umgerechneten Betrag
        else:
            print("Nicht genügend USD-Guthaben")  # Gib eine Fehlermeldung aus


    def eur_in_usd(self, betrag, wechselkurs=1.06):  # Methode zur Umrechnung von EUR in USD
        if betrag <= self.guthaben:  # Überprüfe, ob genügend EUR-Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das EUR-Guthaben um den Betrag
            self.usd_guthaben += betrag * wechselkurs  # Erhöhe das USD-Guthaben um den umgerechneten Betrag
        else:
            print("Nicht genügend EUR-Guthaben")  # Gib eine Fehlermeldung aus


    def __str__(self):  # Dunder-Methode zur String-Repräsentation des Multiwährungskontos
        return f'Inhaber: {self.inhaber}, IBAN: {self.iban}, Guthaben: {self.guthaben} EUR, USD-Guthaben: {self.usd_guthaben} USD'  # Rückgabe der Kontoinformationen



# Beispiel zur Demonstration

konto1 = Konto("Arasp Shojai", 1000)  # Erstelle ein Konto für Arasp Shojai mit 1000 EUR Startguthaben
sparkonto1 = Sparkonto("Malte Haan", 2000, 0.0375)  # Erstelle ein Sparkonto für Malte Haan mit 2000 EUR Startguthaben und 2% Zinssatz
multiwaehrungskonto1 = Multiwaehrungskonto("Nekisa Shojai", 500, 100)  # Erstelle ein Multiwährungskonto für Nekisa Shojai mit 500 EUR und 100 USD Startguthaben


print(konto1)  # Gib die Informationen des Kontos aus
print(sparkonto1)  # Gib die Informationen des Sparkontos aus
print(multiwaehrungskonto1)  # Gib die Informationen des Multiwährungskontos aus


konto1.einzahlen(500)  # Zahle 500 EUR auf das Konto ein
konto1.auszahlen(200)  # Zahle 200 EUR vom Konto aus
konto1.ueberweisen(sparkonto1, 300)  # Überweise 300 EUR vom Konto auf das Sparkonto


sparkonto1.zinsen_berechnen()  # Berechne die Zinsen für das Sparkonto


multiwaehrungskonto1.usd_einzahlen(50)  # Zahle 50 USD auf das Multiwährungskonto ein
multiwaehrungskonto1.usd_in_eur(100)  # Wandle 100 USD in EUR um
multiwaehrungskonto1.eur_in_usd(50)  # Wandle 50 EUR in USD um


print(konto1)  # Gib die aktualisierten Informationen des Kontos aus
print(sparkonto1)  # Gib die aktualisierten Informationen des Sparkontos aus
print(multiwaehrungskonto1)  # Gib die aktualisierten Informationen des Multiwährungskontos aus
