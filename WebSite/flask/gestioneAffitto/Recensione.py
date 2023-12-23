class Recensione:

    def __init__(self, id_alloggio, email, titolo, voto, descrizione, data_recensione):
        self.__id_alloggio = id_alloggio
        self.__email = email
        self.__titolo = titolo
        self.__voto = voto
        self.__descrizione = descrizione
        self.__data_recensione = data_recensione

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email

    def get_titolo(self):
        return self.__titolo

    def set_titolo(self, nuovo_titolo):
        self.__titolo = nuovo_titolo

    def get_voto(self):
        return self.__voto

    def set_voto(self, nuovo_voto):
        self.__voto = nuovo_voto

    def get_descrizione(self):
        return self.__descrizione

    def set_descrizione(self, nuova_descrizione):
        self.__descrizione = nuova_descrizione

    def get_data_recensione(self):
        return self.__data_recensione

    def set_data_recensione(self, nuova_data_recensione):
        self.__data_recensione = nuova_data_recensione
