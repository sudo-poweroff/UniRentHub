from flask import Flask
from gestioneUtente.GestioneUtenteController import gu
from gestioneAnnunci.GestioneAnnunciController import gu2

app = Flask(__name__)
app.secret_key = 'hello'
app.debug = True

app.register_blueprint(gu)
app.register_blueprint(gu2)


if __name__ == '__main__':
    app.run()
