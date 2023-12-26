from .Cliente import Cliente
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class ClienteDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def createCliente(self, cliente):
        query= """
            INSERT INTO cliente (email, nome, cognome, tipo_utente, data_nascita, numero_carta, data_scadenza, verificato, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            cliente.getEmail(), cliente.getNome(), cliente.getCognome(),
            cliente.getTipo(), cliente.getDataNascita(),
            cliente.getNumeroCarta(), cliente.getDataScadenza(),
            0,  # Aggiunto il valore per verificato
            cliente.getPassword()
        )

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def deleteCliente (self, email):
        query="""
            DELETE FROM cliente WHERE email = %s
        """

        values = (email,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def updateCliente(self, email, password, numero_carta, data_scadenza):
        query="""
            UPDATE cliente
            SET password =%s, numero_carta =%s, data_scadenza =%s
            WHERE email =%s
        """

        values = (password, numero_carta, data_scadenza, email)

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricercaEmailC(self, email):
        query="""
            SELECT *
            FROM cliente
            WHERE email =%s
        """

        values =(email,)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            cliente = Cliente(
                email=result[0],
                nome=result[1],
                cognome=result[2],
                tipo_utente=result[3],
                data_nascita=result[4],
                numero_carta=result[5],
                data_scadenza=result[6],
                verificato=result[7],
                password=result[8]
            )
            return cliente
        else:
            return None

    def accesso(self, email,pwd):
        query="""
            SELECT *
            FROM cliente
            WHERE email =%s
            AND password = %s
        """

        values =(email,pwd)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            cliente = Cliente(
                email=result[0],
                nome=result[1],
                cognome=result[2],
                tipo_utente=result[3],
                data_nascita=result[4],
                numero_carta=result[5],
                data_scadenza=result[6],
                verificato=result[7],
                password=result[8]
            )
            return cliente
        else:
            return None



