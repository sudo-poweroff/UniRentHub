class Passione:

    def __init__(self, id_passione, nome):
        self.__id_passione = id_passione
        self.__nome = nome

    def getIdpassione(self):
        return self.__id_passione

    def seIdpassione(self, nuovo_id_passione):
        self.__id_passione = nuovo_id_passione

    def getNome(self):
        return self.__nome

    def setNome(self, nuovo_nome):
        self.__nome = nuovo_nome
