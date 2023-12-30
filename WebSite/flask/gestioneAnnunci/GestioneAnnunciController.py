from flask import Blueprint, request, render_template, session, redirect, url_for, Flask
from datetime import datetime

from numpy import double

from .AlloggioDAO import AlloggioDAO
from .GestioneAnnunciService import pubblicazione_post, pubblicazione_alloggio, ricerca_alloggio, ricerca_post_studente, \
    creazione_post, inserisci_immagini, max_id_casa, indirizzo_crea, crea_possedimento, visualizza_servizi, \
    visualizza_annuncio
from .Indirizzo import Indirizzo
from .IndirizzoDAO import IndirizzoDAO
from .Possedimento import Possedimento
from .ServiziDAO import ServiziDAO

gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")

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


@gu2.route('/Alloggio.html')
def annuncio():

    dao = AlloggioDAO()
    dao2 = ServiziDAO()
    dao3 = IndirizzoDAO()

    id_alloggio = request.args.get('id')
    alloggio = visualizza_annuncio(id_alloggio=id_alloggio)
    servizi = dao.visualizzaservizi(id_alloggio)
   # immagini = dao.visualizzaimmagini(id_alloggio)
    indirizzo = dao3.visualizzaindirizzo(id_alloggio)

    return render_template("Alloggio.html", alloggio=alloggio, servizi=servizi, indirizzo=indirizzo)

@gu2.route('/CaricaAnnuncio', methods=['GET', 'POST'])
def allservizi():
    if request.method == 'GET':
        servizi = visualizza_servizi()
        return render_template("CaricaAnnuncio.html", servizi=servizi)
    elif request.method == 'POST':
        titolo = request.form.get("titolo")
        indirizzo = request.form.get("indirizzo")
        cap = int(request.form.get("cap", 0))
        provincia = request.form.get("provincia")
        citta = request.form.get("citta")
        tipo = request.form.get("tipo")
        descrizione = request.form.get("descrizione")
        num_bagni = int(request.form.get("num_bagni", 0))
        num_camere = int(request.form.get("num_camere", 0))
        classe_energetica = request.form.get("classee")
        num_ospiti = int(request.form.get("num_ospiti", 0))
        metri_quadri = int(request.form.get("metri_quadri", 0))
        prezzo = float(request.form.get("prezzo", 0.0))
        periodo_minimo = int(request.form.get("periodo_minimo", 0))
        pannelli_fotovoltaici = 1 if request.form.get("pannelli_fotovoltaici") else 0
        pannelli_solari = 1 if request.form.get("pannelli_solari") else 0
        arredamento = 1 if request.form.get("arredamento") else 0
        civico = request.form.get("civico")
        data = datetime.now().strftime("%Y-%m-%d")
        mail = session.get("email")
        servizi_selezionati = request.form.getlist('checkboxGroup')

        print("titolo:" + titolo)
        print("indirizzo:" + indirizzo)
        print("cap:" + str(cap))
        print("provincia:" + provincia)
        print("citta:" + citta)
        print("tipo:" + tipo)
        print("descrizione:" + descrizione)
        print("num_bagni:" + str(num_bagni))
        print("num_camere:" + str(num_camere))
        print("classe_energetica:" + classe_energetica)
        print("num_ospiti:" + str(num_ospiti))
        print("metri_quadri:" + str(metri_quadri))
        print("prezzo:" + str(prezzo))
        print("periodo_minimo:" + str(periodo_minimo))
        print("pannelli_fotovoltaici:" + str(pannelli_fotovoltaici))
        print("pannelli_solari:" + str(pannelli_solari))
        print("arredamento:" + str(arredamento))
        print("civico:" + civico)
        print("data:" + data)
        print("mail:" + mail)
        print("servizi_selezionati:" + str(servizi_selezionati))


        alloggio = pubblicazione_alloggio(tipo_alloggio=tipo, titolo=titolo, mq=metri_quadri, n_camere_letto= num_camere, n_bagni=num_bagni, classe_energetica=classe_energetica,
                               arredamenti=arredamento, data_pubblicazione=data, pannelli_solari=pannelli_solari, pannelli_fotovoltaici=pannelli_fotovoltaici, descrizione=descrizione, prezzo=prezzo,
                               n_ospiti=num_ospiti, n_stanze=num_camere, tasse=prezzo-20, email_loc=mail)

        val_id = max_id_casa()
        print("ID: " + str(val_id))

        indirizzo2 = Indirizzo(id_alloggio=val_id, via=indirizzo, cap=cap, citta=citta, civico=civico, provincia=provincia)
        indirizzo_crea(indirizzo2)

        for row in servizi_selezionati:
            possedimento = Possedimento(id_alloggio=val_id, id_servizio=row)
            crea_possedimento(possedimento)

        return render_template("Alloggio.html", alloggio=alloggio, indirizzo=indirizzo2)


