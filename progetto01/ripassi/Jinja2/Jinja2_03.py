import os
from jinja2 import Environment, FileSystemLoader

# definizione delle variabili per i placeholder
max_score = 100  
test_name = "Flask Challenge"  
students = [      
    {"name": "Sandro",  "score": 85},      
    {"name": "Gerry", "score": 55},      
    {"name": "Federica", "score": 92},  
    ]  

# configurazione dell'ambiente Jinja2
environment = Environment(loader=FileSystemLoader("progetto01/ripassi/Jinja2/Templates"))  
template = environment.get_template("messaggioif.txt")

# directory di output per i file creati
output_dir = "progetto01/ripassi/Jinja2/File_.txt_creati"
os.makedirs(output_dir, exist_ok=True)  # Crea la directory se non esiste

# creazione dei singoli file in output
for student in students:      
    filename = os.path.join(output_dir, f"messaggio_{student['name'].lower()}.txt")

    content = template.render(         
        student,          
        max_score=max_score,          
        test_name=test_name      
        )
    
    with open(filename, mode="w", encoding="utf-8") as message:          
        message.write(content)          
        print(f"... crea {filename}")
