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


@gu.route('/admin', methods=['GET'])
def dipendenti_homechecker():
    dao = DipendenteDAO()
    dipendenti_homechecker = dao.ricercaTdipendente('Homechecker')
    if dipendenti_homechecker:
        return render_template('admin.html', dipendenti=dipendenti_homechecker)
    else:
        return 'Nessun dipendente con tipologia "Homechecker" trovato.'



@gu.route('/admin', methods=['GET', 'POST'])
def registra_homechecker():
    email = request.form['email']
    nome = request.form['nome']
    cognome = request.form['cognome']
    password = request.form['password']  # Assicurati di ottenere la password dal form HTML

    # Creazione dell'oggetto Dipendente con i valori forniti dal form
    nuovo_homechecker = Dipendente(
        email=email,
        nome=nome,
        cognome=cognome,
        tipo_dipendente='Homechecker',
        password=password
    )

    dao = DipendenteDAO()
    dao.registra_homechecker(nuovo_homechecker)
    dipendenti_homechecker = dao.ricercaTdipendente('Homechecker')

    return render_template('admin.html', dipendenti=dipendenti_homechecker)
