class Servizi:

    def __init__(self, id_servizio=None, descrizione=None):
        self.__id_servizio = id_servizio
        self.__descrizione = descrizione

    def get_id_servizio(self):
        return self.__id_servizio

    def set_id_servizio(self, nuovo_id_servizio):
        self.__id_servizio = nuovo_id_servizio

    def get_descrizione(self):
        return self.__descrizione

    def set_descrizione(self, nuova_descrizione):
        self.__descrizione = nuova_descrizione
