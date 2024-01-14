from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class PartecipazioneDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def aggiungi_partecipazione(self, id_chat, email):
        query = """
            INSERT INTO partecipazione (id_chat, email) VALUES (%s, %s);
        """
        values = (id_chat, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Partecipazione aggiunta.")

    def elimina_partecipazione(self, id_chat, email):
        query = """
            DELETE FROM partecipazione WHERE id_chat = %s AND email = %s;
        """
        values = (id_chat, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Partecipazione eliminata.")

    def ottieni_partecipazioni_per_chat(self, id_chat):
        query = """
            SELECT * FROM partecipazione WHERE id_chat = %s;
        """
        values = (id_chat,)
        self.__cursor.execute(query, values)
        risultato = self.__cursor.fetchall()
        return risultato