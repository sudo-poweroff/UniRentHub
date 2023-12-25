from flask import Blueprint, request, render_template, session, redirect, url_for, Flask
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .Cliente import Cliente
from .ClienteDAO import ClienteDAO

gu = Blueprint('gu', __name__, template_folder="gestioneUtente")


@gu.route('/')
def main():
    #passiamo il tipo utente alla html per modificare l'header
    tipo_utente = session.get("tipodip", "gest")
    return render_template("Homepage.html", tipo = tipo_utente)


@gu.route('/LoginCliente.html', methods=['GET', 'POST'])
def accessoU():
    session["messaggio"] = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        cliente = Cliente()
        dao = ClienteDAO()
        cliente = dao.accesso(email, password)

        if cliente:  # Se l'autenticazione ha successo
            session.permanent = True
            nomecliente = cliente.getNome()
            cognomecliente = cliente.getCognome()
            mailcliente = cliente.getEmail()
            pwdcliente = cliente.getPassword()
            tipocliente = cliente.getTipo()
            session["nomecliente"] = nomecliente
            session["cognomecliente"] = cognomecliente
            session["maildip"] = mailcliente
            session["pwddip"] = pwdcliente
            session["tipodip"] = tipocliente

            return redirect(url_for("gu.main"))
        else:  # Se l'autenticazione fallisce
            session["messaggio"] = "Credenziali errate"
    return render_template("LoginCliente.html")


@gu.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for('gu.main'))


@gu.route('/Homepage.html') #per il log-out, NON TOCCATE PATH
def show_output():
    return render_template('Homepage.html')


@gu.route('/AccessoAdmin', methods=['GET', 'POST'])
def reg():
    session["messaggio"] = ""
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        dipendente = Dipendente()
        dao = DipendenteDAO()

        dipendente = dao.ricercaDip(email,password)
        if dipendente:
            session.permanent = True  # la sessione è permanente
            nomedip = dipendente.getNome()
            maildip = dipendente.getEmail()
            pwddip = dipendente.getPassword()
            tipodip = dipendente.getTipo()
            session["nomedip"] = nomedip
            session["maildip"] = maildip
            session["pwddip"] = pwddip
            session["tipodip"] = tipodip
            return redirect(url_for('gu.show_output'))
        else:
            session["messaggio"] = "Credenziali errate"
    return render_template("AccessoAdmin.html")


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
