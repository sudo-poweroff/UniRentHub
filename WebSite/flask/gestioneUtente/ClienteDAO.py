from .Cliente import Cliente
from WebSite.flask.test.GestioneConnessione import GestioneConnessione
from WebSite.flask.gestioneAnnunci.Alloggio import Alloggio
from datetime import datetime
class ClienteDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()


    def createCliente(self, cliente):
        query = """
            INSERT INTO cliente (email, nome, cognome, tipo_utente, data_nascita, numero_carta, mese_scadenza, anno_scadenza, verificato, password, data_blocco)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NULL)
        """
        values = (
            cliente.getEmail(), cliente.getNome(), cliente.getCognome(),
            cliente.getTipo(), cliente.getDataNascita(),
            cliente.getNumeroCarta(), cliente.getMeseScadenza(), cliente.getAnnoScadenza(),
            0,  # Aggiunto il valore per verificato
            cliente.getPassword()
        )

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def deleteCliente(self, email):
        query = """
            DELETE FROM cliente WHERE email = %s
        """

        values = (email,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def updateCliente(self, email, password, numero_carta, data_scadenza, data_blocco):
        query = """
            UPDATE cliente
            SET password = %s, numero_carta = %s, data_scadenza = %s, data_blocco = %s
            WHERE email = %s
        """

        values = (password, numero_carta, data_scadenza, data_blocco, email)

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricercaEmailC(self, email):
        query = """
            SELECT email, nome, cognome, tipo_utente, data_nascita, numero_carta, mese_scadenza, anno_scadenza, verificato, password, data_blocco
            FROM cliente
            WHERE email = %s
        """

        values = (email,)

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
                mese_scadenza=result[6],
                anno_scadenza=result[7],
                verificato=result[8],
                password=result[9],
                data_blocco=result[10]
            )
            return cliente
        else:
            return None

    def accesso(self, email, pwd):
        query = """
            SELECT *
            FROM cliente
            WHERE email = %s
            AND password = %s
        """

        values = (email, pwd)

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
                mese_scadenza=result[6],
                anno_scadenza=result[7],
                verificato=result[8],
                password=result[9],
                data_blocco=result[10]
            )
            return cliente
        else:
            return None

    def universitabystudente(self, email):
        query ="""
            SELECT iscrizione.denominazione
            FROM iscrizione
            WHERE email = %s
        """

        values = (email,)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            return result
        else:
            return None

    def cercacaseproprietario(self, email):
        query="""
        SELECT * FROM alloggio
        WHERE email_loc = %s
        """
        values = (email,)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
        alloggi = []
        for r in result:
            alloggio = Alloggio(
                id_alloggio=r[0],
                tipo_alloggio=r[1],
                disponibilita=r[2],
                titolo=r[3],
                mq=r[4],
                n_camere_letto=r[5],
                n_bagni=r[6],
                classe_energetica=r[7],
                arredamenti=r[8],
                data_publicazione=r[9],
                pannelli_solari=r[10],
                pannelli_fotovoltaici=r[11],
                descrizione=r[12],
                verifica=r[13],
                prezzo=r[14],
                n_ospiti=r[15],
                n_stanze=r[16],
                tasse=r[17],
                email_dip=r[18],
                email_loc=r[19],
                data_verifica=r[20],
            )
            alloggi.append(alloggio)
        return alloggi

    def cercacasastudente(self, email, data):
        query="""
        SELECT id_alloggio FROM affittare
        WHERE affittare.email = %s
        AND data_fine > %s
        """
        values = (email, data)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            return result[0]
        else:
            return None

    def aggiornaCliente(self, email, nome, cognome, password, numero_carta, anno, mese):
        try:
            query = """
                UPDATE cliente
                SET nome = %s, cognome = %s, password = %s, numero_carta = %s, anno_scadenza = %s, mese_scadenza = %s
                WHERE email = %s
            """

            values = (nome, cognome, password, numero_carta, anno, mese, email)

            self.__cursor.execute(query, values)
            self.__connection.commit()

            return True  # Restituisce True se l'aggiornamento ha avuto successo
        except Exception as e:
            print(f"Errore durante l'aggiornamento del cliente: {str(e)}")
            return False  # Restituisce False in caso di errore

    def update_verificato(self, email):
        query = """
                UPDATE cliente
                SET verificato = 1
                WHERE email = %s
            """
        values = (email,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def blocca_utente(self, email):
        try:
            data_corrente = datetime.now().strftime("%Y-%m-%d")
            query = """
                    UPDATE cliente
                    SET data_blocco = %s
                    WHERE email = %s
                    """
            values = (data_corrente, email)
            self.__cursor.execute(query, values)
            self.__connection.commit()
            print(data_corrente)
            return True  # Restituisce True se l'aggiornamento ha avuto successo
        except Exception as e:
            print(f"Errore durante l'aggiornamento del cliente: {str(e)}")
            return False  # Restituisce False in caso di errore

    def rimuovi_blocco_utente(self, email):
        query = """
                UPDATE cliente 
                SET data_blocco = NULL 
                WHERE email = %s
                """
        values = (email, )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def resetDataBloccoCliente(self, email):
        query = """
            UPDATE cliente
            SET data_blocco = NULL
            WHERE email = %s
        """

        values = (email,)

        self.__cursor.execute(query, values)
        self.__connection.commit()
