from flask import Blueprint, request, render_template, session, redirect, url_for, Flask

from .AnnuncioDAO import AnnuncioDAO
from .GestioneAnnunciService import pubblicazione_post


gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")


@gu2.route('/CreatePost', methods=['POST', 'GET'])
def creaPost():
    if request.method == 'POST':
        email = session["email"]
        titolo = request.form["titolo"]
        descrizione = request.form["descrizione"]

        post = pubblicazione_post(email = email, titolo = titolo, descrizione = descrizione)
        if post:
            return render_template("output.html", descrizione=descrizione, email= email)
    elif request.method == "GET":
        return render_template("CreatePost.html")
    return render_template("LoginCliente.html", message="Metodo di richiesta non valido")

@gu2.route('/Catalogo.html')
def catalogo():
    dao = AnnuncioDAO()
    alloggi = dao.visualizza()
    immagini = []
    for alloggio in alloggi:
        id_alloggio = alloggio[0]
        immagine = dao.visualizzaimg(id_alloggio)
        immagini.append(immagine)
    return render_template("catalogo.html", immagini=immagini,alloggi=alloggi)


@gu2.route('/Annuncio.html')
def annuncio():
    dao = AnnuncioDAO()
    id_alloggio = request.args.get('id')
    alloggio = dao.visualizzaannuncio(id_alloggio)
    servizi = dao.visualizzaservizi(id_alloggio)
    immagini = dao.visualizzaimmagini(id_alloggio)

    return render_template("Annuncio.html", alloggio=alloggio, servizi=servizi, immagini=immagini)