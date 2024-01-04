import re
from flask import Flask, flash
from .Cliente import Cliente
from .ClienteDAO import ClienteDAO
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .Iscrizione import Iscrizione
from .IscrizioneDAO import IscrizioneDAO
from .UniversitaDAO import UniversitaDAO
from WebSite.flask.gestioneAnnunci.AlloggioDAO import AlloggioDAO
from WebSite.flask.gestioneAffitto.AffittareDAO import AffittareDAO
from WebSite.flask.gestioneUtente.SegnalazioneDAO import SegnalazioneDAO


# Funzione di controllo per l'email caratteri
def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))


# Funzione di controllo per la password caratteri
def is_valid_password(password):
    # La password deve contenere almeno 8 caratteri, di cui almeno una lettera maiuscola, una lettera minuscola e un numero
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    return bool(re.match(password_pattern, password))


# Controlla email esistente
def controlla_email_esistente(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email)
    if cliente:
        return False  # se il cliente esiste torni false
    else:
        return True  # se il cliente non esiste torni true


def cercatutteuni():
    dao = UniversitaDAO()
    results = dao.cercatutti()
    universita = [item[0] for item in results]
    return universita


# Controlla campi
def controlla_campi(nome, cognome, email):
    if not isinstance(nome, str) or not 0 < len(nome) <= 45:
        flash("Nome non valido", category="error")
    elif not isinstance(cognome, str) or not 0 < len(cognome) <= 45:
        flash("Cognome non valido", category="error")
    elif not isinstance(email, str) or not 0 < len(email) <= 45:
        flash("Email non valida", category="error")
    else:
        return True
    return False


def registra_cliente(nome, cognome, email, password, tipo_utente, numero_carta, mese_scadenza, anno_scadenza):
    if controlla_campi(nome, cognome, email):
        if is_valid_email(email):
            if is_valid_password(password):
                if controlla_email_esistente(email):
                    cliente = Cliente(nome=nome, cognome=cognome, email=email, password=password,
                                      tipo_utente=tipo_utente, numero_carta=numero_carta, mese_scadenza=mese_scadenza, anno_scadenza=anno_scadenza)
                    dao = ClienteDAO()
                    dao.createCliente(cliente)
                    return cliente


# creazione nuovo homechecker
def registra_homechecker_service(email, nome, cognome, password):
    if is_valid_email(email):

        if is_valid_password(password):
            dipendente = Dipendente(nome=nome, cognome=cognome, email=email, password=password)
            dao = DipendenteDAO()
            dao.registra_homechecker(dipendente)
            return dipendente


def get_cliente_by_email_password(email, password):
    dao = ClienteDAO()
    cliente = dao.accesso(email=email, pwd=password)
    return cliente


# metodo stampa homechecker
def show_homecheckerService():
    dao = DipendenteDAO()
    dipendenti_homechecker = dao.ricercaTdipendente('Homechecker')
    return dipendenti_homechecker


# regitrazione iscrizione università
def iscrizione_universita(email, denominazione):
    iscrizione = Iscrizione(email=email, denominazione=denominazione)
    dao = IscrizioneDAO()
    dao.create_iscrizione(iscrizione)
    return iscrizione


# accesso admin
def accesso_admin(email, password):
    if is_valid_email(email):
        dao = DipendenteDAO()
        dipendente = dao.ricercaDip(email, password)
        return dipendente


def elimina_dipendente_service(email):
    dao = DipendenteDAO()
    dipendente = dao.elimina_homechecker(email)
    print("eliminato")
    return dipendente


def cerca_uni(email):
    dao = ClienteDAO()
    uni = dao.universitabystudente(email)
    return uni[0]


def casep(email):
    dao = ClienteDAO()
    alloggi = dao.cercacaseproprietario(email)
    return alloggi


def update_cliente(nome, cognome, email, password, tipo_utente, numero_carta, anno, mese):
    if controlla_campi(nome, cognome, email):
        if is_valid_email(email):
            if is_valid_password(password):
                dao = ClienteDAO()
                print(mese)
                cliente = dao.aggiornaCliente(nome, cognome, email, password, tipo_utente, numero_carta, anno, mese)


def idcasas(email, data):
    dao = ClienteDAO()
    id_casa = dao.cercacasastudente(email, data)
    print(id_casa)
    return id_casa


def cercacasastudente(email):
    dao = AlloggioDAO()
    dao2 = AffittareDAO()
    affitti = dao2.ricercaaffitto_per_email(email=email)

    alloggi = []
    for aff in affitti:
        id = aff.get_id_alloggio()
        alloggio = dao.visualizzaannuncio(id)
        alloggi.append(alloggio)
        print("titolo: " + alloggio.get_titolo())

    return alloggi


#sestituisce cliente byemail
def cerca_cliente_byEmail(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email=email)
    return cliente


def visualizzasegnalazione_service(emailS):
    dao = SegnalazioneDAO()
    segnalazioni = dao.visualizzasegnalazione(emailS)
    return segnalazioni

