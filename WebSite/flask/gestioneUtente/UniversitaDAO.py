from .Cliente import Cliente
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class UniversitaDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()




