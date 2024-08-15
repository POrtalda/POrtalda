from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='/static')
# inizializzazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///negozio.db'
db = SQLAlchemy(app)

#definizione del modello
class Prodotto(db.Model):
    __tablename__ = 'Prodotto'
    id = db.Column(db.Integer(), primary_key=True)
    servizio = db.Column(db.String(length=30), nullable=False, unique=True)
    codice = db.Column(db.String(length=12), nullable=False, unique=True)
    prezzo = db.Column(db.Integer(), nullable=False)
    descrizione = db.Column(db.String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Prodotto {self.name}'
      
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# lettura dei record e rendering nella pagina
@app.route('/market')
def market():
    items = Prodotto.query.all()
    return render_template('market.html', items=items)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)