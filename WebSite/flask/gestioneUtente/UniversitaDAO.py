from .Cliente import Cliente
from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class UniversitaDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def cercatutti(self):
        query="""
        SELECT denominazione FROM università
        
        """
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        return result





