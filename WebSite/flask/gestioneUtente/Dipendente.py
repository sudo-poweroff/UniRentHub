class Dipendente:

    def __init__(self, email=None, nome=None, cognome=None, tipo_dipendente=None, password=None):
        self.__email = email
        self.__nome = nome
        self.__cognome = cognome
        self.__tipo_dipendente = tipo_dipendente
        self.__password = password

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCognome(self):
        return self.__cognome

    def setCognome(self, cognome):
        self.__cognome = cognome

    def getTipo(self):
        return self.__tipo_dipendente

    def setTipo(self, tipo):
        self.__tipo_dipendente = tipo

    def getPassword(self):
        return self.__tipo_dipendente

    def setPassword(self, password):
        self.__password = password
