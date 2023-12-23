class Messaggio:

    def __init__(self, id_messaggio=None, email=None, id_chat=None, contenuto=None):
        self.__id_messaggio = id_messaggio
        self.__email = email
        self.__id_chat = id_chat
        self.__contenuto = contenuto

    def get_id_messaggio(self):
        return self.__id_messaggio

    def set_id_messaggio(self, nuovo_id_messaggio):
        self.__id_messaggio = nuovo_id_messaggio

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email

    def get_id_chat(self):
        return self.__id_chat

    def set_id_chat(self, nuovo_id_chat):
        self.__id_chat = nuovo_id_chat

    def get_contenuto(self):
        return self.__contenuto

    def set_contenuto(self, nuovo_contenuto):
        self.__contenuto = nuovo_contenuto
