from flask import Blueprint, request, render_template, session, redirect, url_for, Flask
from .Post import Post
from .PostDAO import PostDAO

gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")


@gu2.route('/CreatePost.html', methods=['POST', 'GET'])
def creaPost():
    print("Ciao Caro")
    if request.method == 'POST':

        email = session["email"]
        titolo = request.form["titolo"]
        descrizione = request.form["descrizione"]

        post = Post(email=email, titolo=titolo, descrizione=descrizione)
        dao = PostDAO()

        dao.createPost(post)
        return render_template("output.html", descrizione=descrizione, email= email)
    elif request.method == "GET":
        return render_template("CreatePost.html")
