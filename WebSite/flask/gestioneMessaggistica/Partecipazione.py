class Partecipazione:

    def __init__(self, id_chat, email):
        self.__id_chat = id_chat
        self.__email = email

    def get_id_chat(self):
        return self.__id_chat

    def set_id_chat(self, nuovo_id_chat):
        self.__id_chat = nuovo_id_chat

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email

