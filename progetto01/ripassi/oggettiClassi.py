# Introduzione alla programmazone ad oggetti
# In python tutto è un oggetto
# proprietà e metodi

# esempio iniziale


# definisco la classe
class persona:
    età = 30
    nome = "Mario"

#istanzio un oggetto

p1 = persona()
print(p1.età,p1.nome)


# miglioriamo la classe

class persona:
  # metodo costruttore  
  def __init__(self, nome, età):
    self.nome = nome
    self.età = età

p2 = persona("luigi",40)
print(p2.età,p2.nome)


# aggiungiamo metodi alla classe

class persona:
  # metodo costruttore  
  def __init__(self, nome, età):
    self.nome = nome
    self.età = età

  def saluti(self):
      print("Ciao, il mio nome è: " + self.nome)


p3 = persona("luigi",40)
print(p3.età,p3.nome)
p3.saluti()

# modificare gli attributi di una classe

p3.età = 45
p3.nome = "Luigi Rossi"
print(p3.età,p3.nome)

# elimare un parametro o un oggetto

del p3.età 
del p3

# ereditarietà

class tecnico(persona):
  pass

t1 = tecnico("Sergio Bianchi",30)
t1.saluti()

# esempio completo con attributo

class tecnico(persona):
  def __init__(self, nome, età, anno):
    super().__init__(nome, età)
    self.inizioAttività = anno

t2 = tecnico("Lisa Giallo", 35, 2019)

# esempio completo con metodo specializzato


class tecnico(persona):
  def __init__(self, nome, età, anno):
    super().__init__(nome, età)
    self.inizioAttività = anno

  def saluti(self):
      print("Ciao, il mio nome è: " + self.nome + " sono tecnico dall'anno: " + str(self.inizioAttività))

t3 = tecnico("Mirco Bruno", 40, 2015)

print(t3.saluti())






