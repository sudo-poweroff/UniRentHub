import mysql.connector


class GestioneConnessione:

    def __init__(self):
        self.__connessione = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Giuseppe",
            database="unirenthub"
        )
        self.__cursor = self.__connessione.cursor()

    def getConnessione(self):
        return self.__connessione

    def getCursor(self):
        return self.__cursor

    def closeConnessione(self):
        self.__connessione.close()