#Barra di ricerca
@gu2.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        citta = request.form["citta"]
        alloggi = ricerca_alloggio(citta)
        for alloggio in alloggi:
            return render_template("Catalogo.html", alloggi=alloggi) #se tutto va bene reinderizzi alla futura visualizza alloggio
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

    if request.method == 'GET':
        dao = AlloggioDAO()
        alloggi = dao.homecheck()
        immagini = []
        for alloggio in alloggi:
            id_alloggio = alloggio.get_id_alloggio()
            immagine = dao.visualizzaimg(id_alloggio)
            immagini.append(immagine)
        return render_template("Homecheck.html", immagini=immagini, alloggi=alloggi)


@gu2.route('/community_post', methods=['GET', 'POST'])
def community_post():
    print("SONO QUI")
    if request.method == 'POST':
        print("SONO DENTRO")
        hidden = request.form["button"]
        session["citta"] = hidden
        print("VALUE: " + str(hidden))
        return redirect(url_for("gu2.post"))
    return render_template("CommunityPosts.html")


@gu2.route('/community_post_view', methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        hidden = session["citta"]
        posts = ricerca_post_studente(hidden)
        for post in posts:
            print("Email: " + str(post.get_email()))
        return render_template("CommunityPosts.html", posts = posts, hidden = hidden)


@gu2.route('/community_crea_post', methods=['GET', 'POST'])
def crea_post():
    if request.method == 'GET':
        return render_template("CreatePost.html")
    if request.method == 'POST':

        titolo = request.form["titolo"]
        descrizione = request.form["descrizione"]
        print("\n" + titolo +"\n\n")
        print(descrizione)
        email = session["email"]
        hidden = session["citta"]
        creazione_post(titolo, descrizione, email)

        return redirect(url_for("gu2.post"))


@gu2.route('/ListaPreferiti.html',methods=['GET', 'POST'])
def lista():
    alloggi=[]
    for num in session['case_preferite']:
        print(num)
        dao = AlloggioDAO()
        alloggio = dao.visualizzaannuncio(num)
        alloggi.append(alloggio)

    return render_template("ListaPreferiti.html",alloggi=alloggi)


@gu2.route('/Preferiti',methods=['GET', 'POST'])
def preferiti():
    if 'case_preferite' not in session:
        session['case_preferite'] = []
    id_alloggio = request.args.get('id')
    print("IDALLOGGIO: " + str(id_alloggio))

    if id_alloggio:
        if id_alloggio in session['case_preferite']:
            print("Gia inserito")
        else:
            case_preferite = session['case_preferite']
            case_preferite.append(id_alloggio)
            session['case_preferite'] = case_preferite
            print("Inserito")

    source_url = request.referrer  # Ottieni l'URL della pagina precedente
    if source_url:
        return redirect(source_url)


@gu2.route('/RimuoviP',methods=['GET', 'POST'])
def rimuovip():
    id_alloggio = request.args.get('id')
    if id_alloggio:
        case_preferite = session['case_preferite']
        case_preferite.remove(id_alloggio)
        session['case_preferite'] = case_preferite
    source_url = request.referrer  # Ottieni l'URL della pagina precedente
    if source_url:
        return redirect(source_url)

