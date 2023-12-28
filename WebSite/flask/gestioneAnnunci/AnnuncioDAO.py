from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class AnnuncioDAO:
    # ciccioègay
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

    def visualizzaimg(self, id):
        query = """
                SELECT * FROM immagine 
                where id_alloggio = %s
                LIMIT 1       
        """
        values = (id,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()
        return result

    def visualizzaannuncio(self, id_alloggio):
        query = """
        SELECT * FROM alloggio
        WHERE id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()
        return result

    def visualizzaservizi(self, id_alloggio):
        query = """
        SELECT descrizione FROM servizi,possedimento
        WHERE servizi.id_servizio = possedimento.id_servizio
        and possedimento.id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
        return result

    def visualizzaimmagini(self, id_alloggio):
        query = """
        SELECT path FROM immagine
        WHERE id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
        return result

    def visualizzaservizidisponibili(self):
        query = """
        SELECT descrizione FROM servizi
        """
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        return result

    def cercaidcasa(self):
        query = """
        SELECT MAX(id_alloggio) FROM alloggio
        """
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        if result and len(result) > 0:
            return result[0]  # Restituisci solo il valore dell'ID massimo
        else:
            return None

    def inseriscicasa(self, titolo, tipo, descrizione, num_bagni, num_camere, classe_energetica, num_ospiti,
                      metri_quadri, prezzo, periodo_minimo, arredamento, pannelli_fotovoltaici, pannelli_solari,
                      data, stanze, mail):
        query = """
                INSERT INTO Alloggio (tipo_alloggio, disponibilità, titolo, mq, n_camere_letto, n_bagni,
                                      classe_energetica, arredamenti, data_pubblicazione, pannelli_solari,
                                      pannelli_fotovoltaici, descrizione, verifica, prezzo, n_ospiti, n_stanze, tasse, 
                                      email_loc)
                                      VALUES
                                      (%s, 1,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, %s,%s,%s,%s)
                """
        tasse=10
        values = (tipo, titolo, metri_quadri, num_camere, num_bagni, classe_energetica, arredamento, data,
                  pannelli_solari, pannelli_fotovoltaici, descrizione, prezzo, num_ospiti, stanze,tasse, mail)

        self.__cursor.execute(query, values)

    def inseriscipossedimento(self, id_alloggio, id_servizio):
        query = """
        INSERT INTO possedimento (id_servizio,id_alloggio)VALUES
        (%s,%s) 
        """
        values = (id_servizio, id_alloggio)
        self.__cursor.execute(query, values)

    def inserisciindirizzo(self, id_alloggio, indirizzo, cap, citta, provincia, civico):
        query = """
        INSERT INTO indirizzo (id_alloggio,via,cap,citta,provincia,civico)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        values = (id_alloggio, indirizzo, cap, citta, provincia, civico)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()
#aa