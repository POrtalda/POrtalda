import os
from jinja2 import Environment, FileSystemLoader

# Definizione delle variabili per i placeholder
max_score = 100  
test_name = "Flask Challenge"  
students = [      
    {"name": "Sandro",  "score": 100},      
    {"name": "Gerry", "score": 60},      
    {"name": "Federica", "score": 92},
    {"name": "Samuele", "score": 20},
]

# Configurazione dell'ambiente Jinja2
environment = Environment(loader=FileSystemLoader("progetto01/ripassi/Jinja2/Templates"))  
template = environment.get_template("template_ris.html")

# Definizione del contenuto da passare al template
content = {
    "students": students,          
    "max_score": max_score,          
    "test_name": test_name,      
}

# Definizione della directory di output e del percorso completo del file
output_dir = "progetto01/ripassi/Jinja2/File_.html_creati"
os.makedirs(output_dir, exist_ok=True)  # Crea la directory se non esiste
results_html = os.path.join(output_dir, "risultati_studenti.html")

# Creazione e salvataggio del file HTML
with open(results_html, mode="w", encoding="utf-8") as results:
    results.write(template.render(content))
    
print(f"File salvato in: {results_html}")
