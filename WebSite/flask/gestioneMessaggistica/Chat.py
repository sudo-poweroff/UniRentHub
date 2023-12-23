class Chat:

    def __init__(self, id_chat, titolo):
        self.__id_chat = id_chat
        self.__titolo = titolo

    def get_id_chat(self):
        return self.__id_chat

    def set_id_chat(self, nuovo_id_chat):
        self.__id_chat = nuovo_id_chat

    def get_titolo(self):
        return self.__titolo

    def set_titolo(self, nuovo_titolo):
        self.__titolo = nuovo_titolo
