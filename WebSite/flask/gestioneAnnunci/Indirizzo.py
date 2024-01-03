class Indirizzo:

    def __init__(self, id_alloggio, via, cap, civico, citta, provincia):
        self.__id_alloggio = id_alloggio
        self.__via = via
        self.__cap = cap
        self.__civico = civico
        self.__citta = citta
        self.__provincia = provincia

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_via(self):
        return self.__via

    def set_via(self, nuova_via):
        self.__via = nuova_via

    def get_cap(self):
        return self.__cap

    def set_cap(self, nuovo_cap):
        self.__cap = nuovo_cap

    def get_civico(self):
        return self.__civico

    def set_civico(self, nuovo_civico):
        self.__civico = nuovo_civico

    def get_citta(self):
        return self.__citta

    def set_citta(self, nuova_citta):
        self.__citta = nuova_citta

    def get_provincia(self):
        return self.__provincia

    def set_provincia(self, nuova_provincia):
        self.__provincia = nuova_provincia
