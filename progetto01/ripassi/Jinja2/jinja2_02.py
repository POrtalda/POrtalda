from jinja2 import Environment, FileSystemLoader
import os

# definizione delle variabili per i placeholder
max_score = 100  
test_name = "Flask Challenge"  
students = [      
    {"name": "Sandro",  "score": 100},      
    {"name": "Gerry", "score": 87},      
    {"name": "Federica", "score": 92},  
    ]  

# creazione del template
environment = Environment(loader=FileSystemLoader("progetto01/ripassi/Jinja2/Templates"))
template = environment.get_template("messaggio.txt")

# creazione dei singoli file in output
output_dir = "progetto01/ripassi/Jinja2/File_.txt_creati"
os.makedirs(output_dir, exist_ok=True)  # Crea la directory se non esiste

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
