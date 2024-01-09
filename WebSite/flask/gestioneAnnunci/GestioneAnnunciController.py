from flask import Blueprint, request, render_template, session, redirect, url_for, Flask
from datetime import datetime, date

from numpy import double

from .AlloggioDAO import AlloggioDAO
from .GestioneAnnunciService import pubblicazione_alloggio, ricerca_alloggio, ricerca_post_studente, \
    creazione_post, max_id_casa, indirizzo_crea, crea_possedimento, visualizza_servizi, \
    visualizza_annuncio, inserisci_immagini_service, visualizza_servizi_alloggio, visualizza_indirizzo, \
    modifica_annuncio_byid, modifica_indirizzo_byid, preleva_immagini, elimina_alloggio_byid, preleva_data_visita, \
    recensione, cercarec, segnala_service, cercadataacquisto
from .ImmagineDAO import ImmagineDAO
from .Indirizzo import Indirizzo
from .IndirizzoDAO import IndirizzoDAO
from .Possedimento import Possedimento
from .ServiziDAO import ServiziDAO
from WebSite.flask.gestioneAffitto.GestioneAffittoService import ricerca_data_disponibile
from WebSite.flask.gestioneUtente.GestioneUtenteService import idcasas

gu2 = Blueprint('gu2', __name__, template_folder="gestioneAnnunci")

@gu2.route('/page', methods=['GET'])
def catalogo():
    if request.method == "GET":
        citta = session.get("ricerca")
        print("citta" + citta)
        alloggi = ricerca_alloggio(citta)
        print("hey")
        id_alloggi = []
        immagini = []
        if alloggi:
            for row in alloggi:
                print("hey 2")
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
            return redirect(url_for('gu.main')) #output per il get se non sono presenti alloggi
        return render_template("Catalogo.html", immagini=immagini, alloggi=alloggi, citta=citta)


@gu2.route('/Alloggio.html')
def annuncio():

    dao = AlloggioDAO()
    dao2 = ImmagineDAO()
    dao3 = IndirizzoDAO()

    id_alloggio = request.args.get('id') or session.get("id_alloggio")

    #ATTENZIONE
    #importante non eliminare la sessione, serve per un corretto funzionamento di data visita Locatore
    session["id_alloggio"] = id_alloggio

    alloggio = visualizza_annuncio(id_alloggio=id_alloggio)
    servizi = dao.visualizzaservizi(id_alloggio)

    immagini = dao2.recupera_path(id_alloggio=id_alloggio)

    path = []
    for im in immagini:
        path.append(im.get_path())

    for p in path:
        print("PATH:    " + p)

    indirizzo = dao3.visualizzaindirizzo(id_alloggio)

    prenotazione = ricerca_data_disponibile(id_alloggio=id_alloggio)
    data_time = []

    for row in prenotazione:
        d = row.get_data_visita()
        datetime_object = datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S')
        print("AFFITTO -> dataTIME:  " + str(datetime_object))

        data_time.append(datetime_object)

    return render_template("Alloggio.html", alloggio=alloggio, servizi=servizi, indirizzo=indirizzo, immagini = path, data=data_time)

@gu2.route('/CaricaAnnuncio', methods=['GET', 'POST'])
def allservizi():
    if request.method == 'GET':
        servizi = visualizza_servizi()
        return render_template("CaricaAnnuncio.html", servizi=servizi)
    elif request.method == 'POST':
        titolo = request.form.get("titolo")
        indirizzo = request.form.get("indirizzo")
        cap = request.form.get("cap")
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

        cap_con_zero = cap.zfill(5)

        print("titolo:" + titolo)
        print("indirizzo:" + indirizzo)
        print("cap:" + str(cap_con_zero))
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

        session["id_alloggio"] = val_id

        indirizzo2 = Indirizzo(id_alloggio=val_id, via=indirizzo, cap=cap, citta=citta, civico=civico, provincia=provincia)
        indirizzo_crea(indirizzo2)

        for row in servizi_selezionati:
            possedimento = Possedimento(id_alloggio=val_id, id_servizio=row)
            crea_possedimento(possedimento)

        servizi = visualizza_servizi_alloggio(val_id)


        lista_immagini = request.files.getlist("lista_immagini[]")
        nomi_immagini = []

        if lista_immagini:
            nomi_immagini = inserisci_immagini_service(lista_immagini)

        for im in nomi_immagini:
            print(im)
        return render_template("Alloggio.html", alloggio=alloggio, indirizzo=indirizzo2, immagini = nomi_immagini, servizi=servizi)


#Barra di ricerca
@gu2.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        citta = request.form["citta"]
        session["ricerca"] = citta
        print("Sono dentro")
        return redirect(url_for('gu2.catalogo')) #se tutto va bene reinderizzi alla futura visualizza alloggio
    return redirect(url_for('gu2.main')) #output per il get se non sono presenti alloggi


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
        id_alloggi =[]
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
    immagini = []
    for num in session['case_preferite']:
        print(num)
        alloggio = visualizza_annuncio(num)
        alloggi.append(alloggio)
        count = 0
        path = preleva_immagini(num)
        for p in path:
            if count == 0:
                print("pathricerca:     " + p)
                immagini.append(p)
                count = 1
    print(immagini)
    return render_template("ListaPreferiti.html",alloggi=alloggi,immagini=immagini)


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
    print("id_alloggio fuori: " + id_alloggio)
    if id_alloggio:
        case_preferite = session['case_preferite']
        case_preferite.remove(id_alloggio)
        session['case_preferite'] = case_preferite
    source_url = request.referrer  # Ottieni l'URL della pagina precedente
    if source_url:
        return redirect(source_url)

