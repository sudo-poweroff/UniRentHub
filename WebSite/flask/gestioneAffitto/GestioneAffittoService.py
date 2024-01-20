from WebSite.flask.gestioneAffitto.Affittare import Affittare
from WebSite.flask.gestioneAffitto.AffittareDAO import AffittareDAO
from WebSite.flask.gestioneAffitto.PrenotazioneDAO import PrenotazioneDAO


def insert_data_byId(prenotazione):
    dao = PrenotazioneDAO()
    dao.creaprenotazione(prenotazione=prenotazione)
    print("prenotazione creata! " + prenotazione.get_data_visita())


def delete_data_byId(id_alloggio, data_visita):
    dao = PrenotazioneDAO()
    dao.deleteprenotazione(id_alloggio=id_alloggio, data_visita=data_visita)
    print("cancellato!")


def update_disponibilita(id_alloggio, data_visita):
    dao = PrenotazioneDAO()
    print("sono qui")
    dao.update_disponibilita(id_alloggio=id_alloggio, data_visita=data_visita)


def ricerca_data_disponibile(id_alloggio):
    dao = PrenotazioneDAO()
    prenotazione = dao.ricerca_alloggi_disponibili(id_alloggio=id_alloggio)
    return prenotazione


# verifica se ci sono date disponibili
def date_disponibili_pagamento(id_alloggio, data_inizio, data_fine):
    dao = AffittareDAO()
    val = dao.verifica_prenotazioni(id_alloggio=id_alloggio, data_inizio=data_inizio, data_fine=data_fine)
    return val


# creazione nuovo affitto
def affitto_alloggio_cliente(id_alloggio, email, data_inizio, data_fine, numero_carta, mese_scadenza, anno_scadenza,
                             prezzo):
    affittare = Affittare(id_alloggio=id_alloggio, email=email, data_inizio=data_inizio, data_fine=data_fine,
                          numero_carta=numero_carta, mese_scadenza=mese_scadenza, anno_scadenza=anno_scadenza,
                          prezzo=prezzo)
    dao = AffittareDAO()
    try:
        dao.creaaffitto(affittare)
        return affittare
    except ValueError:
        return


#ottieni date da affittare dato un id_alloggio
def ottieni_date_per_alloggio_byId(id_alloggio):
    affittare_dao = AffittareDAO()
    date_per_alloggio = affittare_dao.ottieni_date_per_alloggio(id_alloggio=id_alloggio)
    print(date_per_alloggio)
    return date_per_alloggio
