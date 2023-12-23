class Universita:

    def __init__(self, denomimazione, email, indirizzo):
        self.__denominazione = denomimazione
        self.__email = email
        self.__indirizzo = indirizzo

    # Getter per denominazione
    def getDenominazione(self):
        return self.__denominazione

    # Setter per denominazione
    def setDenominazione(self, nuova_denominazione):
        self.__denominazione = nuova_denominazione

    # Getter per email
    def getEmail(self):
        return self.__email

    # Setter per email
    def setEmail(self, nuova_email):
        self.__email = nuova_email

    # Getter per indirizzo
    def getIndirizzo(self):
        return self.__indirizzo

    # Setter per indirizzo
    def setIndirizzo(self, nuovo_indirizzo):
        self.__indirizzo = nuovo_indirizzo
