# Importa il modulo Flask
from flask import Flask, render_template

# Crea un'istanza di Flask
app = Flask(__name__)

# Crea una route che risponda a GET /
@app.route("/")

def home():
    return render_template("base.html",title="Jinja2 e Flask")

# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)