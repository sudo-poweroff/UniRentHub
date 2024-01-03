from WebSite.flask.gestioneAffitto.Affittare import Affittare
from WebSite.flask.test.GestioneConnessione import GestioneConnessione



class AffittareDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()



    #creazione affitto
    def creaaffitto(self, id_alloggio, email, data_inizio, data_fine, numero_carta, data_scadenza, prezzo):
            query = """
                    INSERT INTO Affittare (id_alloggio, email, data_inizio, data_fine, numero_carta,data_scadenza, prezzo)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
            values = (id_alloggio, email, data_inizio, data_fine, numero_carta, data_scadenza, prezzo)
            self.__cursor.execute(query, values)
            self.__connection.commit()




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


