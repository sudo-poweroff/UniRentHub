class Immagine:

    def __init__(self, id_immagine, id_alloggio, path):
        self.__id_immagine = id_immagine
        self.__id_alloggio = id_alloggio
        self.__path = path

    def get_id_immagine(self):
        return self.__id_immagine

    def set_id_immagine(self, nuovo_id_immagine):
        self.__id_immagine = nuovo_id_immagine

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_path(self):
        return self.__path

    def set_path(self, nuovo_path):
        self.__path = nuovo_path
