from flask import Blueprint, request, render_template
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO

gu = Blueprint('gu', __name__, template_folder="gestioneUtente")


@gu.route('/')
def main():
    return "<h1>Sono Scarso</h1>"

@gu.route('/home')
def home():
    return render_template("Homepage.html")

@gu.route('/registrazione', methods=['GET', 'POST'])
def reg():
    if request.method == "POST":

        email = request.form["email"]

        dipendente = Dipendente()
        dao = DipendenteDAO()

        dipendente = dao.ricercaEmailD(email)

        return  render_template("output.html", dipendente=dipendente.getNome())
    else:
        return render_template("registrazione.html")

