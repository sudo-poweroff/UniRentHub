from WebSite.flask.gestioneAnnunci.Servizi import Servizi
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class ServiziDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def visualizzaservizidisponibili(self):
        query = """
        SELECT descrizione FROM servizi
        """
        self.__cursor.execute(query)
        results = self.__cursor.fetchall()

        servizi = []

        for row in results:
            servizio = Servizi(
                descrizione=row[0]
            )
            servizi.append(servizio)
        return servizi

    def visualizza_servizio_by_id(self, id_servizio):
        query = """
        SELECT descrizione
        FROM servizi
        WHERE id_servizio = %s
        """
        values = (id_servizio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        return result
