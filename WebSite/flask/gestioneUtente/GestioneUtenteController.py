from flask import Blueprint, request, render_template, session, redirect, url_for
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .GestioneUtenteService import get_cliente_by_email_password, registra_cliente, registra_homechecker_service, \
    show_homecheckerService

gu = Blueprint('gu', __name__, template_folder="gestioneUtente")


@gu.route('/')
def main():
    #passiamo il tipo utente alla html per modificare l'header
    tipo_utente = session.get("tipo", "gest")
    return render_template("Homepage.html", tipo = tipo_utente)


@gu.route('/LoginCliente.html', methods=['GET', 'POST'])
def accessoU():
    session["messaggio"] = ""
    if request.method == "POST":

        button = request.form["selectButton"]

        if button == "Accedi":

            email = request.form["email"]
            password = request.form["password"]

            user = get_cliente_by_email_password(email, password)

            if user:  # Se l'autenticazione ha successo
                session.permanent = True
                nomecliente = user.getNome()
                cognomecliente = user.getCognome()
                mailcliente = user.getEmail()
                pwdcliente = user.getPassword()
                tipocliente = user.getTipo()
                session["nome"] = nomecliente
                session["cognome"] = cognomecliente
                session["email"] = mailcliente
                session["password"] = pwdcliente
                session["tipo"] = tipocliente

                return redirect(url_for("gu.main"))
            else:  # Se l'autenticazione fallisce
                session["messaggio"] = "Credenziali errate"

        elif button == "Registrazione":

            nome = request.form["nome2"]
            cognome = request.form["cognome2"]
            email = request.form["email2"]
            password = request.form["password2"]
            tipo = request.form.get("locatore2", "Studente")

            user = registra_cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo)

            if user:
                session["nome"] = user.getNome()
                session["cognome"] = user.getCognome()
                session["email"] = user.getEmail()
                session["password"] = user.getPassword()
                session["tipo"] = user.getTipo()

                return redirect(url_for("gu.main"))
            else:  # Se l'autenticazione fallisce
                session["messaggio"] = "Credenziali errate"

    return render_template("LoginCliente.html")


@gu.route("/logout")
def logout():
    session.pop("nome", None)
    session.pop("cognome", None)
    session.pop("email", None)
    session.pop("password", None)
    session.pop("tipo", None)
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

        dipendente = dao.ricercaDip(email, password)
        if dipendente:
            session.permanent = True  # la sessione è permanente
            nomedip = dipendente.getNome()
            maildip = dipendente.getEmail()
            pwddip = dipendente.getPassword()
            tipodip = dipendente.getTipo()
            session["nome"] = nomedip
            session["email"] = maildip
            session["password"] = pwddip
            session["tipo"] = tipodip
            return redirect(url_for('gu.show_output'))
        else:
            session["messaggio"] = "Credenziali errate"
    return render_template("AccessoAdmin.html")


#registrazione e stampa homechecker
@gu.route('/admin', methods=['GET', 'POST'])
def registra_homechecker():

    dipendenti_homechecker = show_homecheckerService()

    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        cognome = request.form['cognome']
        password = request.form['password']  # Assicurati di ottenere la password dal form HTML

        # Creazione dell'oggetto Dipendente con i valori forniti dal form
        nuovo_homechecker = registra_homechecker_service(email, nome, cognome, password)
        if nuovo_homechecker:
            #se avviene la registrazione aggiorna la lista
            dipendenti_homechecker = show_homecheckerService()
            return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker,nuovo_homechecker=nuovo_homechecker)


    return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker)





