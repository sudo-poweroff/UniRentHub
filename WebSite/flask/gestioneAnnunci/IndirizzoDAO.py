from WebSite.flask.gestioneAnnunci.Indirizzo import Indirizzo
from WebSite.flask.test.GestioneConnessione import GestioneConnessione

class IndirizzoDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def ricerca_citta(self, citta):
        query = """
                SELECT id_alloggio FROM indirizzo
                WHERE citta = %s
                """
        values = (citta, )
        self.__cursor.execute(query, values)
        id_alloggi = self.__cursor.fetchall()  # Ottieni tutti i risultati della query
        for i in id_alloggi:
            print("ID:" + str(i[0]))
        return id_alloggi

    def crea_indirizzo(self, indirizzo):
        query = """
                INSERT INTO indirizzo (id_alloggio, via, cap, civico, citta, provincia)
                VALUES (%s, %s, %s, %s, %s, %s)
                """
        values = (indirizzo.get_id_alloggio(), indirizzo.get_via(), indirizzo.get_cap(), indirizzo.get_civico(), indirizzo.get_citta(), indirizzo.get_provincia())
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def visualizzaindirizzo(self, id_alloggio):
        query = "SELECT * FROM indirizzo WHERE id_alloggio = %s"
        values = (id_alloggio,)
        self.__cursor.execute(query, values)
        result = self.__cursor.fetchall()

        if result:
            # Assume che result contenga solo una riga
            indirizzo = Indirizzo(
                id_alloggio=id_alloggio,
                via=result[0][1],
                cap=result[0][2],
                civico=result[0][3],
                citta=result[0][4],
                provincia=result[0][5]
            )
            print(indirizzo.get_via())
            return indirizzo
