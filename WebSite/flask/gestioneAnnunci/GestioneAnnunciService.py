import re
from flask import Flask, flash

from .AlloggioDAO import AlloggioDAO
from .IndirizzoDAO import IndirizzoDAO
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
        dao = AlloggioDAO()
        stanze = num_camere + num_bagni
        dao.inseriscicasa(titolo, tipo, descrizione, num_bagni, num_camere, classe_energetica, num_ospiti, metri_quadri,
                          prezzo, periodo_minimo, arredamento, pannelli_fotovoltaici, pannelli_solari, data, stanze, mail)
        id_alloggio = dao.cercaidcasa()

        for servizio_id in servizi_selezionati:
            dao.inseriscipossedimento(id_alloggio, servizio_id)
        dao.inserisciindirizzo(id_alloggio, indirizzo, cap, citta, provincia, civico)


def ricerca_alloggio(citta):
    dao1 = IndirizzoDAO()
    dao2 = AlloggioDAO()

    # Ottieni una lista di ID alloggi per la città specificata
    id_alloggi = dao1.ricerca_citta(citta=citta)
    for i in id_alloggi:
        print("ID SERVICE:" + str(i[0]))

    # Inizializza una lista vuota per gli alloggi
    alloggi = []
    print("Sono FUORI")
    # Itera su ogni ID alloggio e cerca l'alloggio associato
    for i in id_alloggi:
        id_alloggio = i[0] #inserisco i[0] in id_alloggio, in modo tale da scorrere sempre il prossimo id
        alloggio = dao2.visualizzaannuncio(id_alloggio)
        print("nome ALLOGGIO: " + alloggio.get_titolo())
        # Aggiungi l'alloggio alla lista
        alloggi.append(alloggio)

    return alloggi
