from WebSite.flask.test.GestioneConnessione import GestioneConnessione

class IndirizzoDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def ricerca_citta(self, citta):
        query = """
                SELECT id_alloggio FROM indirizzo
                WHERE citta = %s
                """
        values = (citta, )
        self.__cursor.execute(query, values)
        id_alloggi = self.__cursor.fetchall()  # Ottieni tutti i risultati della query
        for i in id_alloggi:
            print("ID:" + str(i[0]))
        return id_alloggi
