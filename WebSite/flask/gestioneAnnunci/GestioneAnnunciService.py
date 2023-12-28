import re
from flask import Flask, flash

from .AnnuncioDAO import AnnuncioDAO
from .Post import Post
from .PostDAO import PostDAO
from WebSite.flask.gestioneUtente.ClienteDAO import ClienteDAO


# Funzione di controllo per l'email caratteri
def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))


# Controlla email esistente
def controlla_email_esistente(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email)
    if cliente:
        return True  # se il cliente esiste torni True
    else:
        return False  # se il cliente non esiste torni False


def pubblicazione_post(email, titolo, descrizione):
    if is_valid_email(email):
        if controlla_email_esistente(email):
            post = Post(email=email, titolo=titolo, descrizione=descrizione)
            dao = PostDAO()

            dao.createPost(post)
            return post


def verifica_campi(titolo, indirizzo, descrizione, num_bagni, num_camere, num_ospiti, metri_quadri, prezzo,
                   periodo_minimo):
    if 30 > len(titolo) > 5:
        if 30 > len(indirizzo) > 5:
            if len(descrizione) > 30:
                if num_bagni > 0:
                    if num_camere > 0:
                        if num_ospiti > 0:
                            if metri_quadri > 0:
                                if prezzo > 0:
                                    return True
    else:
        return False


def pubblicazione_alloggio(titolo, indirizzo, cap, provincia, citta, tipo, descrizione, civico,
                           num_bagni, num_camere, classe_energetica, num_ospiti,
                           metri_quadri, prezzo, periodo_minimo, arredamento,
                           pannelli_fotovoltaici, pannelli_solari, servizi_selezionati, data, mail):
    if verifica_campi(titolo, indirizzo, descrizione, num_bagni, num_camere, num_ospiti, metri_quadri, prezzo,
                      periodo_minimo):
        dao = AnnuncioDAO()
        stanze = num_camere + num_bagni
        dao.inseriscicasa(titolo, tipo, descrizione, num_bagni, num_camere, classe_energetica, num_ospiti, metri_quadri,
                          prezzo, periodo_minimo, arredamento, pannelli_fotovoltaici, pannelli_solari, data, stanze, mail)
        id_alloggio = dao.cercaidcasa()

        for servizio_id in servizi_selezionati:
            dao.inseriscipossedimento(id_alloggio, servizio_id)
        dao.inserisciindirizzo(id_alloggio, indirizzo, cap, citta, provincia, civico)
