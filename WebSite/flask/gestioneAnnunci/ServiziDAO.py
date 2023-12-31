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
        SELECT *
        FROM servizi
        WHERE id_servizio = %s
        """
        values = (id_servizio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()

        servizi = []

        for row in result:
            servizo = Servizi(
                id_servizio=row[0],
                descrizione=row[1]
            )
            servizi.append(servizo)

        return servizi

    def visualizza_servizi(self, id_alloggio):
        query = """
        SELECT descrizione FROM servizi,possedimento
        WHERE servizi.id_servizio = possedimento.id_servizio
        and possedimento.id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()

        servizi = []

        for row in results:
            servizio = Servizi(
                descrizione=row[0]
            )
            servizi.append(servizio)
        return servizi

