import re
from flask import Flask, flash
from .Post import Post
from .PostDAO import PostDAO
from WebSite.flask.gestioneUtente.ClienteDAO import ClienteDAO


# Funzione di controllo per l'email caratteri
def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))


#Controlla email esistente
def controlla_email_esistente(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email)
    if cliente:
        return True #se il cliente esiste torni True
    else:
        return False #se il cliente non esiste torni False


def pubblicazione_post(email, titolo, descrizione):
    if is_valid_email(email):
        if controlla_email_esistente(email):
            post = Post(email=email, titolo=titolo, descrizione=descrizione)
            dao = PostDAO()

            dao.createPost(post)
            return post
