class Segnalazione:

    def __init__(self, email, emailS, stato, motivo):
        self.__email = email
        self.__emailS = emailS
        self.__stato = stato
        self.__motivo = motivo

    def getEmail(self):
        return self.__email

    def setEmail(self, nuova_email):
        self.__email = nuova_email

    def getEmailS(self):
        return self.__emailS

    def setEmailS(self, nuova_emailS):
        self.__emailS = nuova_emailS

    def getStato(self):
        return self.__stato

    def setStato(self, nuovo_stato):
        self.__stato = nuovo_stato

    def getMotivo(self):
        return self.__motivo

    def setMotivo(self, nuovo_motivo):
        self.__motivo = nuovo_motivo
