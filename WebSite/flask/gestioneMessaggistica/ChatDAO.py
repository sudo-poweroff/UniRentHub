from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class ChatDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def inserisci_chat(self, titolo):
        query = """
            INSERT INTO chat (titolo) VALUES (%s);
        """
        values = (titolo,)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Nuova chat inserita.")

    def seleziona_tutte_le_chats(self):
        query = """
            SELECT * FROM chat;
        """
        self.__cursor.execute(query)
        risultato = self.__cursor.fetchall()
        return risultato

    def seleziona_chat_per_id(self, chat_id):
        query = """
            SELECT * FROM chat WHERE id_chat = %s;
        """
        values = (chat_id,)
        self.__cursor.execute(query, values)
        risultato = self.__cursor.fetchone()
        return risultato

    def aggiorna_titolo_chat(self, chat_id, nuovo_titolo):
        query = """
            UPDATE chat SET titolo = %s WHERE id_chat = %s;
        """
        values = (nuovo_titolo, chat_id)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Titolo della chat aggiornato.")

    def elimina_chat(self, chat_id):
        query = """
            DELETE FROM chat WHERE id_chat = %s;
        """
        values = (chat_id,)
        self.__cursor.execute(query, values)
        self.__connection.commit()
        print("Chat eliminata.")