from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione
from WebSite.flask.gestioneAnnunci.Alloggio import Alloggio

class PossedimentoDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def inserisci_possedimento(self, possedimento):
        query = """
                INSERT INTO possedimento (id_alloggio, id_servizio)
                VALUES (%s, %s)
                """
        values = (possedimento.get_id_alloggio(), possedimento.get_id_servizio())
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricerca_by_id_alloggio(self, id_alloggio):
        query = """
                SELECT id_servizio
                FROM possedimento
                WHERE id_alloggio = %s
                """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()

        id_servizi = [result[0] for result in results]

        return id_servizi