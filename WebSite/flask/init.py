from flask import Flask
from gestioneUtente.GestioneUtenteController import gu


app = Flask(__name__)
app.secret_key = 'hello'
app.debug = True

app.register_blueprint(gu)


if __name__ == '__main__':
    app.run()
