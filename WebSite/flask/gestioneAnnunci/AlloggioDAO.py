from WebSite.flask.gestioneAnnunci.Alloggio import Alloggio
from WebSite.flask.gestioneAnnunci.Indirizzo import Indirizzo
from WebSite.flask.gestioneAnnunci.Servizi import Servizi
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class AlloggioDAO:
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

    def visualizzaannuncio(self, id):
        query = """
            SELECT * FROM alloggio
            WHERE id_alloggio = %s
        """
        values = (id,)  # Assicurati che i valori siano in una tupla
        print(str(id)+"DAO")
        print("DAO Join")
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            print("Result from query:", result)  # Aggiungi questa linea per stampare i valori ottenuti dalla query
            alloggio = Alloggio(
                id_alloggio=result[0],
                tipo_alloggio=result[1],
                disponibilita=result[2],
                titolo=result[3],
                mq=result[4],
                n_camere_letto=result[5],
                n_bagni=result[6],
                classe_energetica=result[7],
                arredamenti=result[8],
                data_publicazione=result[9],
                pannelli_solari=result[10],
                pannelli_fotovoltaici=result[11],
                descrizione=result[12],
                verifica=result[13],
                prezzo=result[14],
                n_ospiti=result[15],
                n_stanze=result[16],
                tasse=result[17],
                email_dip=result[18],
                email_loc=result[19],
                data_verifica=result[20]
            )
            return alloggio
        else:
            return None

    def visualizzaservizi(self, id_alloggio):
        query = """
        SELECT descrizione FROM servizi,possedimento
        WHERE servizi.id_servizio = possedimento.id_servizio
        and possedimento.id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()

        servizi = []

        for row in results:
            servizio = Servizi(
                descrizione=row[0]
            )
            servizi.append(servizio)
        return servizi


    def visualizzaimmagini(self, id_alloggio):
        query = """
        SELECT path FROM immagine
        WHERE id_alloggio = %s
        """
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
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

    def inseriscicasa(self, alloggio):
        query = """
                INSERT INTO Alloggio (tipo_alloggio, disponibilità, titolo, mq, n_camere_letto, n_bagni,
                                      classe_energetica, arredamenti, data_pubblicazione, pannelli_solari,
                                      pannelli_fotovoltaici, descrizione, verifica, prezzo, n_ospiti, n_stanze, tasse, 
                                      email_loc)
                                      VALUES
                                      (%s, 1,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, %s, %s,%s,%s,%s)
                """
        tasse=10
        values = (alloggio.get_id_alloggio(), alloggio.get_disponibilita(), alloggio.get_titolo(), alloggio.get_mq(), alloggio.get_n_camere_letto(), alloggio.get_n_bagni(), alloggio.get_classe_energetica(),
                  alloggio.get_arredamenti(), alloggio.get_data_pubblicazione(), alloggio.get_pannelli_solari(), alloggio.get_pannelli_fotovoltaici(), alloggio.get_descrizione(), alloggio.get_verifica(),
                  alloggio.get_prezzo(), alloggio.get_n_ospiti(), alloggio.get_n_stanze(), alloggio.get_tasse(), alloggio.get_email_loc())

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



    def homecheckgood(self, id_alloggio):
        query = """
                     UPDATE alloggio
                     SET verifica = 1
                     WHERE id_alloggio = %s
                     """
        self.__cursor.execute(query, (id_alloggio,))
        self.__connection.commit()

    def homecheck(self):
        query = """
                   SELECT * FROM alloggio
                   WHERE verifica=0
                   """
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()  # Ottieni tutti i risultati della query
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
                data_verifica=r[20]
            )
            alloggi.append(alloggio)
        return alloggi

    def create_alloggio(self, alloggio):
        if (alloggio is None or alloggio.get_disponibilita() is None or alloggio.get_disponibilita() == "" or
                alloggio.get_titolo() is None or alloggio.get_titolo() == "" or
                alloggio.get_mq() is None or alloggio.get_mq() == "" or
                alloggio.get_n_bagni() is None or alloggio.get_n_bagni() == "" or
                alloggio.get_n_camere_letto() is None or alloggio.get_n_camere_letto() == "" or
                alloggio.get_classe_energetica() is None or alloggio.get_classe_energetica() == "" or
                alloggio.get_arredamenti() is None or alloggio.get_arredamenti() == "" or
                alloggio.get_data_publicazione() is None or alloggio.get_data_publicazione() == "" or
                alloggio.get_pannelli_fotovoltaici() is None or alloggio.get_tipo_alloggio() == "" or
                alloggio.get_descrizione() is None or alloggio.get_descrizione() == "" or
                alloggio.get_prezzo() is None or alloggio.get_prezzo() == "" or
                alloggio.get_pannelli_solari() is None or alloggio.get_pannelli_solari()=="" or
                alloggio.get_n_ospiti() is None or alloggio.get_n_ospiti()=="" or
                alloggio.get_tasse() is None or alloggio.get_tasse()=="" or
                alloggio.get_email_dip() is None or alloggio.get_email_dip()=="" or
                alloggio.get_email_loc() is None or alloggio.get_email_loc()=="" or
                alloggio.get_data_verifica() is None or alloggio.get_data_verifica()=="" or
                alloggio.get_n_stanze() is None or alloggio.get_n_stanze()==""):
            raise ValueError("L'Annuncio e tutti i suoi campi devono essere definiti.")

        query = """
            INSERT INTO alloggio
            (tipo_alloggio, disponibilità, titolo, mq, n_camere_letto, n_bagni, classe_energetica, arredamenti, 
            data_pubblicazione, pannelli_solari, pannelli_fotovoltaici, descrizione, verifica, prezzo, n_ospiti, n_stanze, 
            tasse, email_dip, email_loc, data_verifica)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            alloggio.get_tipo_alloggio(),  # tipo_alloggio
            1,  # disponibilità
            alloggio.get_titolo(),  # titolo
            alloggio.get_mq(),  # mq
            alloggio.get_n_camere_letto(),  # n_camere_letto
            alloggio.get_n_bagni(),  # n_bagni
            alloggio.get_classe_energetica(),  # classe_energetica
            alloggio.get_arredamenti(),  # arredamenti
            alloggio.get_data_publicazione(),  # data_pubblicazione
            alloggio.get_pannelli_solari(),  # pannelli_solari
            alloggio.get_pannelli_fotovoltaici(),  # pannelli_fotovoltaici
            alloggio.get_descrizione(),  # descrizione
            0,  # verifica
            alloggio.get_prezzo(),  # prezzo
            alloggio.get_n_ospiti(),  # n_ospiti
            alloggio.get_n_stanze(),  # n_stanze
            alloggio.get_tasse(),  # tasse
            None,  # email_dip
            alloggio.get_email_loc(),  # email_loc
            None  # data_verifica
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def modifica_alloggio(self, id_alloggio, alloggio):
        query = """
            UPDATE alloggio
            SET
                tipo_alloggio = %s,
                titolo = %s,
                mq = %s,
                n_camere_letto = %s,
                n_bagni = %s,
                classe_energetica = %s,
                arredamenti = %s,
                pannelli_solari = %s,
                pannelli_fotovoltaici = %s,
                descrizione = %s,
                prezzo = %s,
                n_ospiti = %s,
                n_stanze = %s,
                tasse = %s
            WHERE
                id_alloggio = %s
        """
        values = (
            alloggio.get_tipo_alloggio(),  # tipo_alloggio
            alloggio.get_titolo(),  # titolo
            alloggio.get_mq(),  # mq
            alloggio.get_n_camere_letto(),  # n_camere_letto
            alloggio.get_n_bagni(),  # n_bagni
            alloggio.get_classe_energetica(),  # classe_energetica
            alloggio.get_arredamenti(),  # arredamenti
            alloggio.get_pannelli_solari(),  # pannelli_solari
            alloggio.get_pannelli_fotovoltaici(),  # pannelli_fotovoltaici
            alloggio.get_descrizione(),  # descrizione
            alloggio.get_prezzo(),  # prezzo
            alloggio.get_n_ospiti(),  # n_ospiti
            alloggio.get_n_stanze(),  # n_stanze
            alloggio.get_tasse(),  # tasse
            id_alloggio  # id_alloggio
        )
        print("MODIFCO DAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        result = self.__cursor.execute(query, values)
        self.__connection.commit()
        if result:
            print("FATTO: " + result)
        else:
            print("NONEEEE")

    def elimina_alloggio(self, id_alloggio):
        query = "DELETE FROM alloggio WHERE id_alloggio = %s"
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricerca_prezzo_minore_per_citta(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_prezzo_maggiore_per_citta(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            ORDER BY a.prezzo DESC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_per_classe_energetica(self, citta):
        classe_energetica_minima = 'A++'
        classe_energetica_massima = 'D'

        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica BETWEEN %s AND %s
            ORDER BY a.classe_energetica ASC, a.prezzo ASC
        """
        values = (citta, classe_energetica_minima, classe_energetica_massima)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        current_classe_energetica = None
        current_classe_energetica_alloggi = []

        for row in alloggi:
            classe_energetica = row[7]

            if classe_energetica != current_classe_energetica:
                # Nuova classe energetica, aggiungi gli alloggi della classe precedente al risultato
                result.extend(current_classe_energetica_alloggi)

                # Inizializza per la nuova classe energetica
                current_classe_energetica = classe_energetica
                current_classe_energetica_alloggi = []

            print("ID DAO ENERGIA:      " + str(row[0]))
            current_classe_energetica_alloggi.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        # Aggiungi gli alloggi dell'ultima classe energetica al risultato
        result.extend(current_classe_energetica_alloggi)

        return result


    def ricerca_classe_energetica_Aplusplus(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'A++'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_classe_energetica_Aplus(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'A+'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_classe_energetica_A(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'A'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_classe_energetica_B(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'B'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_classe_energetica_C(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'C'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result

    def ricerca_classe_energetica_D(self, citta):
        query = """
            SELECT a.*
            FROM alloggio a
            INNER JOIN indirizzo i ON a.id_alloggio = i.id_alloggio
            WHERE a.disponibilità = 1
            AND i.citta = %s
            AND a.classe_energetica = 'D'
            ORDER BY a.prezzo ASC
        """
        values = (citta,)
        self.__cursor.execute(query, values)
        alloggi = self.__cursor.fetchall()

        result = []
        for row in alloggi:
            print("ID DAO ENERGIA:      " + str(row[0]))
            result.append(Alloggio(
                id_alloggio=row[0],
                tipo_alloggio=row[1],
                disponibilita=row[2],
                titolo=row[3],
                mq=row[4],
                n_camere_letto=row[5],
                n_bagni=row[6],
                classe_energetica=row[7],
                arredamenti=row[8],
                data_publicazione=row[9],
                pannelli_solari=row[10],
                pannelli_fotovoltaici=row[11],
                descrizione=row[12],
                verifica=row[13],
                prezzo=row[14],
                n_ospiti=row[15],
                n_stanze=row[16],
                tasse=row[17],
                email_dip=row[18],
                email_loc=row[19],
                data_verifica=row[20]
            ))

        return result


    def ricerca_per_id(self, id_alloggio):
        query = """
            SELECT * FROM alloggio
            WHERE id_alloggio = %s
        """
        values = (id_alloggio,)

        self.__cursor.execute(query, values)
        result = self.__cursor.fetchone()

        if result:
            alloggio = Alloggio(
                id_alloggio=result[0],
                tipo_alloggio=result[1],
                disponibilita=result[2],
                titolo=result[3],
                mq=result[4],
                n_camere_letto=result[5],
                n_bagni=result[6],
                classe_energetica=result[7],
                arredamenti=result[8],
                data_publicazione=result[9],
                pannelli_solari=result[10],
                pannelli_fotovoltaici=result[11],
                descrizione=result[12],
                verifica=result[13],
                prezzo=result[14],
                n_ospiti=result[15],
                n_stanze=result[16],
                tasse=result[17],
                email_dip=result[18],
                email_loc=result[19],
                data_verifica=result[20]
            )
            return alloggio
        else:
            return None

    def conta(self):
        query = """
                    SELECT COUNT(*) FROM alloggio
                """
        self.__cursor.execute(query)
        results = self.__cursor.fetchone()[0]
        return results
