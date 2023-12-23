class Assegnazione:

    def __init__(self, idPassione=None, email=None):
        self.__idPassione = idPassione
        self.__email = email

    def getIdPassione(self):
        return self.__idPassione

    def setIdPassione(self, nuovo_idPassione):
        self.__idPassione = nuovo_idPassione

    def getEmail(self):
        return self.__email

    def setEmail(self, nuova_email):
        self.__email = nuova_email
