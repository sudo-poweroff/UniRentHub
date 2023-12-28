from flask import Blueprint, request, render_template, session, redirect, url_for
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .GestioneUtenteService import get_cliente_by_email_password, registra_cliente, registra_homechecker_service, \
    show_homecheckerService, iscrizione_universita, accesso_admin, elimina_dipendente_service

gu = Blueprint('gu', __name__, template_folder="gestioneUtente")


@gu.route('/')
def main():
    #passiamo il tipo utente alla html per modificare l'header
    tipo_utente = session.get("tipo", "gest")
    return render_template("Homepage.html", tipo = tipo_utente)


@gu.route('/registrazione', methods=['GET', 'POST'])
def registrazione():
    if request.method == "GET":
        return render_template("registrazione.html")

    if request.method == "POST":
        nome = request.form["nome"]
        cognome = request.form["cognome"]
        email = request.form["email"]
        password = request.form["password"]
        denominazione = request.form.get("universita", "")
        tipo = request.form.get("locatore2", "Studente")
        numero_carta = request.form["numero_carta"]
        cvv = request.form["cvv"]
        scadenza = request.form["scadenza"]

        user = registra_cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo, numero_carta = numero_carta, scadenza = scadenza)
        if tipo == "Studente":
            iscrizione = iscrizione_universita(denominazione=denominazione, email=email)

        if user:
            session["nome"] = user.getNome()
            session["cognome"] = user.getCognome()
            session["email"] = user.getEmail()
            session["password"] = user.getPassword()
            session["tipo"] = user.getTipo()

            return redirect(url_for("gu.main"))


@gu.route('/login', methods=['GET', 'POST'])
def accessoU():
    session["messaggio"] = ""
    if request.method == "POST":

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

    return render_template("Homepage.html")


@gu.route("/logout")
def logout():
    if session.get("tipo") == "Studente" or session.get("tipo") == "Locatore":
        session.pop("nome", None)
        session.pop("cognome", None)
        session.pop("email", None)
        session.pop("password", None)
        session.pop("tipo", None)
        print("ciao sono CLIENTE")
        return redirect(url_for('gu.main'))
    elif session.get("tipo") == "Homechecker" or session.get("tipo") == "Admin":
        print("ciao sono DIPENDENTE")
        session.pop("nome", None)
        session.pop("cognome", None)
        session.pop("email", None)
        session.pop("password", None)
        session.pop("tipo", None)
        return render_template("AccessoAdmin.html")


@gu.route('/Homepage.html') #per il log-out, NON TOCCATE PATH
def show_output():
    return render_template('Homepage.html')


@gu.route('/AccessoAdmin', methods=['GET', 'POST'])
def reg():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        dipendente = accesso_admin(email=email, password=password)
        print("CIAO SONO FUORI")
        if dipendente:
            print("CIAO SONO ENTRATO")
            session.permanent = True  # la sessione è permanente
            nomedip = dipendente.getNome()
            maildip = dipendente.getEmail()
            pwddip = dipendente.getPassword()
            tipodip = dipendente.getTipo()
            session["nome"] = nomedip
            session["email"] = maildip
            session["password"] = pwddip
            session["tipo"] = tipodip
            return render_template("admin.html")
        else:
            session["messaggio"] = "Credenziali errate"
    return render_template("AccessoAdmin.html")


@gu.route('/admin', methods=['GET', 'POST'])
def registra_homechecker():

    dipendenti_homechecker = show_homecheckerService()

    if request.method == 'POST':
        if 'delete_email' in request.form:
            email_da_eliminare = request.form['delete_email']
            print("ciao")
            # Chiamata alla funzione per eliminare il dipendente dal DAO
            elimina_dipendente_service(email_da_eliminare)
            print("ciao2")
            # Se l'eliminazione ha avuto successo, aggiorna la lista dei dipendenti
            dipendenti_homechecker = show_homecheckerService()
            return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker)

        else:
            email = request.form['email']
            nome = request.form['nome']
            cognome = request.form['cognome']
            password = request.form['password']  # Assicurati di ottenere la password dal form HTML

            nuovo_homechecker = registra_homechecker_service(email, nome, cognome, password)
            if nuovo_homechecker:
                dipendenti_homechecker = show_homecheckerService()
                return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker, nuovo_homechecker=nuovo_homechecker)

    return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker)





