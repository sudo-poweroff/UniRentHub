from datetime import date
from flask import current_app as app
from flask_mail import Message, Mail
from flask import Blueprint, request, render_template, session, redirect, url_for
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .GestioneUtenteService import get_cliente_by_email_password, registra_cliente, registra_homechecker_service, \
    show_homecheckerService, iscrizione_universita, accesso_admin, elimina_dipendente_service, \
    cerca_uni, cercatutteuni, casep, update_cliente, idcasas, cercacasastudente, visualizzasegnalazione_service, \
    update_verificatoservice, check_account_verification, cerca_cliente_byEmail, blocca_utenteservice, \
    rimuovi_blocco_utenteservice, utenti_contre_segnalazioniservice, chiudi_tutte_le_segnalazioni, update_blocco, \
    validate_registrazione, validate_registrazione_dipendente
from WebSite.flask.gestioneAnnunci.GestioneAnnunciService import preleva_immagini
from itsdangerous import  URLSafeTimedSerializer
from functools import wraps
from datetime import datetime
import datetime

from flask import flash

serializer = URLSafeTimedSerializer('my_secret_token')
gu = Blueprint('gu', __name__, template_folder="gestioneUtente")






#decoratore (serve per prendere una funzione come argomento e resituire una nuova funzione, in pratica eseguo questa funzione in qualsiasi altra funzione semplicemente facnedo @verifica_account_required

def verifica_account_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'verificato' in session and session['verificato']:
            return f(*args, **kwargs)
        else:
            return redirect(
                url_for('gu.verifica'))  # Reindirizza alla pagina di verifica se l'account non è stato verificato
    return decorated_function



#decoratore per il controllo del bloccato
def controllo_blocco_utente(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        data_blocco = session.get('data_blocco')

        if data_blocco is not None and (datetime.now() - data_blocco).days < 30:
            return render_template('blockpage.html', messaggio="Utente già bloccato nelle ultime 30 giorni.")
        return f(*args, **kwargs)
    return decorated_function



@gu.route('/')
def main():
    # passiamo il tipo utente alla html per modificare l'header
    tipo_utente = session.get("tipo", "gest")
    return render_template("Homepage.html", tipo=tipo_utente)


@gu.route('/registrazione', methods=['GET', 'POST'])
def registrazione():
    if request.method == "GET":
        universita = cercatutteuni()
        return render_template("registrazione.html",universita=universita)

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

        print("OKAY SONO FUORI")
        #verifichiamo se esiste l'utente nel DB
        boolean = validate_registrazione(email=email)

        #se è uguale a false vuol dire che esiste già un utente nel db non quell'email
        if boolean is False:
            print("okay, ci sono nel boolean")
            flash("Email già registrata. Prova con un'altra.", 'error')
            return redirect(url_for("gu.registrazione"))

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
            session["carta"] = user.getNumeroCarta()
            session["mese"] = user.getMeseScadenza()
            session["anno"] = user.getAnnoScadenza()
            session["universita"] = denominazione
            session["verificato"] = 0

        if tipo in ["Studente", "Locatore"]:
            return redirect(url_for("gu.verifica"))
    return render_template("verifica.html")


@gu.route('/login', methods=['GET', 'POST'])
def accessoU():
    session["messaggio"] = ""
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = get_cliente_by_email_password(email, password)

        if user:  # Se l'autenticazione ha successo

            data_blocco = user.getDataBlocco()
            verifica = user.getVerificato()

            if data_blocco is not None:
                data_blocco = datetime.datetime.combine(data_blocco, datetime.datetime.min.time())
                data_attuale = datetime.datetime.now()
                differenza_tempo = data_attuale - data_blocco
                print("Differenza TEMPO: ", differenza_tempo)
                if differenza_tempo.days >= 30:
                    update_blocco(email)
                else:
                    return render_template("blockpage.html")

            if not verifica:
                return render_template("verifica.html")

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
            verificato = user.getVerificato()

            session["nome"] = nomecliente
            session["cognome"] = cognomecliente
            session["email"] = mailcliente
            session["password"] = pwdcliente
            session["tipo"] = tipocliente
            session["carta"] = numcarta
            session["mese"] = mese
            session["anno"] = anno
            session["verificato"] = verificato

            return redirect(url_for("gu.main"))
        else:  # Se l'autenticazione fallisce
            session["messaggio"] = "Credenziali errate"

    return render_template("Homepage.html")


@gu.route("/logout")
def logout():
    if session.get("tipo") == "Studente" or session.get("tipo") == "Locatore":
        if session.get("verifica") == 0:
            session.pop("nome", None)
            session.pop("cognome", None)
            session.pop("email", None)
            session.pop("password", None)
            session.pop("tipo", None)
            session.pop("verificato", None)
            return render_template("verifica.html")
        session.pop("nome", None)
        session.pop("cognome", None)
        session.pop("email", None)
        session.pop("password", None)
        session.pop("tipo", None)
        session.pop("verificato", None)
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
    utenti_con_segnalazioni = utenti_contre_segnalazioniservice()
    if request.method == 'POST':
        if 'delete_email' in request.form:
            email_da_eliminare = request.form['delete_email']
            # Chiamata alla funzione per eliminare il dipendente dal DAO
            elimina_dipendente_service(email_da_eliminare)
            # Se l'eliminazione ha avuto successo, aggiorna la lista dei dipendenti
            dipendenti_homechecker = show_homecheckerService()
            return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker)

        else:
            email = request.form.get('email')
            nome = request.form.get('nome')
            cognome = request.form.get('cognome')
            password = request.form.get('password')

            if email and nome and cognome and password:
                # Verifica che tutti i campi siano presenti
                # verifichiamo se esiste l'utente nel DB
                boolean = validate_registrazione_dipendente(email=email, password=password)

                # se è uguale a false vuol dire che esiste già un utente nel db non quell'email
                if boolean is False:
                    flash("Email già registrata. Prova con un'altra.", 'error')
                    return redirect(url_for("gu.registra_homechecker"))

                nuovo_homechecker = registra_homechecker_service(email, nome, cognome, password)
                if nuovo_homechecker:
                    dipendenti_homechecker = show_homecheckerService()
                    return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker,
                                           nuovo_homechecker=nuovo_homechecker)

    return render_template('admin.html', dipendenti_homechecker=dipendenti_homechecker, utenti_con_segnalazioni=utenti_con_segnalazioni)


