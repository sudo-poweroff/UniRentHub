from .Immagine import Immagine
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


class ImmagineDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def inserisci_immagine(self,id_alloggio, path):
        directory_salvataggio = 'static/img'
        query= """
             INSERT INTO immagine
            ( id_alloggio, path) 
            VALUES (%s,%s)
               """

        values = (id_alloggio, path)

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def recupera_path(self, id_alloggio):
        query="""
            SELECT * from immagine WHERE id_alloggio = %s
        """
        self.__cursor.execute(query, (id_alloggio,))
        results = self.__cursor.fetchall()

        immagine = []
        for row in results:
            imm = Immagine(
                id_immagine=row[0],
                id_alloggio=row[1],
                path=row[2]
            )
            immagine.append(imm)
        return immagine

