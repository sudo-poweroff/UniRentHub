from flask import Blueprint, request, render_template, session, redirect, url_for, Flask
from datetime import datetime

from numpy import double

from .AlloggioDAO import AlloggioDAO
from .GestioneAnnunciService import pubblicazione_post, pubblicazione_alloggio, ricerca_alloggio

gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")


@gu2.route('/CreatePost', methods=['POST', 'GET'])
def creaPost():
    if request.method == 'POST':
        email = session["email"]
        titolo = request.form["titolo"]
        descrizione = request.form["descrizione"]

        post = pubblicazione_post(email=email, titolo=titolo, descrizione=descrizione)
        if post:
            return render_template("output.html", descrizione=descrizione, email=email)
    elif request.method == "GET":
        return render_template("CreatePost.html")
    return render_template("LoginCliente.html", message="Metodo di richiesta non valido")


@gu2.route('/Catalogo.html')
def catalogo():
    dao = AlloggioDAO()
    alloggi = dao.visualizza()
    immagini = []
    for alloggio in alloggi:
        id_alloggio = alloggio[0]
        immagine = dao.visualizzaimg(id_alloggio)
        immagini.append(immagine)
    return render_template("catalogo.html", immagini=immagini, alloggi=alloggi)


@gu2.route('/Annuncio.html')
def annuncio():
    dao = AlloggioDAO()
    id_alloggio = request.args.get('id')
    alloggio = dao.visualizzaannuncio(id_alloggio)
    servizi = dao.visualizzaservizi(id_alloggio)
    immagini = dao.visualizzaimmagini(id_alloggio)

    return render_template("Annuncio.html", alloggio=alloggio, servizi=servizi, immagini=immagini)


@gu2.route('/CaricaAnnuncio.html')
def allservizi():
    dao = AlloggioDAO()
    servizi = dao.visualizzaservizidisponibili()
    return render_template("CaricaAnnuncio.html", servizi=servizi)


@gu2.route('/Carica', methods=['POST'])
def pubblicazione():
    titolo = request.form.get("titolo")
    indirizzo = request.form.get("indirizzo")
    cap = request.form.get("cap")
    cap = int(cap)
    provincia = request.form.get("provincia")
    citta = request.form.get("citta")
    tipo = request.form.get("tipo")
    descrizione = request.form.get("descrizione")
    num_bagni = request.form.get("num_bagni")
    num_bagni = int(num_bagni)
    num_camere = request.form.get("num_camere")
    num_camere = int(num_camere)
    classe_energetica = request.form.get("classee")
    num_ospiti = request.form.get("num_ospiti")
    num_ospiti = int(num_ospiti)
    metri_quadri = request.form.get("metri_quadri")
    metri_quadri = int(metri_quadri)
    prezzo = request.form.get("prezzo")
    prezzo = double(prezzo)
    periodo_minimo = request.form.get("periodo_minimo")
    periodo_minimo = int(periodo_minimo)
    pannelli_fotovoltaici = 1 if request.form.get("pannelli_fotovoltaici") else 0
    pannelli_solari = 1 if request.form.get("pannelli_solari") else 0
    arredamento = 1 if request.form.get("arredamento") else 0
    civico = request.form.get("civico")
    data = datetime.now().strftime("%Y-%m-%d")
    mail = session["email"]
    servizi_selezionati = request.form.get("servizi_selezionati")
    servizi_selezionati_lista = servizi_selezionati.split(',')
    #pubblicazione_alloggio(titolo, indirizzo, cap, provincia, citta, tipo, descrizione, civico,
     #                      num_bagni, num_camere, classe_energetica, num_ospiti,
      #                     metri_quadri, prezzo, periodo_minimo, arredamento,
       #                    pannelli_fotovoltaici, pannelli_solari, servizi_selezionati_lista, data,mail)
    #return render_template("Homepage.html")
    return render_template("boh.html",
     titolo=titolo,
     indirizzo=indirizzo,
     cap=cap,
     provincia=provincia,
     citta=citta,
     tipo=tipo,
     descrizione=descrizione,
     num_bagni=num_bagni,
     num_camere=num_camere,
     classe_energetica=classe_energetica,
     num_ospiti=num_ospiti,
     metri_quadri=metri_quadri,
     prezzo=prezzo,
     periodo_minimo=periodo_minimo,
      arredamento=arredamento,
       pannelli_fotovoltaici=pannelli_fotovoltaici,
      pannelli_solari=pannelli_solari,
       servizi_selezionati=servizi_selezionati_lista,
     data=data
     )

#Barra di ricerca
@gu2.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        citta = request.form["citta"]
        alloggi = ricerca_alloggio(citta)
        for alloggio in alloggi:
            return render_template("output.html", alloggi=alloggi) #se tutto va bene reinderizzi alla futura visualizza alloggio
    return render_template("Homepage.html") #output per il get se non sono presenti alloggi


@gu2.route('/Homecheck', methods=['GET', 'POST'])
def homechecker():
    if request.method == 'POST':
        id_alloggio = request.form.get('id_alloggio')


        if id_alloggio is not None and id_alloggio.isdigit():  # Verifica se id_alloggio è un numero intero
            dao = AlloggioDAO()
            dao.homecheckgood(int(id_alloggio))
            return redirect(url_for('gu2.homechecker'))
        else:
            return 'Invalid data received for id_alloggio', 400

    else:
        dao = AlloggioDAO()
        alloggi = dao.homecheck()
        immagini = []
        for alloggio in alloggi:
            id_alloggio = alloggio.get_id_alloggio()
            immagine = dao.visualizzaimg(id_alloggio)
            immagini.append(immagine)
        return render_template("Homecheck.html", immagini=immagini, alloggi=alloggi)