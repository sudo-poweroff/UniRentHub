from flask import Flask
from flask_mail import Mail

from gestioneUtente.GestioneUtenteController import gu
from gestioneAnnunci.GestioneAnnunciController import gu2
from gestioneAffitto.GestioneAffittoController import gu3

app = Flask(__name__)



app.secret_key = 'hello'
app.debug = True

app.register_blueprint(gu)
app.register_blueprint(gu2)
app.register_blueprint(gu3)

if __name__ == '__main__':
    app.run()
