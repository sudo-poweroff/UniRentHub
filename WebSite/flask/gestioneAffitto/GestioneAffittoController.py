from flask import Blueprint, request, render_template, session, redirect, url_for, Flask, jsonify
from datetime import datetime

from WebSite.flask.gestioneAffitto.GestioneAffittoService import insert_data_byId, delete_data_byId
from WebSite.flask.gestioneAffitto.Prenotazione import Prenotazione
from WebSite.flask.gestioneAnnunci.GestioneAnnunciService import preleva_data_visita

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


