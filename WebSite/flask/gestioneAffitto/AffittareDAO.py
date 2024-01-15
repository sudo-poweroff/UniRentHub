from datetime import datetime, timedelta

from WebSite.flask.gestioneAffitto.Affittare import Affittare
from WebSite.flask.test.GestioneConnessione import GestioneConnessione



class AffittareDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()


    # Update affitto
    def updateaffittare(self, id_alloggio, email, data_inizio, data_fine, numero_carta, data_scadenza, prezzo):
        query = """
                UPDATE Affittare
                SET data_inizio = %s, data_fine = %s, numero_carta = %s, data_scadenza = %s, prezzo = %s
                WHERE id_alloggio = %s AND email = %s
                """
        values = (data_inizio, data_fine, numero_carta, data_scadenza, prezzo, id_alloggio, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    # Delete affitto
    def deleteaffittare(self, id_alloggio, email):
        query = """
                DELETE FROM Affittare
                WHERE id_alloggio = %s AND email = %s
                """
        values = (id_alloggio, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    # Ricerca affitto
    def ricercaaffitto(self, id_alloggio):

        query = """
                SELECT id_alloggio, email, data_inizio, data_fine, numero_carta,data_scadenza, prezzo 
                FROM Affittare
                WHERE id_alloggio = %s
                """
        value = (id_alloggio,)
        self.__cursor.execute(query, value)
        results = self.__cursor.fetchall()

        affitti = []
        for result in results:

            affitto = Affittare(
                id_alloggio=result[0],
                email=result[1],
                data_inizio=result[2],
                data_fine=result[3],
                numero_carta=result[4],
                data_scadenza=result[5],
                prezzo=result[6]

            )

            affitti.append(affitto)

        return affitti

        # Verifica se ci sono prenotazioni nelle date specificate

    #verifica prenotazione
    def verifica_prenotazioni(self, id_alloggio, data_inizio, data_fine):
        query = """
                   SELECT COUNT(*)
                   FROM Affittare
                   WHERE id_alloggio = %s
                   AND (data_inizio BETWEEN %s AND %s OR data_fine BETWEEN %s AND %s)
                   """
        values = (id_alloggio, data_inizio, data_fine, data_inizio, data_fine)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()
        return result[0] > 0  # Restituisce True se ci sono prenotazioni, altrimenti False

    #creazione affitto
    def creaaffitto(self, id_alloggio, email, data_inizio, data_fine, numero_carta, mese_scadenza, anno_scadenza,
                    prezzo):
        query = """
                INSERT INTO affittare (id_alloggio, email, data_inizio, data_fine, numero_carta, mese_scadenza, anno_scadenza, prezzo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
        values = (id_alloggio, email, data_inizio, data_fine, numero_carta, mese_scadenza, anno_scadenza, prezzo)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    def ottieni_date_per_alloggio(self, id_alloggio):
        query = """
                SELECT data_inizio, data_fine
                FROM Affittare
                WHERE id_alloggio = %s
                """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()

        date = []
        for result in results:
            data_inizio = result[0]
            data_fine = result[1]
            date.append(data_inizio)
            date.append(data_fine)

        return date

    def ricercaaffitto_per_email(self, email):
        query = """
                SELECT id_alloggio
                FROM Affittare
                WHERE email = %s
                """
        value = (email,)
        self.__cursor.execute(query, value)
        results = self.__cursor.fetchall()

        affitti = []
        for result in results:
            affitto = Affittare(
                id_alloggio=result[0],
                email=email  # Usiamo l'email passata come parametro
            )
            affitti.append(affitto)

        return affitti

    def cercadataaffitto(self,email,id_alloggio):
        query = """
        SELECT data_inizio
        FROM Affittare
        WHERE email=%s
        AND id_alloggio = %s
        """
        values = (email,id_alloggio)
        self.__cursor.execute(query,values)
        result = self.__cursor.fetchone()
        return result[0]