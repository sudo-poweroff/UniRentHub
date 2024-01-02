from WebSite.flask.gestioneAffitto.Prenotazione import Prenotazione
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class PrenotazioneDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    #creazione prenotazione
    def creaprenotazione(self, prenotazione):
        query = """ 
                INSERT INTO prenotazione(id_alloggio, email, data_visita, disponibilita)
                VALUES(%s, %s, %s, %s)
                """
        values = (
            prenotazione.get_id_alloggio(),
            prenotazione.get_email(),
            prenotazione.get_data_visita(),
            True
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    #update prenotazione
    def updateprenotazione(self, id_alloggio, email, data_visita):
        query = """
                UPDATE prenotazione
                SET data_visita = %s
                WHERE id_alloggio = %s AND email = %s
                """
        values = (data_visita,id_alloggio, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    #cancella prenotazione
    def deleteprenotazione(self, id_alloggio, email):
        query = """
                DELETE FROM affittare
                WHERE id_alloggio = %s AND email = %s
                """
        values = (id_alloggio, email)
        self.__cursor.execute(query,  values)
        self.__connection.commit()

    #ricerca prenotazioni
    def ricercaprenotazione(self, id_alloggio):
        query = """
                SELECT email, data_visita 
                FROM prenotazione
                WHERE id_alloggio = %s
                """
        value = (id_alloggio,)
        self.__cursor.execute(query, value)
        results = self.__cursor.fetchall()

        prenotazioni = []
        for result in results:
            prenotazione = Prenotazione(
                email= result[0],
                data_visita=result[1]
            )
            prenotazioni.append(prenotazione)
        return prenotazioni
