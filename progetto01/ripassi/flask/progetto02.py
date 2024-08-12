# Importa il modulo Flask
from flask import Flask

# Crea un'istanza di Flask
app = Flask(__name__)

nominativo="Carlo"

# Crea una route che risponda a GET /
@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <title>Ciao mondo!</title>
        </head>
        <body>
            <h1>Ciao mondo, {nome}!</h1>
        </body>
    </html>
    """.format(nome=nominativo)

# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)