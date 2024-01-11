from WebSite.flask.gestioneUtente.Segnalazione import Segnalazione
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class SegnalazioneDAO:




    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()


    def createSegnalazione(self, email, emailS,motivo):
        stato = "aperto" #imposto lo stato ad aperto quando si crea la segnalazione
        query = """
                INSERT INTO Segnalazione ( email, emailS, stato, motivo)
                VAlUES (%s,%s,%s,%s)
                """
        values = (email, emailS, stato, motivo)
        print(values)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    def updateSegnalazione(self, email, emailS, stato, motivo):
        query = """
                UPDATE Segnalazione 
                SET email=%s,emailS=%s,stato=%s, motivo = %s
                WHERE email = %s AND emailS=%s
                """
        values = (email, emailS,stato, motivo)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    def deleteSegnalazione(self, email, emailS):
        query = """
                DELETE FROM Segnalazione
                WHERE email = %s, emailS=%s
                """
        values = (email, emailS)
        self.__cursor.execute(query, values)
        self.__connection.commit()


    def visualizzasegnalazione(self, emailS):
        query = """
                SELECT motivo, stato
                FROM Segnalazione
                WHERE emailS = %s
                """
        values = (emailS,)
        self.__cursor.execute(query, values)
        results = self.__cursor.fetchall()
        segnalazioni = []
        for result in results:
            segnalazione = Segnalazione(
                motivo=result[0],
                stato =result[1]
            )
            print(segnalazioni)
            segnalazioni.append(segnalazione)
        return segnalazioni



    def utenti_contre_segnalazioni(self):
        query = """
                SELECT  emailS
                FROM segnalazione
                """
        self.__cursor.execute(query)
        results = self.__cursor.fetchall()
        segnalazioni_per_utente = {}

        for result in results:
            emailS = result[0]
            #verifica se l'emaiS ha altre segnalazioni
            if emailS not in segnalazioni_per_utente:
                #se non ci sta mette il contatore a 1
                segnalazioni_per_utente[emailS] = 1
            else:
                #altrimenti lo aggiora di 1
                segnalazioni_per_utente[emailS] +=1
        #crea una lista di utenti con 3 più segnalazioni
        utenti_con_segnalazioni = [emailS for emailS, count in segnalazioni_per_utente.items() if count >= 3]
        return utenti_con_segnalazioni