@gu2.route('/ModificaAnnuncio', methods=['GET', 'POST'])
def modifica_annuncio():
    if request.method=='GET':
        id_alloggio = request.args.get('id')
        alloggio = visualizza_annuncio(id_alloggio=id_alloggio)
        indirizzo = visualizza_indirizzo(id_alloggio)
        print("indirizzo: " + indirizzo.get_citta())
        session["id_alloggio"] = id_alloggio
        print("ID ALLOGGIO GET: " + session["id_alloggio"])
        return render_template("ModificaAlloggio.html", alloggio=alloggio, indirizzo=indirizzo)
    elif request.method=='POST':
        id_ = session.get("id_alloggio")
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
        periodo_minimo_str = request.form.get("periodo_minimo", "")
        if periodo_minimo_str:
            periodo_minimo = int(periodo_minimo_str)
        else:
            # Tratta il caso in cui il valore sia vuoto, ad esempio assegnando un valore predefinito.
            periodo_minimo = 0  # o qualsiasi altro valore di default che si desidera assegnare
        pannelli_fotovoltaici = 1 if request.form.get("pannelli_fotovoltaici") else 0
        pannelli_solari = 1 if request.form.get("pannelli_solari") else 0
        arredamento = 1 if request.form.get("arredamento") else 0
        civico = request.form.get("civico")
        data = datetime.now().strftime("%Y-%m-%d")
        mail = session.get("email")
        servizi_selezionati = request.form.getlist('checkboxGroup')

        print("id: " + str(id_))
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

        alloggio = modifica_annuncio_byid(id_allogio=id_, tipo_alloggio=tipo, titolo=titolo, mq=metri_quadri, n_camere_letto=num_camere,
                                          n_bagni=num_bagni, classe_energetica=classe_energetica,
                                          arredamenti=arredamento, data_pubblicazione=data,
                                          pannelli_solari=pannelli_solari, pannelli_fotovoltaici=pannelli_fotovoltaici,
                                          descrizione=descrizione, prezzo=prezzo,
                                          n_ospiti=num_ospiti, n_stanze=num_camere, tasse=prezzo - 20)

        indirizzo2 = Indirizzo(id_alloggio=id_, via=indirizzo, cap=cap, citta=citta, civico=civico,
                               provincia=provincia)
        modifica_indirizzo_byid(id_alloggio=id_, indirizzo=indirizzo2)

        servizi = visualizza_servizi_alloggio(id_)

        path = preleva_immagini(id_)

        return render_template("Alloggio.html", alloggio=alloggio, indirizzo=indirizzo2, immagini=path,
                               servizi=servizi)

#da concludere
@gu2.route('/elimina_post', methods=['POST'])
def elimina_annuncio():
    if request.method == 'POST':
        id_alloggio = session.get("id_alloggio")
        elimina_alloggio_byid(id_alloggio)
        return render_template("Userpage.html")


@gu2.route('/data_visita')
def data_visita_locatore():
    id_alloggio = request.args.get('id') or session.get("id_alloggio")
    print("id_alloggio fuori: " + str(id_alloggio))

    prenotazione = preleva_data_visita(id_alloggio=id_alloggio)
    data_time = []

    for row in prenotazione:
        d = row.get_data_visita()
        datetime_object = datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S')
        print("AFFITTO -> dataTIME:  " + str(datetime_object))

        data_time.append(datetime_object)

    return render_template("DataVisita.html", data=data_time)


@gu2.route('/Segnala', methods=['GET', 'POST'])
def segnala():
    if request.method == 'POST':
        #prendo id alloggio dalla sessione
        id_alloggio = session.get("id_alloggio")
        #richiamo l'alloggio con id da visualizza_alloggio
        alloggio = visualizza_annuncio(id_alloggio=id_alloggio)
        email = session.get("email")
        #prendo il valore di emailS dalla funzione get email loc
        emailS = alloggio.get_email_loc()
        motivo = request.form.get('motivo')


        # Chiamata al servizio di segnalazione
        segnala_service(email, emailS, motivo)  #stato non è passato perchè è settato a aperto quando creato nel DAO

        return redirect(url_for('gu2.segnala_successo', id_alloggio=id_alloggio))

    return render_template("Segnala.html")


@gu2.route('/segnala_successo')
def segnala_successo():
    return render_template("segnala_successo.html")





@gu2.route("/recensione")
def inseriscirec():
    data_oggi = date.today()
    id_alloggio = int(request.args.get('id') or session.get("id_alloggio"))
    email=session["email"]
    id_casa = int(idcasas(email, data_oggi))
    print(id_casa,id_alloggio)
    data_acquisto = cercadataacquisto(email,id_alloggio)
    print("DATAOGGI")
    print(data_oggi)
    print("DATAACQUISTO")
    print(data_acquisto)
    diff = data_oggi - data_acquisto
    diff = diff.days
    print(diff)
    if id_casa == id_alloggio and diff>30:
        rec = cercarec(id_alloggio, email)
        print("SONO QUI")
        return render_template("Recensione.html", id=id_alloggio, rec=rec)
    else:
        if diff<30:
            session["alert"]=id_alloggio
        return redirect(url_for('gu.userpage'))

@gu2.route("/recensisci", methods=['POST'])
def recensisci():
    if request.method == 'POST':
        id_alloggio = request.form.get("id")
        print(id_alloggio)
        titolo = request.form.get("titolo")
        descrizione = request.form.get("descrizione")
        email = session["email"]
        voto = request.form.get("voto")
        data = datetime.now().strftime("%Y-%m-%d")
        print(id_alloggio, titolo, descrizione, email, voto, data)
        recensione(id_alloggio, titolo, descrizione, voto, data, email)
        return redirect(url_for('gu.userpage'))


