import re
from flask import Flask, flash
from .Cliente import Cliente
from .ClienteDAO import ClienteDAO
from .Dipendente import Dipendente
from .DipendenteDAO import DipendenteDAO
from .Iscrizione import Iscrizione
from .IscrizioneDAO import IscrizioneDAO


# Funzione di controllo per l'email caratteri
def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))

# Funzione di controllo per la password caratteri
def is_valid_password(password):
    # La password deve contenere almeno 8 caratteri, di cui almeno una lettera maiuscola, una lettera minuscola e un numero
    password_pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$')
    return bool(re.match(password_pattern, password))

#Controlla email esistente
def controlla_email_esistente(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email)
    if cliente:
        return False #se il cliente esiste torni false
    else:
        return True #se il cliente non esiste torni true


#Controlla campi
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


def registra_cliente(nome, cognome, email, password, tipo_utente, numero_carta, scadenza):
    if controlla_campi(nome, cognome, email):
        if is_valid_email(email):
            if is_valid_password(password):
                if controlla_email_esistente(email):
                    cliente = Cliente(nome=nome, cognome=cognome, email=email, password=password, tipo_utente=tipo_utente, numero_carta=numero_carta, data_scadenza=scadenza)
                    dao = ClienteDAO()
                    dao.createCliente(cliente)
                    return cliente
#creazione nuovo homechecker
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

#metodo stampa homechecker
def show_homecheckerService():
    dao = DipendenteDAO()
    dipendenti_homechecker = dao.ricercaTdipendente('Homechecker')
    return dipendenti_homechecker


#regitrazione iscrizione università
def iscrizione_universita(email, denominazione):
    iscrizione = Iscrizione(email=email, denominazione=denominazione)
    dao = IscrizioneDAO()
    dao.create_iscrizione(iscrizione)
    return iscrizione

