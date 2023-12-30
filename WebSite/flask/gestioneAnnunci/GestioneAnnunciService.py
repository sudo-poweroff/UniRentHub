import os
import re
from flask import Flask, flash

from .Alloggio import Alloggio
from .AlloggioDAO import AlloggioDAO
from .ImmagineDAO import ImmagineDAO
from .IndirizzoDAO import IndirizzoDAO
from .PossidimentoDAO import PossedimentoDAO
from .Post import Post
from .PostDAO import PostDAO
from WebSite.flask.gestioneUtente.ClienteDAO import ClienteDAO
from .ServiziDAO import ServiziDAO


# Funzione di controllo per l'email caratteri
def is_valid_email(email):
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))


# Controlla email esistente
def controlla_email_esistente(email):
    dao = ClienteDAO()
    cliente = dao.ricercaEmailC(email)
    if cliente:
        return True  # se il cliente esiste torni True
    else:
        return False  # se il cliente non esiste torni False


def pubblicazione_post(email, titolo, descrizione):
    if is_valid_email(email):
        if controlla_email_esistente(email):
            post = Post(email=email, titolo=titolo, descrizione=descrizione)
            dao = PostDAO()

            dao.createPost(post)
            return post


def verifica_campi(titolo, indirizzo, descrizione, num_bagni, num_camere, num_ospiti, metri_quadri, prezzo,
                   periodo_minimo):
    if 30 > len(titolo) > 5:
        if 30 > len(indirizzo) > 5:
            if len(descrizione) > 30:
                if num_bagni > 0:
                    if num_camere > 0:
                        if num_ospiti > 0:
                            if metri_quadri > 0:
                                if prezzo > 0:
                                    return True
    else:
        return False


def pubblicazione_alloggio(tipo_alloggio, titolo, mq, n_camere_letto, n_bagni,
                           classe_energetica, arredamenti, data_pubblicazione,
                           pannelli_solari, pannelli_fotovoltaici, descrizione,
                           prezzo, n_ospiti, n_stanze, tasse, email_loc):
    alloggio = Alloggio(
        tipo_alloggio=tipo_alloggio,
        titolo=titolo,
        mq=mq,
        n_camere_letto=n_camere_letto,
        n_bagni=n_bagni,
        classe_energetica=classe_energetica,
        arredamenti=arredamenti,
        data_publicazione=data_pubblicazione,
        pannelli_solari=pannelli_solari,
        pannelli_fotovoltaici=pannelli_fotovoltaici,
        descrizione=descrizione,
        prezzo=prezzo,
        n_ospiti=n_ospiti,
        n_stanze=n_stanze,
        tasse=tasse,
        email_loc=email_loc,
    )
    dao = AlloggioDAO()
    dao.create_alloggio(alloggio=alloggio)
    return alloggio

def ricerca_alloggio(citta):
    dao1 = IndirizzoDAO()
    dao2 = AlloggioDAO()

    # Ottieni una lista di ID alloggi per la città specificata
    id_alloggi = dao1.ricerca_citta(citta=citta)
    for i in id_alloggi:
        print("ID SERVICE:" + str(i[0]))

    # Inizializza una lista vuota per gli alloggi
    alloggi = []
    print("Sono FUORI")
    # Itera su ogni ID alloggio e cerca l'alloggio associato
    for i in id_alloggi:
        id_alloggio = i[0] #inserisco i[0] in id_alloggio, in modo tale da scorrere sempre il prossimo id
        alloggio = dao2.visualizzaannuncio(id_alloggio)
        print("nome ALLOGGIO: " + alloggio.get_titolo())
        # Aggiungi l'alloggio alla lista
        alloggi.append(alloggio)

    return alloggi

def ricerca_post_studente(value):
    dao = PostDAO()
    posts = dao.ricerca_post(value)
    return posts

def creazione_post(titolo, descrizione, email):
    dao = PostDAO()
    post = Post(titolo=titolo, descrizione=descrizione, email=email)
    dao.createPost(post=post)

def inserisci_immagini(lista_immagini):
    dao1 = AlloggioDAO()
    dao2 = ImmagineDAO()
    id_cartella = dao1.cercaidcasa() + 1   #incremento per prendere l'id dell'alloggio che sta per essere creato
    path_cartella = f"static/alloggi/{id_cartella}" #istanzio il path della cartella dell'alloggio in una variabile

    if not os.path.isdir(path_cartella): #controllo esistenza path
        os.mkdir(path_cartella) #creo la cartella con la variabile path

    nomi_immagini = []  # Lista per memorizzare i nomi dei file delle immagini caricate
    count = 0

    for immagine in lista_immagini:
        if count < 3:
            path_immagine = os.path.join(path_cartella, immagine.filename)
            immagine.save(path_immagine) #salva l'immagine
            dao2.inserisci_immagine(immagine.get_id_immagine(), id_cartella, path_immagine)
            nomi_immagini.append(immagine.filename)  # Ottieni il nome del file e aggiungilo alla lista
            count += 1
        else:
            break

#non toccare fondamentale Alloggio
def max_id_casa():
    dao = AlloggioDAO()
    val = dao.cercaidcasa()
    return val

#non toccare fondamentale Alloggio
def indirizzo_crea(indirizzo):
    dao = IndirizzoDAO()
    dao.crea_indirizzo(indirizzo)

#non toccare per Alloggio
def crea_possedimento(possedimento):
    dao = PossedimentoDAO()
    dao.inserisci_possedimento(possedimento)

#non toccare Alloggio
def visualizza_servizi():
    dao = ServiziDAO()
    servizi = dao.visualizzaservizidisponibili()
    return servizi

#non toccare Alloggio
def visualizza_annuncio(id_alloggio):
    dao = AlloggioDAO()
    alloggio = dao.visualizzaannuncio(id_alloggio)
    return alloggio

#non toccare
def visualizza_indirizzo(id_alloggio):
    dao = IndirizzoDAO()
    indirizzo = dao.visualizzaindirizzo(id_alloggio=id_alloggio)
    return indirizzo

#non toccare Alloggio
def visualizza_servizi_alloggio(id_servizio):
    dao = ServiziDAO()
    servizio = dao.visualizza_servizio_by_id(id_servizio=id_servizio)
    return servizio

def visualizza_servizi_possedimento_byid(id_alloggio):
    dao = PossedimentoDAO()
    id_possedimento = dao.ricerca_by_id_alloggio(id_alloggio=id_alloggio)
    return id_possedimento