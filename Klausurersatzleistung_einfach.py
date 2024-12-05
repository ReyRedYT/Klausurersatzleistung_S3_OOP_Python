import random  # Importiere das Modul random, um zufällige IBANs zu generieren

def typecheck(variable, validTypes):
    if not isinstance(variable, validTypes):
        raise TypeError(f"Variable {variable} is not of type {validTypes}") # Gib eine Fehlermeldung aus, wenn der Typ nicht übereinstimmend ist


class Konto:  # Definiere die Basisklasse Konto
    def __init__(self, inhaber, startguthaben=0):  # Initialisierungsmethode
        self.inhaber = inhaber  # Setze den Kontoinhaber
        self.guthaben = startguthaben  # Setze das Startguthaben
        self.iban = self.generiere_iban()  # Generiere eine IBAN für das Konto
        self.buchungen = []  # Initialisiere eine Liste für die Buchungen


    def generiere_iban(self):  # Methode zur Generierung einer IBAN
        return 'DE' + ''.join([str(random.randint(0, 9)) for _ in range(20)])  # Erzeuge eine zufällige IBAN


    def einzahlen(self, betrag):  # Methode zum Einzahlen eines Betrags
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        self.guthaben += betrag  # Erhöhe das Guthaben um den Betrag
        self.buchungen.append(f"Einzahlung über {betrag} EUR")  # Füge die Buchung hinzu
        print(f"Einzahlung über {betrag} EUR erfolgreich")


    def auszahlen(self, betrag):  # Methode zum Auszahlen eines Betrags
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        if betrag <= self.guthaben:  # Überprüfe, ob genügend Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das Guthaben um den Betrag
            self.buchungen.append(f"Auszahlung über {betrag} EUR")  # Füge die Buchung hinzu
            print(f"Auszahlung über {betrag} EUR erfolgreich")  # Gib eine Erfolgsmeldung aus
        else:
            print("Nicht genügend Guthaben")  # Gib eine Fehlermeldung aus


    def ueberweisen(self, empfaenger, betrag):  # Methode zur Überweisung eines Betrags
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        if betrag <= self.guthaben:  # Überprüfe, ob genügend Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das Guthaben um den Betrag
            empfaenger.einzahlen(betrag)  # Zahle den Betrag auf das Empfängerkonto ein
            self.buchungen.append(f"Überweisung an {empfaenger.inhaber} mit der IBAN {empfaenger.iban} über {betrag} EUR")  # Füge die Buchung hinzu
            empfaenger.buchungen.append(f"Überweisung von {self.inhaber} mit der IBAN {self.iban} über {betrag} EUR")  # Füge die Buchung hinzu
            print(f"Überweisung von {self.inhaber} an {empfaenger.inhaber} über {betrag} EUR erfolgreich")  # Gib eine Erfolgsmeldung aus
        else:
            print("Nicht genügend Guthaben")  # Gib eine Fehlermeldung aus


    def buchungen_anzeigen(self):  # Methode zur Anzeige der Buchungen
        print(f"\n{'='*50}")
        print(f"Kontoauszug für {self.inhaber} (IBAN: {self.iban})")  # Gib den Kontoinhaber und die IBAN aus
        print(f"{'='*50}")
        if self.buchungen:
            for buchung in self.buchungen:  # Iteriere über die Buchungen
                print(f"{buchung}")  # Gib die Buchung aus
        else:
            print("Keine Buchungen vorhanden.")  # Nachricht, wenn keine Buchungen vorhanden sind
        print(f"{'='*50}")
        print(f"Aktueller Kontostand: {self.guthaben:.2f} EUR\n")  # Gib den aktuellen Kontostand aus
        print(f"{'='*50}\n")


    def iban_ausgeben(self):  # Methode zur Ausgabe der IBAN
        print(self.inhaber, self.iban)  # Gib die IBAN aus

    def kontostand(self):  # Methode zur Ausgabe des Kontostands
        print(f"{self.inhaber} mit der IBAN: {self.iban} hat {self.guthaben}€ Guthaben.")  # Gib den Kontostand aus


    def __str__(self):  # Dunder-Methode zur String-Repräsentation des Kontos
        return f'Inhaber: {self.inhaber}, IBAN: {self.iban}, Guthaben: {self.guthaben} EUR'  # Rückgabe der Kontoinformationen




class Sparkonto(Konto):  # Definiere die Klasse Sparkonto, die von Konto erbt
    def __init__(self, inhaber, startguthaben=0, zinssatz=0.0325):  # Initialisierungsmethode
        super().__init__(inhaber, startguthaben)  # Rufe die Initialisierungsmethode der Basisklasse auf
        self.zinssatz = zinssatz  # Setze den Zinssatz


    def zinsen_berechnen(self):  # Methode zur Berechnung der Zinsen
        print(f"Zinsen in Höhe von {self.guthaben * self.zinssatz} EUR wurden dem Konto von {self.inhaber} mit der IBAN: {self.iban} gutgeschrieben.")  # Gib die Zinsen aus
        self.guthaben += self.guthaben * self.zinssatz  # Erhöhe das Guthaben um die Zinsen


    def __str__(self):  # Dunder-Methode zur String-Repräsentation des Sparkontos
        return f'Inhaber: {self.inhaber}, IBAN: {self.iban}, Guthaben: {self.guthaben} EUR, Zinssatz: {self.zinssatz * 100} %'  # Rückgabe der Kontoinformationen




