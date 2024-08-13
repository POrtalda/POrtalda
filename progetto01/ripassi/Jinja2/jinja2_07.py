# Importa il modulo Flask
from flask import Flask, render_template

punteggio_massimo = 100
nome_test = "Sfida Python"

studenti = [
    {"name": "Sabrina", "score": 100},
    {"name": "Giorgio", "score": 87},
    {"name": "Sofia", "score": 92},
    {"name": "Francesco", "score": 40},
    {"name": "Sirio", "score": 75},
]

# Crea un'istanza di Flask
app = Flask(__name__)

# Crea una route che risponda a GET /

@app.route("/")

def home():
    return render_template("base_block.html",title="Jinja2 e Flask")

@app.route("/results")

def results():
    context = {
        "title": "Risultati",
        "students": studenti,
        "test_name": nome_test,
        "max_score": punteggio_massimo,
    }

    return render_template("template_ris_block.html", **context)


# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)