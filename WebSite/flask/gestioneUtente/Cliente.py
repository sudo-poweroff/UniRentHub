class Cliente:
    def __init__(self, email=None, nome=None, cognome=None, tipo_utente=None, data_nascita=None, numero_carta=None, verificato=None, data_scadenza=None, password=None):
        self.__email = email
        self.__nome = nome
        self.__cognome = cognome
        self.__tipo_utente = tipo_utente
        self.__data_nascita = data_nascita
        self.__numero_carta = numero_carta
        self.__verificato = verificato
        self.__data_scadenza = data_scadenza
        self.__password = password

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

    def getDataScadenza(self):
        return self.__data_scadenza

    def getPassword(self):
        return self.__password

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

    def setDataScadenza(self, data_scadenza):
        self.__data_scadenza = data_scadenza

    def setPassword(self, password):
        self.__password = password
