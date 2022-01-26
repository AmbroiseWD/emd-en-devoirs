class User :
    'pour les utilisateurs'

    def __init__(self,nom,mail,paswd,bool='false'):
        self.nom = nom
        self.mail = mail
        self.paswd = paswd

    def getAttributs(self):
        print("les attributs sonts : nom: ",self.nom," mail ",self.mail, " paswd ",self.paswd)

    def hello(self):
        print("hey my login is : ",self.nom)

class AdminUser(User,bool='true') :
    'pour les administrateurs'
    def helloAdmin(self):
        print("Good morning i am admin there : ",self.nom)

def fonctionDecorateur(nomFonction):
    for compteur in range(2) :
        nomFonction()
def fonctionArnaquer(valeur):
    return valeur*90/100

fileName = "fichier.txt"
def analyseDeText(fileName):
    with open(fileName) as f:
        lines = f.read().splitlines()
        nb_lines = len(lines)
        nb_chars = 0
        for line in lines:
            for char in line:
               nb_chars += 1
        from pathlib import Path
        Path(fileName).stat()
        file_size = Path(fileName).stat().st_size
        print("votre fichier comporte : ",nb_lines,"lignes et ",nb_chars," caractères et pèse", file_size, "bytes")

