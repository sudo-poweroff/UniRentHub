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
    dao.update_disponibilita(id_alloggio=id_alloggio,data_visita=data_visita)

def ricerca_data_disponibile(id_alloggio):
    dao = PrenotazioneDAO()
    prenotazione = dao.ricerca_alloggi_disponibili(id_alloggio=id_alloggio)
    return prenotazione