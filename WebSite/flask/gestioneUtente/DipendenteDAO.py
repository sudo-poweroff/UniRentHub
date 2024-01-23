from .Dipendente import Dipendente
from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class DipendenteDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def registra_homechecker(self, dipendente):
        if (dipendente is None or dipendente.getEmail() is None or dipendente.getEmail() == ""
                or dipendente.getNome() is None or dipendente.getNome() == ""
                or dipendente.getCognome() is None or dipendente.getCognome() == ""
                or dipendente.getPassword() is None or dipendente.getPassword() == ""):
            raise ValueError("Il dipendente e tutti i suoi campi devono essere definiti.")

        query = """
            INSERT INTO dipendente (email, nome, cognome, tipo_dipendente, password)
            VALUES (%s, %s, %s, 'Homechecker', AES_ENCRYPT(%s, 'ciao'))
        """
        values = (
            dipendente.getEmail(), dipendente.getNome(), dipendente.getCognome(),
            dipendente.getPassword()
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def deleteDipendente(self, email):
        query = """
            DELETE FROM dipendente WHERE email = %s
        """
        values = (email,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def updateDipendente(self, email, password):
        query = """
            UPDATE dipendente
            SET password = AES_ENCRYPT(%s, 'ciao')
            WHERE email = %s
        """
        values = (password, email)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricercaDip(self, email, password):
        query = """
            SELECT *
            FROM dipendente
            WHERE email = %s
            AND password = AES_ENCRYPT(%s, 'ciao')
        """
        values = (email, password)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            dipendente = Dipendente(
                email=result[0],
                nome=result[1],
                cognome=result[2],
                tipo_dipendente=result[3],
                password=password
            )
            return dipendente
        else:
            return None

    def ricercaTdipendente(self, tipologia):
        query = """
                SELECT *
                FROM dipendente
                WHERE tipo_dipendente = %s
                """
        values = (tipologia,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()

        dipendenti_homechecker = []
        for result in results:
            dipendente = Dipendente(
                email=result[0],
                nome=result[1],
                cognome=result[2],
                tipo_dipendente=result[3],
                password=result[4]
            )
            dipendenti_homechecker.append(dipendente)
        return dipendenti_homechecker

    def elimina_homechecker(self, email):
        query = """
                DELETE FROM dipendente
                WHERE email = %s
                """
        values = (email,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def contadip(self):
        query = """
                        SELECT COUNT(*) FROM dipendente
                        WHERE  tipo_dipendente='Homechecker'
                        """
        self.__cursor.execute(query)
        results = self.__cursor.fetchone()[0]
        return results
