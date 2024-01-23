from WebSite.flask.gestioneAffitto.Recensione import Recensione
from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class RecensioneDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()



    #creazione recensione
    def recensione_alloggio(self, recensione):
        if (recensione is None or recensione.get_email() is None or recensione.get_email() == ""
                or recensione.get_id_alloggio() is None or recensione.get_id_alloggio() == ""
                or recensione.get_titolo() is None or recensione.get_titolo() == ""
                or recensione.get_descrizione() is None or recensione.get_descrizione() == ""
                or recensione.get_data_recensione() is None or recensione.get_data_recensione() == ""
                or recensione.get_voto() is None or recensione.get_voto() == ""):
            raise ValueError("Il dipendente e tutti i suoi campi devono essere definiti.")
        query = """
        INSERT INTO recensione
        (id_alloggio, email, titolo, voto, descrizione, data_recensione) 
        VALUES(%s,%s,%s,%s,%s,%s)
        """
        values = (recensione.get_id_alloggio(), recensione.get_email(), recensione.get_titolo(), recensione.get_voto(), recensione.get_descrizione(), recensione.get_data_recensione())
        self.__cursor.execute(query, values)
        self.__connection.commit()







    #updaterecensione
    def updaterecensione(self, id_alloggio, email, titolo, voto, descrizione,data_recensione):
        query = """
                UPDATE recensione
                SET titolo = %s, voto = %s, descrizione = %s, data_recensione = %s
                WHERE id_alloggio = %s AND email = %s
                """
        values = (id_alloggio, email, titolo, voto, descrizione,data_recensione)
        self.__cursor.execute(query, values)
        self.__connection.commit()




    #deleterecensione
    def deleterecensione(self,id_alloggio, email):
        query = """
                DELETE FROM recensione
                WHERE id_alloggio = %s AND email = %s
                """
        values = (id_alloggio, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    def ricercarecensionestudente(self, id_alloggio,email):
        query = """
                SELECT  id_alloggio, email, titolo, voto, descrizione, data_recensione 
                FROM recensione
                WHERE id_alloggio = %s
                AND email = %s 
                """
        value = (id_alloggio,email)
        self.__cursor.execute(query, value)
        result = self.__cursor.fetchone()
        if result:
            rec = Recensione(
                id_alloggio=result[0],
                email=result[1],
                titolo=result[2],
                voto=result[3],
                descrizione=result[4],
                data_recensione=result[5]
            )
            return rec

    def ricercarecensionealloggio(self, id_alloggio):
        query = """
                SELECT  id_alloggio, email, titolo, voto, descrizione, data_recensione 
                FROM recensione
                WHERE id_alloggio = %s
                """
        value = (id_alloggio,)
        self.__cursor.execute(query, value)
        results = self.__cursor.fetchall()
        recensioni = []
        for result in results:
            rec = Recensione(
                id_alloggio=result[0],
                email=result[1],
                titolo=result[2],
                voto=result[3],
                descrizione=result[4],
                data_recensione=result[5]
            )
            recensioni.append(rec)
        return recensioni

    def contarec(self):
        query="""
            SELECT COUNT(*) FROM recensione
        """
        self.__cursor.execute(query)
        results = self.__cursor.fetchone()[0]
        return results