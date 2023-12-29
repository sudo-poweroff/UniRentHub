from datetime import date

from flask import Blueprint, request, render_template, session, redirect, url_for
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .GestioneUtenteService import get_cliente_by_email_password, registra_cliente, registra_homechecker_service, \
    show_homecheckerService, iscrizione_universita, accesso_admin, elimina_dipendente_service, \
    cerca_uni, cercatutteuni, casep, update_cliente, idcasas, cercacasastudente

gu = Blueprint('gu', __name__, template_folder="gestioneUtente")


@gu.route('/')
def main():
    # passiamo il tipo utente alla html per modificare l'header
    tipo_utente = session.get("tipo", "gest")
    return render_template("Homepage.html", tipo=tipo_utente)


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
        mese = request.form["mese-scadenza"]
        anno = request.form["anno-scadenza"]

        user = registra_cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo,
                                numero_carta=numero_carta, mese_scadenza=mese, anno_scadenza=anno)
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

            if user.getTipo() == "Studente":
                uni = cerca_uni(email)
                session["universita"] = uni

            nomecliente = user.getNome()
            cognomecliente = user.getCognome()
            mailcliente = user.getEmail()
            pwdcliente = user.getPassword()
            tipocliente = user.getTipo()
            numcarta = user.getNumeroCarta()
            mese = user.getMeseScadenza()
            anno = user.getAnnoScadenza()
            cvv = user.getVerificato()

            session["nome"] = nomecliente
            session["cognome"] = cognomecliente
            session["email"] = mailcliente
            session["password"] = pwdcliente
            session["tipo"] = tipocliente
            session["carta"] = numcarta
            session["mese"] = mese
            session["anno"] = anno
            session["cvv"] = cvv

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


@gu.route('/Homepage.html')  # per il log-out, NON TOCCATE PATH
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
            if dipendente.getTipo() == "Admin":
                return redirect(url_for('gu.registra_homechecker'))
            elif dipendente.getTipo() == "Homechecker":
                return redirect(url_for('gu2.homechecker'))
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
                return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker,
                                       nuovo_homechecker=nuovo_homechecker)

    return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker)


@gu.route('/Userpage', methods=['GET', 'POST'])
def userpage():
    universita = cercatutteuni()
    alloggi = []  # Inizializzazione della lista per memorizzare le case

    if session["tipo"] == "Locatore":
        alloggi = casep(session["email"])
    else:
        data_oggi = date.today().isoformat()
        id_casa = idcasas(session["email"], data_oggi)
        print(str(id_casa)+"Controller")
        alloggio = cercacasastudente(id_casa)
        print(alloggio.get_titolo()+"Controller")
        alloggi.append(alloggio)
        return render_template("Userpage.html",alloggi=alloggi, universita= universita)
    return render_template('Userpage.html', universita=universita, alloggi=alloggi)


@gu.route('/modifica', methods=['GET', 'POST'])
def modifica():
    if request.method == "POST":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        email = request.form.get("email")
        password = request.form.get("password")
        tipo = session["tipo"]
        denominazione = request.form.get("universita")
        numero_carta = request.form.get("numeroc")
        cvv = request.form.get("cvv")
        scadenza = request.form.get("scadenza")
        update_cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo,
                       numero_carta=numero_carta, scadenza=scadenza)

        if tipo == "Studente":
            if session["universita"] != denominazione:
                iscrizione = iscrizione_universita(denominazione=denominazione, email=email)

        session["nome"] = nome
        session["cognome"] = cognome
        session["email"] = email
        session["password"] = password
        session["carta"] = numero_carta
        session["scadenza"] = scadenza
        session["cvv"] = cvv
        session["universita"] = denominazione
    return redirect(url_for('gu.userpage'))


@gu.route("/servizi")
def servizi():
    return render_template("Servizi.html")

@gu.route("/community")
def community():
    return render_template("Community.html")
