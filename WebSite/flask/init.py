from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(host='localhost', port='3306', database='unirenthub', user='root', password='ciccio')
cursor = connection.cursor()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/home')
def python():
    cursor.execute("SELECT * FROM Cliente")
    value = cursor.fetchall()
    return render_template("index.html", value=value)


if __name__ == '__main__':
    app.run()
