class Affittare:

    def __init__(self, id_alloggio=None, email=None, data_inizio=None, data_fine=None, numero_carta=None, mese_scadenza=None, anno_scadenza=None, prezzo=None):
        self.__id_alloggio = id_alloggio
        self.__email = email
        self.__data_inizio = data_inizio
        self.__data_fine = data_fine
        self.__numero_carta = numero_carta
        self.__mese_scadenza = mese_scadenza
        self.__anno_scadenza = anno_scadenza
        self.__prezzo = prezzo

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_email(self):
        return self.__email

    def set_email(self, nuova_email):
        self.__email = nuova_email

    def get_data_inizio(self):
        return self.__data_inizio

    def set_data_inizio(self, nuova_data_inizio):
        self.__data_inizio = nuova_data_inizio

    def get_data_fine(self):
        return self.__data_fine

    def set_data_fine(self, nuova_data_fine):
        self.__data_fine = nuova_data_fine

    def get_numero_carta(self):
        return self.__numero_carta

    def set_numero_carta(self, nuovo_numero_carta):
        self.__numero_carta = nuovo_numero_carta

    def get_prezzo(self):
        return self.__prezzo

    def set_prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo


    def get_mese_scadenza(self):
        return self.__mese_scadenza

    def set_mese_scadenza(self, nuovo_mese_scadenza):
        self.__mese_scadenza  = nuovo_mese_scadenza

    def get_anno_scadenza(self):
        return self.__anno_scadenza

    def set_anno_scadenza(self, nuovo_anno_scadenza):
        self.__anno_scadenza = nuovo_anno_scadenza