@gu.route('/Userpage', methods=['GET', 'POST'])
def userpage():
    if session.get("tipo") == "Locatore" or session.get("tipo") == "Studente":
        if(request.args.get('message')):
            message = request.args.get('message')
        else:
            message=""
        universita = cercatutteuni()
        alloggi = []  # Inizializzazione della lista per memorizzare le case
        immagini=[] #inizializzazione della lista per memorizzare le immagini
        if session.get("tipo") == "Locatore":
            alloggi = casep(session["email"])
            id_alloggi = []
            #non toccare questa sequenza di for e if, è una logica implementativa per ritornarci la prima immagine del DB di un Locatore
            for row in alloggi:
                id_alloggio = row.get_id_alloggio()
                id_alloggi.append(id_alloggio)
            for id_ in id_alloggi:
                print("id:     " + str(id_))
                count = 0
                path = preleva_immagini(id_)
                for p in path:
                    if count == 0:
                        print("path:     " + p)
                        immagini.append(p)
                        count = 1
        else:
            data_oggi = date.today().isoformat()
            id_casa = idcasas(session["email"], data_oggi)
            if id_casa != None:
                print("ID_CASA: " + str(id_casa))
                email = session["email"]
                alloggi = cercacasastudente(email=email)

                id_alloggi = []
                immagini = []
                for row in alloggi:
                    id_alloggio = row.get_id_alloggio()
                    id_alloggi.append(id_alloggio)
                for id_ in id_alloggi:
                    print("id:     " + str(id_))
                    count = 0
                    path = preleva_immagini(id_)
                    for p in path:
                        if count == 0:
                            print("path:     " + p)
                            immagini.append(p)
                            count = 1
                return render_template("Userpage.html",alloggi=alloggi, universita= universita, immagini=immagini,message=message) #se l'utente ha case in affitto
            return render_template("Userpage.html", universita=universita) #se l'utente non ha case in affitto
        return render_template('Userpage.html', universita=universita, alloggi=alloggi, immagini = immagini) #se l'utente LOCATORE ha postato case
    return render_template("error.html")


