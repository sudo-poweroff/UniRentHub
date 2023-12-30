class Alloggio:

    def __init__(self, id_alloggio=None, tipo_alloggio=None, disponibilita=None, titolo=None, mq=None,
                 n_camere_letto=None, n_bagni=None, classe_energetica=None, arredamenti=None,
                 data_publicazione=None, pannelli_solari=None, pannelli_fotovoltaici=None,
                 descrizione=None, verifica=None, prezzo=None, n_ospiti=None, n_stanze=None,
                 tasse=None, email_dip=None, email_loc=None, data_verifica=None):
        self.__id_alloggio = id_alloggio
        self.__tipo_alloggio = tipo_alloggio
        self.__disponibilita = disponibilita
        self.__titolo = titolo
        self.__mq = mq
        self.__n_camere_letto = n_camere_letto
        self.__n_bagni = n_bagni
        self.__classe_energetica = classe_energetica
        self.__arredamenti = arredamenti
        self.__data_publicazione = data_publicazione
        self.__pannelli_solari = pannelli_solari
        self.__pannelli_fotovoltaici = pannelli_fotovoltaici
        self.__descrizione = descrizione
        self.__verifica = verifica
        self.__prezzo = prezzo
        self.__n_ospiti = n_ospiti
        self.__n_stanze = n_stanze
        self.__tasse = tasse
        self.__email_dip = email_dip
        self.__email_loc = email_loc
        self.__data_verifica = data_verifica

    def get_id_alloggio(self):
        return self.__id_alloggio

    def set_id_alloggio(self, nuovo_id_alloggio):
        self.__id_alloggio = nuovo_id_alloggio

    def get_tipo_alloggio(self):
        return self.__tipo_alloggio

    def set_tipo_alloggio(self, nuovo_tipo_alloggio):
        self.__tipo_alloggio = nuovo_tipo_alloggio

    def get_disponibilita(self):
        return self.__disponibilita

    def set_disponibilita(self, nuova_disponibilita):
        self.__disponibilita = nuova_disponibilita

    def get_titolo(self):
        return self.__titolo

    def set_titolo(self, nuovo_titolo):
        self.__titolo = nuovo_titolo

    def get_mq(self):
        return self.__mq

    def set_mq(self, nuovo_mq):
        self.__mq = nuovo_mq

    def get_n_camere_letto(self):
        return self.__n_camere_letto

    def set_n_camere_letto(self, nuovo_n_camere_letto):
        self.__n_camere_letto = nuovo_n_camere_letto

    def get_n_bagni(self):
        return self.__n_bagni

    def set_n_bagni(self, nuovo_n_bagni):
        self.__n_bagni = nuovo_n_bagni

    def get_classe_energetica(self):
        return self.__classe_energetica

    def set_classe_energetica(self, nuova_classe_energetica):
        self.__classe_energetica = nuova_classe_energetica

    def get_arredamenti(self):
        return self.__arredamenti

    def set_arredamenti(self, nuovi_arredamenti):
        self.__arredamenti = nuovi_arredamenti

    def get_data_publicazione(self):
        return self.__data_publicazione

    def set_data_publicazione(self, nuova_data_publicazione):
        self.__data_publicazione = nuova_data_publicazione

    def get_pannelli_solari(self):
        return self.__pannelli_solari

    def set_pannelli_solari(self, nuovi_pannelli_solari):
        self.__pannelli_solari = nuovi_pannelli_solari

    def get_pannelli_fotovoltaici(self):
        return self.__pannelli_fotovoltaici

    def set_pannelli_fotovoltaici(self, nuovi_pannelli_fotovoltaici):
        self.__pannelli_fotovoltaici = nuovi_pannelli_fotovoltaici

    def get_descrizione(self):
        return self.__descrizione

    def set_descrizione(self, nuova_descrizione):
        self.__descrizione = nuova_descrizione

    def get_verifica(self):
        return self.__verifica

    def set_verifica(self, nuova_verifica):
        self.__verifica = nuova_verifica

    def get_prezzo(self):
        return self.__prezzo

    def set_prezzo(self, nuovo_prezzo):
        self.__prezzo = nuovo_prezzo

    def get_n_ospiti(self):
        return self.__n_ospiti

    def set_n_ospiti(self, nuovo_n_ospiti):
        self.__n_ospiti = nuovo_n_ospiti

    def get_n_stanze(self):
        return self.__n_stanze

    def set_n_stanze(self, nuovo_n_stanze):
        self.__n_stanze = nuovo_n_stanze

    def get_tasse(self):
        return self.__tasse

    def set_tasse(self, nuove_tasse):
        self.__tasse = nuove_tasse

    def get_email_dip(self):
        return self.__email_dip

    def set_email_dip(self, nuova_email_dip):
        self.__email_dip = nuova_email_dip

    def get_email_loc(self):
        return self.__email_loc

    def set_email_loc(self, nuova_email_loc):
        self.__email_loc = nuova_email_loc

    def get_data_verifica(self):
        return self.__data_verifica

    def set_data_verifica(self, nuova_data_verifica):
        self.__data_verifica = nuova_data_verifica
