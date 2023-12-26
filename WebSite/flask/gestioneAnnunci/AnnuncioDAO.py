from WebSite.flask.test.GestioneConnessione import GestioneConnessione
class AnnuncioDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()
    def visualizza(self):
        query = """
                SELECT * FROM alloggio
                WHERE disponibilità=1
                """
        self.__cursor.execute(query)
        alloggi = self.__cursor.fetchall()  # Ottieni tutti i risultati della query
        return alloggi
    def visualizzaimg(self,id):
        query ="""
                SELECT * FROM immagine 
                where id_alloggio = %s
                LIMIT 1       
        """
        values = (id,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()
        return result

    def visualizzaannuncio(self,id_alloggio):
        query="""
        SELECT * FROM alloggio
        WHERE id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()
        return result

    def visualizzaservizi(self,id_alloggio):
        query="""
        SELECT descrizione FROM servizi,possedimento
        WHERE servizi.id_servizio = possedimento.id_servizio
        and possedimento.id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
        return result

    def visualizzaimmagini(self,id_alloggio):
        query="""
        SELECT path FROM immagine
        WHERE id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
        return result