@gu.route('/modifica', methods=['GET', 'POST'])
def modifica():
    if request.method == "GET":
        return "FRATMMMMMMMMMMMMMMMM"
    if request.method == "POST":
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        email = request.form.get("email")
        password = request.form.get("password")
        tipo = session["tipo"]
        denominazione = request.form.get("universita")
        numero_carta = request.form.get("numeroc")
        mese = request.form.get("mese-scadenza")
        anno = request.form.get("anno-scadenza")
        cvv = request.form.get("cvv")

        update_cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo,
                       numero_carta=numero_carta, mese=mese, anno=anno)

        if tipo == "Studente":
            if session["universita"] != denominazione:
                iscrizione = iscrizione_universita(denominazione=denominazione, email=email)

        session["nome"] = nome
        session["cognome"] = cognome
        session["email"] = email
        session["password"] = password
        session["carta"] = numero_carta
        session["cvv"] = cvv
        session["universita"] = denominazione
    return redirect(url_for('gu.userpage'))


@gu.route("/servizi")
def servizi():
    return render_template("Servizi.html")

@gu.route("/community")
def community():
    return render_template("Community.html")


#codice per la gestione della virifica account con creazione/gestione di token univoco
#questa funzione genera il token
def generate_confirmation_token(email):
    return serializer.dumps(email)




#gestione del token con decodificazione
def confirm_token(token, expiration=600):
    try:
        email = serializer.loads(token, max_age=expiration)
    except:
        return False
    return email


# Configurazione della posta
def configure_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = 'm.greco65@studenti.unisa.it'
    app.config['MAIL_PASSWORD'] = 'Marcogreco123$!'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'm.greco65@studenti.unisa.it'

    mail = Mail(app)
    return mail



# Funzione per inviare l'email di conferma
def send_verification_email(mail, email, confirmation_url):
    msg = Message("Verifica dell'account", sender=mail.default_sender, recipients=[email])
    msg.body = f"Ciao, sei stato verificato! Link alla tua pagina utente: {confirmation_url}"
    mail.send(msg)


#funzione invio email
@gu.route("/verifica")
def verifica():
    if request.method == "POST":
        pass
    else:
        if 'email' in session:
            email = session['email']
            token = generate_confirmation_token(email)

            confirmation_url = url_for('gu.conferma_account', token=token, _external=True)

            # Invia l'email di conferma
            mail = configure_mail(app)
            send_verification_email(mail, email, confirmation_url)  # Passa l'istanza mail configurata
            logout()
            return render_template("verifica.html")

        # Se l'email non è presente nella sessione, reindirizza l'utente alla pagina di login
        return redirect(url_for('gu.main'))


#conferma account basata sul token
@gu.route('/conferma/<token>', methods=['GET'])
def conferma_account(token):
    email = confirm_token(token)
    if email:
        update_verificatoservice(email)
        session['verificato'] = True
        return redirect(url_for('gu.userpage'))
    else:
        return render_template('link_scaduto.html')

@gu.route('/segnalazioni/<emailS>')
def visualizzasegnalazione(emailS):
    segnalazioni = visualizzasegnalazione_service(emailS)
    return render_template('segnalazioni.html', segnalazioni = segnalazioni)


@gu.route('/block_user', methods=["POST", "GET"])
def blocca_utente():
    if request.method == "GET":
        email = session.get("emailS")
        print("BLOCCO:  " + email)
        chiudi_tutte_le_segnalazioni(email)
        blocca_utenteservice(email)
        return redirect(url_for("gu.segnalazioni_card"))


@gu.route('/segnalazioni', methods=["GET"])
def segnalazioni():
    if request.method == "GET":
        email = request.args.get('email')
        session["emailS"] = email
        print("EMAIL:    "  + email)
        segnalazioni = visualizzasegnalazione_service(email)
        return render_template("segnalazioni_admin.html", segnalazioni=segnalazioni)


@gu.route('/segnalazioni_card', methods=["GET"])
def segnalazioni_card():
    if request.method == "GET":
        segnalazioni = []
        emailS = utenti_contre_segnalazioniservice()
        return render_template("segnalazioni_card.html", emailS = emailS)