class Multiwaehrungskonto(Konto):  # Definiere die Klasse Multiwaehrungskonto, die von Konto erbt
    def __init__(self, inhaber, startguthaben=0, usd_guthaben=0):  # Initialisierungsmethode
        super().__init__(inhaber, startguthaben)  # Rufe die Initialisierungsmethode der Basisklasse auf
        self.usd_guthaben = usd_guthaben  # Setze das USD-Guthaben


    def usd_einzahlen(self, betrag):  # Methode zum Einzahlen eines Betrags in USD
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        self.usd_guthaben += betrag  # Erhöhe das USD-Guthaben um den Betrag
        print(f"Einzahlung über {betrag} USD erfolgreich")  # Gib eine Erfolgsmeldung aus


    def usd_auszahlen(self, betrag):  # Methode zum Auszahlen eines Betrags in USD
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        if betrag <= self.usd_guthaben:  # Überprüfe, ob genügend USD-Guthaben vorhanden ist
            self.usd_guthaben -= betrag  # Verringere das USD-Guthaben um den Betrag
            print(f"Auszahlung über {betrag} USD erfolgreich")  # Gib eine Erfolgsmeldung aus
        else:
            print("Nicht genügend USD-Guthaben")  # Gib eine Fehlermeldung aus


    def usd_in_eur(self, betrag, wechselkurs=0.94):  # Methode zur Umrechnung von USD in EUR
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        if betrag <= self.usd_guthaben:  # Überprüfe, ob genügend USD-Guthaben vorhanden ist
            self.usd_guthaben -= betrag  # Verringere das USD-Guthaben um den Betrag
            self.guthaben += betrag * wechselkurs  # Erhöhe das EUR-Guthaben um den umgerechneten Betrag
            print(f"Umtausch von {betrag} USD in {betrag * wechselkurs} EUR erfolgreich")  # Gib eine Erfolgsmeldung aus
        else:
            print("Nicht genügend USD-Guthaben")  # Gib eine Fehlermeldung aus


    def eur_in_usd(self, betrag, wechselkurs=1.06):  # Methode zur Umrechnung von EUR in USD
        typecheck(betrag, (int, float))  # Überprüfe, ob der Betrag ein Integer oder Float ist
        if betrag <= self.guthaben:  # Überprüfe, ob genügend EUR-Guthaben vorhanden ist
            self.guthaben -= betrag  # Verringere das EUR-Guthaben um den Betrag
            self.usd_guthaben += betrag * wechselkurs  # Erhöhe das USD-Guthaben um den umgerechneten Betrag
            print(f"Umtausch von {betrag} EUR in {betrag * wechselkurs} USD erfolgreich")  # Gib eine Erfolgsmeldung aus
        else:
            print("Nicht genügend EUR-Guthaben")  # Gib eine Fehlermeldung aus


    def __str__(self):  # Dunder-Methode zur String-Repräsentation des Multiwährungskontos
        return f'Inhaber: {self.inhaber}, IBAN: {self.iban}, Guthaben: {self.guthaben} EUR, USD-Guthaben: {self.usd_guthaben} USD'  # Rückgabe der Kontoinformationen



# Test

konto1 = Konto("Arasp Shojai", 1000)  # Erstelle ein Konto für Arasp Shojai mit 1000 EUR Startguthaben
sparkonto1 = Sparkonto("Malte Haan", 2000, 0.0325)  # Erstelle ein Sparkonto für Malte Haan mit 2000 EUR Startguthaben und 3,25% Zinssatz
multiwaehrungskonto1 = Multiwaehrungskonto("Nekisa Shojai", 500, 100)  # Erstelle ein Multiwährungskonto für Nekisa Shojai mit 500 EUR und 100 USD Startguthaben


print(konto1)  # Gib die Informationen des Kontos aus
print(sparkonto1)  # Gib die Informationen des Sparkontos aus
print(multiwaehrungskonto1)  # Gib die Informationen des Multiwährungskontos aus


konto1.einzahlen(100)  # Zahle 100 EUR auf das Konto ein
konto1.auszahlen(200)  # Zahle 200 EUR vom Konto aus
konto1.ueberweisen(sparkonto1, 300)  # Überweise 300 EUR vom Konto auf das Sparkonto


sparkonto1.zinsen_berechnen()  # Berechne die Zinsen für das Sparkonto


multiwaehrungskonto1.usd_einzahlen(50)  # Zahle 50 USD auf das Multiwährungskonto ein
multiwaehrungskonto1.usd_in_eur(100)  # Wandle 100 USD in EUR um
multiwaehrungskonto1.eur_in_usd(50)  # Wandle 50 EUR in USD um


print(konto1)  # Gib die aktualisierten Informationen des Kontos aus
print(sparkonto1)  # Gib die aktualisierten Informationen des Sparkontos aus
print(multiwaehrungskonto1)  # Gib die aktualisierten Informationen des Multiwährungskontos aus

konto1.iban_ausgeben()  # Gib die IBAN des Kontos aus
sparkonto1.kontostand()  # Gib den Kontostand des Sparkontos aus
sparkonto1.einzahlen(1000)  # Zahle 1000 EUR auf das Sparkonto ein
sparkonto1.buchungen_anzeigen()  # Gib die Buchungen des Kontos aus
