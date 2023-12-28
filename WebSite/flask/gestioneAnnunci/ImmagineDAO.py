from .Immagine import Immagine
from WebSite.flask.test.GestioneConnessione import GestioneConnessione


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


class ImmagineDAO:
    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def inserisci_immagine(self, immagine):
        query="""
             INSERT INTO immagine
            (id_immagine, id_alloggio, path) VALUES (%s,%s,%s)
        """
        empPicture = convertToBinaryData(immagine.get_path())
        print("VALUEEEEEE" + str(empPicture))
        values = (
            immagine.get_id_immagine(), immagine.get_id_alloggio(), empPicture
        )

        self.__cursor.execute(query, values)
        self.__connection.commit()

    def recupera_immagine(self, id_alloggio):
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
