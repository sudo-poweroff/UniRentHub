from WebSite.flask.gestioneAffitto.Recensione import Recensione
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class RecensioneDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()



    #creazione recensione
    def recensione_alloggio(self, id_alloggio, email, titolo, voto, descrizione, data):
        query = """
        INSERT INTO recensione
        (id_alloggio, email, titolo, voto, descrizione, data_recensione) 
        VALUES(%s,%s,%s,%s,%s,%s)
        """
        values = (id_alloggio, email, titolo, voto, descrizione, data)
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


    #ricercarecensioni di un alloggio
    def ricercarecensione(self, id_alloggio):
        query = """
                SELECT  id_alloggio, email, titolo, voto, descrizione, data_recensione 
                FROM recensione
                WHERE id_alloggio = %s 
                """
        value = (id_alloggio,)
        self.__cursor.execute(query, value)
        results = self.__cursor.fetchall()


        recensioni= []
        for result in results:
            recensione = Recensione(
                id_alloggio=result[0],
                email=result[1],
                titolo=result[2],
                voto=result[3],
                descrizione=result[4],
                data_recensione=result[5]
            )
            recensioni.append(recensione)
        return recensioni

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


