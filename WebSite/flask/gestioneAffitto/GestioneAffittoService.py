from WebSite.flask.gestioneAffitto.PrenotazioneDAO import PrenotazioneDAO


def insert_data_byId(prenotazione):
    dao = PrenotazioneDAO()
    dao.creaprenotazione(prenotazione=prenotazione)
    print("prenotazione creata! " + prenotazione.get_data_visita())
