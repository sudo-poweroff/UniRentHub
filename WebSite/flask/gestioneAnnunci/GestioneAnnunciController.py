from flask import Blueprint, request, render_template, session, redirect, url_for, Flask

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