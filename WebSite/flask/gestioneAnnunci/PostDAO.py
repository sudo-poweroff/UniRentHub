from .Post import Post
from WebSite.flask.DBConnection.GestioneConnessione import GestioneConnessione


class PostDAO:

    def __init__(self):
        self.__gestioneConnessione = GestioneConnessione()
        self.__connection = self.__gestioneConnessione.getConnessione()
        self.__cursor = self.__gestioneConnessione.getCursor()

    def createPost(self, post):
        if (post is None or post.get_email() is None or post.get_email() == ""
                or post.get_titolo() is None or post.get_titolo() == ""
                or post.get_descrizione() is None or post.get_descrizione() == ""):
            raise ValueError("Il post e tutti i suoi campi devono essere definiti.")
        query = """
            INSERT INTO Post (titolo, descrizione, email)
            VALUES (%s, %s, %s)
        """
        values = (
            post.get_titolo(), post.get_descrizione(),
            post.get_email()
        )
        self.__cursor.execute(query, values)
        self.__connection.commit()

    def ricerca_post(self, parola_chiave):
        query = """
            SELECT *
            FROM post
            WHERE descrizione LIKE %s
        """
        values = ('%' + parola_chiave + '%',)

        self.__cursor.execute(query, values)
        risultati = self.__cursor.fetchall()

        posts = []

        for row in risultati:
            post = Post(
                titolo=row[1],
                descrizione=row[2],
                email=row[3]
            )
            posts.append(post)
        return posts

    def contapost(self):
        query = """
            SELECT COUNT(*) FROM post
        """
        self.__cursor.execute(query)
        results = self.__cursor.fetchone()[0]
        return results
