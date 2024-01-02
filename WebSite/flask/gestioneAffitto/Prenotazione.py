class Prenotazione:

    def __init__(self, id_alloggio = None, email = None, data_visita = None, disponibilita = None):
        self.__id_alloggio = id_alloggio
        self.__email = email
        self.__data_visita = data_visita
        self.__disponibilita = disponibilita

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email

    def get_data_visita(self):
        return self.__data_visita

    def set_data_visita(self, nuova_data_visita):
        self.__data_visita = nuova_data_visita

    def get_disponibilita(self):
        return self.__disponibilita

    def set_disponibilita(self, disponibilita):
        self.__disponibilita = disponibilita