class Servizi:

    def __init__(self, id_servizio=None, id_alloggio=None):
        self.__id_servizio = id_servizio
        self.__id_alloggio = id_alloggio

    def get_id_servizio(self):
        return self.__id_servizio

    def set_id_servizio(self, nuovo_id_servizio):
        self.__id_servizio = nuovo_id_servizio

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio
