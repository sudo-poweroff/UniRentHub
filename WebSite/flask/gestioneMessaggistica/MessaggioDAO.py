from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class MessaggioDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def inserisci_messaggio(self, email, id_chat, contenuto):
        query = """
            INSERT INTO messaggio (email, id_chat, contenuto) VALUES (%s, %s, %s);
        """
        values = (email, id_chat, contenuto)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Nuovo messaggio inserito.")

    def seleziona_tutti_i_messaggi(self):
        query = """
            SELECT * FROM messaggio;
        """
        self.__cursor.execute(query)
        risultato = self.__cursor.fetchall()
        return risultato

    def seleziona_messaggio_per_id(self, messaggio_id):
        query = """
            SELECT * FROM messaggio WHERE id_messaggio = %s;
        """
        values = (messaggio_id,)
        self.__cursor.execute(query, values)
        risultato = self.__cursor.fetchone()
        return risultato

    def aggiorna_contenuto_messaggio(self, messaggio_id, nuovo_contenuto):
        query = """
            UPDATE messaggio SET contenuto = %s WHERE id_messaggio = %s;
        """
        values = (nuovo_contenuto, messaggio_id)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Contenuto del messaggio aggiornato.")

    def elimina_messaggio(self, messaggio_id):
        query = """
            DELETE FROM messaggio WHERE id_messaggio = %s;
        """
        values = (messaggio_id,)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Messaggio eliminato.")
