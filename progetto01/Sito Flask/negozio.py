from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)