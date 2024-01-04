from flask import Blueprint, request, render_template, session, redirect, url_for, Flask, jsonify
from datetime import datetime

from WebSite.flask.gestioneAffitto.GestioneAffittoService import insert_data_byId, delete_data_byId, \
    update_disponibilita, date_disponibili_pagamento, affitto_alloggio_cliente, ottieni_date_per_alloggio_byId
from WebSite.flask.gestioneAffitto.Prenotazione import Prenotazione
from WebSite.flask.gestioneAnnunci.GestioneAnnunciService import preleva_data_visita, visualizza_annuncio, \
    preleva_immagini

gu3 = Blueprint('gu3', __name__, template_folder="gestioneAnnunci")

@gu3.route('/insert_data', methods=['GET', 'POST'])
def insert_data():
    if request.method == 'POST':
        id_alloggio = session.get("id_alloggio")
        email = session.get("email")
        datetime_value = request.form.get('datetime')

        data = []
        data1 = []
        prenotazione = preleva_data_visita(id_alloggio)

        for row in prenotazione:
            d = row.get_data_visita()
            data1.append(d)

        for d in data1:
            datetime_object = datetime.strptime(str(d), '%Y-%m-%d %H:%M:%S')
            data.append(datetime_object)
            print("DATA VISIONeds33e2: " + str(datetime_object.date().strftime("%Y-%m-%d %H:%M:%S")))

        print("AFFITTO -> ID ALLOGGIO:  " + str(id_alloggio))
        print("AFFITTO -> EMAIL:  " + email)
        print("AFFITTO -> data:  " + str(datetime_value))

        # Converti la stringa di data e ora in un oggetto datetime
        datetime_object = datetime.strptime(str(datetime_value), '%Y-%m-%dT%H:%M')
        data.append(datetime_object)
        print("AFFITTO -> dataTIME:  " + str(datetime_object))

        prenotazione = Prenotazione(id_alloggio=id_alloggio, email=email, data_visita=datetime_value)
        insert_data_byId(prenotazione)

        return render_template("DataVisita.html", data=data)


@gu3.route('/remove_data', methods=['POST'])
def remove_data():
    if request.method == 'POST':
        date = request.form["button"]
        print("NUOVA DATA RIMOSSA: " + date)
        id_alloggio = session.get("id_alloggio")
        delete_data_byId(id_alloggio=id_alloggio, data_visita=date)

        return redirect(url_for("gu2.data_visita_locatore"))


@gu3.route('/select_data', methods=['POST'])
def update_data():
    if request.method == 'POST':
        date = request.form["button"]
        print("NUOVA DATA: " + date)
        id_alloggio = session.get("id_alloggio")
        print(id_alloggio+"IDIDIDIDIDID")
        update_disponibilita(id_alloggio=id_alloggio, data_visita=date)

        return redirect(url_for("gu2.annuncio"))

@gu3.route('/Pagamento', methods=['POST', 'GET'])
def pagamento():
    if request.method == 'GET':
        val = False
        periodo = True
        id_alloggio = request.args.get('id')
        session['id_alloggio'] = id_alloggio
        print("IDIDIDIDI ->" + str(id_alloggio))
        alloggio = visualizza_annuncio(id_alloggio=id_alloggio)

        immagini = []
        count = 0
        path = preleva_immagini(id_alloggio)
        for p in path:
            if count == 0:
                print("path:     " + p)
                immagini.append(p)
                count = 1

        prezzo = alloggio.get_prezzo()
        periodo_minimo = 3

        # calcolo percentuale
        tmp = (prezzo * 5) / 100
        new_prezzo = prezzo + tmp

        date = ottieni_date_per_alloggio_byId(id_alloggio)

        print("DATEEEEEEEEEEEEEEEEEEE: " + str(date))

        return render_template("Pagamento.html", titolo = alloggio.get_titolo(), immagini=path, prezzo = new_prezzo, val=val, date=date, periodo_minimo=periodo_minimo, periodo=periodo)

    if request.method == 'POST':

        id_alloggio = session['id_alloggio']
        check_in = session['check_in_date']
        check_out = session['check_out_date']
        totale = session['totale']

        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        email = request.form.get("email")
        numero_carta = request.form.get("numeroc")
        mese = request.form.get("mese_scadenza")
        anno = request.form.get("anno_scadenza")
        cvv = request.form.get("cvv")

        print("NOME:    " + nome)
        print("COGNOME: " + cognome)
        print("email:   " + email)
        print("numero_carta:    " + str(numero_carta))
        print("mese: " + str(mese))
        print("anno:   " + str(anno))

        affitto_alloggio_cliente(id_alloggio = id_alloggio, email = email, data_inizio = check_in, data_fine = check_out, numero_carta = numero_carta, mese_scadenza = 11, anno_scadenza = 2025, prezzo = totale)

        return redirect(url_for("gu.userpage"))

@gu3.route('/calcola_prezzo', methods=['GET', 'POST'])
def gestisci_richiesta():
    if request.method == 'POST':
        check_in = request.form.get('checkIn')
        check_out = request.form.get('checkOut')
        id_alloggio = session['id_alloggio']

        # Converti le stringhe in oggetti datetime
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")

        session["check_in_date"] = check_in_date
        session["check_out_date"] = check_out_date

        print("CHECK-IN: " + str(check_in_date))
        print("CHECK-OUT: " + str(check_out_date))
        print("ID_alloggio: " + id_alloggio)

        # Calcola la differenza in mesi
        months_of_stay = (check_out_date.year - check_in_date.year) * 12 + check_out_date.month - check_in_date.month

        print("Mesi di residenza: " + str(months_of_stay))

        alloggio = visualizza_annuncio(id_alloggio=id_alloggio)
        prezzo = alloggio.get_prezzo()
        periodo_minimo = 3

        session["periodo_minimo"] = periodo_minimo
        #cast mese
        months_of_stay = int(months_of_stay)

        # ci prendiamo sempre di default un mese, anche se sta 15 giorni
        if months_of_stay == 0:
            months_of_stay = 1

        #calcolo percentuale
        tmp = (prezzo * 5) / 100
        new_prezzo = prezzo + tmp
        print("NUOVO PREZZO: " + str(new_prezzo))

        last_price = 0
        # se sta un mese non ci serve calcolare anche gli altri mesi
        if months_of_stay != 1:
            #Calcolo mese - 1 per il primo mese
            mese = months_of_stay - 1
            last_price = prezzo * mese
            print("LAST_PRICE: " + str(last_price))

        #calcolo prezzo finale
        totale = last_price + new_prezzo
        print("FINALE:   " + str(totale))

        session['totale'] = totale

        #prelevo immagini path
        immagini = []
        count = 0
        path = preleva_immagini(id_alloggio)
        for p in path:
            if count == 0:
                print("path:     " + p)
                immagini.append(p)
                count = 1

        val = date_disponibili_pagamento(id_alloggio=id_alloggio, data_inizio=check_in_date, data_fine=check_out)
        print("val" + str(val))#Restituisce true se ci sono prenotazioni

        date = ottieni_date_per_alloggio_byId(id_alloggio)

        periodo = True
        if months_of_stay < periodo_minimo:
            periodo = False

        return render_template("Pagamento.html", titolo=alloggio.get_titolo(), immagini=path, prezzo=totale, val=val, date=date, periodo=periodo, periodo_minimo=periodo_minimo)
