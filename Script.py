import string

def compter_lettres(fichier):
    compteur_lettres = dict.fromkeys(string.ascii_lowercase, 0)
    total_lettres = 0

    with open(fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            mots = ligne.strip().lower().split()
            for mot in mots:
                for lettre in mot:
                    if lettre in compteur_lettres:
                        compteur_lettres[lettre] += 1
                        total_lettres += 1

    probabilites = {lettre: (compteur / total_lettres) for lettre, compteur in compteur_lettres.items()}

    return probabilites
probabilites_lettres = compter_lettres('chemin/vers/le/fichier.txt')

for lettre, probabilité in probabilites_lettres.items():
    print(f"La lettre '{lettre}' apparaît avec une probabilité de {probabilité:.4f}")
