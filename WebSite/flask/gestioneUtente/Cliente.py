from flask import Flask


class Cliente:
    def __init__(self, email=None, nome=None, cognome=None, tipo_utente=None, data_nascita=None, numero_carta=None,
                 mese_scadenza=None, anno_scadenza=None, verificato=None, password=None, data_blocco=None):
        self.__email = email
        self.__nome = nome
        self.__cognome = cognome
        self.__tipo_utente = tipo_utente
        self.__data_nascita = data_nascita
        self.__numero_carta = numero_carta
        self.__mese_scadenza = mese_scadenza
        self.__anno_scadenza = anno_scadenza
        self.__verificato = verificato
        self.__password = password
        self.__data_blocco = data_blocco
    def getEmail(self):
        return self.__email

    def getNome(self):
        return self.__nome

    def getCognome(self):
        return self.__cognome

    def getTipo(self):
        return self.__tipo_utente

    def getDataNascita(self):
        return self.__data_nascita

    def getNumeroCarta(self):
        return self.__numero_carta

    def getVerificato(self):
        return self.__verificato

    def getMeseScadenza(self):
        return self.__mese_scadenza

    def getAnnoScadenza(self):
        return self.__anno_scadenza

    def getPassword(self):
        return self.__password

    def getDataBlocco(self):
        return self.__data_blocco

    def setEmail(self, email):
        self.__email = email

    def setNome(self, nome):
        self.__nome = nome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def setTipo(self, tipo):
        self.__tipo_utente = tipo

    def setDataNascita(self, data_nascita):
        self.__data_nascita = data_nascita

    def setNumeroCarta(self, numero_carta):
        self.__numero_carta = numero_carta

    def setVerificato(self, verificato):
        self.__verificato = verificato

    def setMeseScadenza(self, mese_scadenza):
        self.__mese_scadenza = mese_scadenza

    def setAnnoScadenza(self, anno_scadenza):
        self.__anno_scadenza = anno_scadenza

    def setPassword(self, password):
        self.__password = password

    def setDataBlocco(self, data_blocco):
        self.__data_blocco = data_blocco


