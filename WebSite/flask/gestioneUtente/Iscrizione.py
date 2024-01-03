class Iscrizione:

    def __init__(self, denominazione=None, email=None):
        self.__denominazione = denominazione
        self.__email = email

    def getDenominazione(self):
        return self.__denominazione

    def setDenominazione(self, nuova_denominazione):
        self.__denominazione = nuova_denominazione

    def getEmail(self):
        return self.__email

    def setEmail(self, nuova_email):
        self.__email = nuova_email
