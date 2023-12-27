from .Dipendente import Dipendente
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class DipendenteDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def registra_homechecker(self, dipendente):
        dipendente.setTipo('Homechecker')
        query = """
            INSERT INTO dipendente (email, nome, cognome, tipo_dipendente, password)
            VALUES (%s, %s, %s, 'Homechecker', %s)
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
            SET password = %s
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
            AND password = %s
        """
        values = (email,password)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            dipendente = Dipendente(
                email=result[0],
                nome=result[1],
                cognome=result[2],
                tipo_dipendente=result[3],
                password=result[4]
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

