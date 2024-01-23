from .Cliente import Cliente
from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class IscrizioneDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def create_iscrizione(self, iscrizione):
        query = """
                    INSERT INTO iscrizione (denominazione, email)
                    VALUES (%s, %s)
                """
        values = (iscrizione.getDenominazione(), iscrizione.getEmail())

        self.__cursor.execute(query, values)
        self.__connection.commit()


