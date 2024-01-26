import string
import random

# Fonction pour compter les lettres
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

    probabilites = {lettre: (compteur / total_lettres)*100 for lettre, compteur in compteur_lettres.items()}
    return probabilites

# Fonction pour compter les lettres précédentes
def compter_lettres_precedentes(fichier):
    alphabet = string.ascii_lowercase
    compteur_lettres = {lettre: {precedente: 0 for precedente in alphabet} for lettre in alphabet}
    total_lettres = 0

    with open(fichier, 'r', encoding='utf-8') as f:
        for ligne in f:
            mots = ligne.strip().lower().split()
            for mot in mots:
                for i in range(1, len(mot)):
                    lettre = mot[i]
                    precedente = mot[i - 1]

                    if lettre in compteur_lettres and precedente in compteur_lettres[lettre]:
                        compteur_lettres[lettre][precedente] += 1
                        total_lettres += 1

    probabilites = {lettre: {precedente: (compteur / total_lettres)*100 for precedente, compteur in precedentes.items()} for lettre, precedentes in compteur_lettres.items()}
    return probabilites

# Fonction pour générer un mot
def generer_mot(probabilites, longueur_max):
    lettres_possibles = [lettre for lettre in probabilites.keys()]
    lettre_actuelle = random.choice(lettres_possibles)
    mot = lettre_actuelle

    for _ in range(1, longueur_max):
        suivantes = probabilites.get(lettre_actuelle, {})
        total = sum(suivantes.values())
        
        if total == 0:
            break

        suivantes_filtrées = {lettre: freq for lettre, freq in suivantes.items()}
        poids = [freq / total for freq in suivantes_filtrées.values()]

        if not poids:
            break

        lettre_actuelle = random.choices(list(suivantes_filtrées.keys()), weights=poids, k=1)[0]
        mot += lettre_actuelle

    return mot

# Génération des probabilités avec compter_lettres_precedentes
probabilites_lettres_precedentes = compter_lettres_precedentes('./liste_francais.txt')

# Utilisation de la fonction generer_mot originale
mot_genere = generer_mot(probabilites_lettres_precedentes, 5)
print("Mot généré:", mot_genere)