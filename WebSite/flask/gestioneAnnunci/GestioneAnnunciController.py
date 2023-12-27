from flask import Blueprint, request, render_template, session, redirect, url_for, Flask

from .AnnuncioDAO import AnnuncioDAO
from .GestioneAnnunciService import pubblicazione_post


gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")


@gu2.route('/CreatePost', methods=['POST', 'GET'])
def creaPost():
    if request.method == 'POST':
        email = session["email"]
        titolo = request.form["titolo"]
        descrizione = request.form["descrizione"]

        post = pubblicazione_post(email = email, titolo = titolo, descrizione = descrizione)
        if post:
            return render_template("output.html", descrizione=descrizione, email= email)
    elif request.method == "GET":
        return render_template("CreatePost.html")
    return render_template("LoginCliente.html", message="Metodo di richiesta non valido")

@gu2.route('/Catalogo.html')
def catalogo():
    dao = AnnuncioDAO()
    alloggi = dao.visualizza()
    immagini = []
    for alloggio in alloggi:
        id_alloggio = alloggio[0]
        immagine = dao.visualizzaimg(id_alloggio)
        immagini.append(immagine)
    return render_template("catalogo.html", immagini=immagini,alloggi=alloggi)


@gu2.route('/Annuncio.html')
def annuncio():
    dao = AnnuncioDAO()
    id_alloggio = request.args.get('id')
    alloggio = dao.visualizzaannuncio(id_alloggio)
    servizi = dao.visualizzaservizi(id_alloggio)
    immagini = dao.visualizzaimmagini(id_alloggio)

    return render_template("Annuncio.html", alloggio=alloggio, servizi=servizi, immagini=immagini)

@gu2.route('/CaricaAnnuncio.html')
def allservizi():
    dao = AnnuncioDAO()
    servizi = dao.visualizzaservizidisponibili()
    return render_template("CaricaAnnuncio.html",servizi=servizi)

@gu2.route('/Carica', methods=['POST'])
def pubblicazione():
    titolo = request.form.get("titolo")
    indirizzo = request.form.get("indirizzo")
    cap = request.form.get("cap")
    provincia = request.form.get("provincia")
    citta = request.form.get("citta")
    tipo = request.form.get("tipo")
    descrizione = request.form.get("Descrizione")
    num_bagni = request.form.get("num_bagni")
    num_camere = request.form.get("num_camere")
    classe_energetica = request.form.get("classee")
    num_ospiti = request.form.get("num_ospiti")
    metri_quadri = request.form.get("metri_quadri")
    prezzo = request.form.get("prezzo")
    periodo_minimo = request.form.get("periodo_minimo")
    pannelli_fotovoltaici = request.form.get("pannelli_fotovoltaici")
    pannelli_solari = request.form.get("pannelli_solari")
    arredamento = request.form.get("arredamento")
    dao = AnnuncioDAO()
    servizi = dao.visualizzaservizidisponibili()
    servizi_selezionati = []
    for key, value in request.form.items():
        if key.startswith('servizio_') and value == 'on':
            servizio_selezionato = key.split('_')[1]  # Ottieni l'ID dell'elemento selezionato
            servizi_selezionati.append(servizio_selezionato)


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
                           servizi_selezionati=servizi_selezionati
    )





