class Post:

    def __init__(self, id_post = None, titolo = None, descrizione = None, email = None):
        self.__id_post = id_post
        self.__titolo = titolo
        self.__descrizione = descrizione
        self.__email = email

    def get_id_post(self):
        return self.__id_post

    def set_id_post(self, nuovo_id_post):
        self.__id_post = nuovo_id_post

    def get_titolo(self):
        return self.__titolo

    def set_titolo(self, nuovo_titolo):
        self.__titolo = nuovo_titolo

    def get_descrizione(self):
        return self.__descrizione

    def set_descrizione(self, nuova_descrizione):
        self.__descrizione = nuova_descrizione

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email
