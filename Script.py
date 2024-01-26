from collections import defaultdict
import string
import random

def lire_fichier(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        mots = f.read().split('#')
    return [mot.replace('@', '') for mot in mots if mot]

# Fonction pour calculer les probabilités des lettres
def calculer_probabilites_lettres(mots):
    compteur = dict.fromkeys(string.ascii_lowercase, 0)
    total_lettres = 0

    for mot in mots:
        for lettre in mot.lower():
            if lettre in compteur:
                compteur[lettre] += 1
                total_lettres += 1

    probabilites = {lettre: compteur[lettre] / total_lettres for lettre in compteur if compteur[lettre] > 0}
    return probabilites

def calculer_probabilites_lettres_precedentes(mots):
    compteur = defaultdict(lambda: defaultdict(int))
    total_precedentes = defaultdict(int)

    for mot in mots:
        for i in range(1, len(mot)):
            actuelle, precedente = mot[i].lower(), mot[i-1].lower()
            if actuelle in string.ascii_lowercase and precedente in string.ascii_lowercase:
                compteur[actuelle][precedente] += 1
                total_precedentes[precedente] += 1

    probabilites = {lettre: {precedente: compteur[lettre][precedente] / total_precedentes[precedente]
                             for precedente in compteur[lettre]}
                    for lettre in compteur}
    return probabilites

def generer_mot(probabilites, longueur_max):
    lettres_possibles = [lettre for lettre in probabilites.keys() if lettre not in ['#', '@']]
    lettre_actuelle = random.choice(lettres_possibles)
    mot = lettre_actuelle

    for _ in range(1, longueur_max):
        suivantes = probabilites.get(lettre_actuelle, {})
        total = sum(suivantes.values())
        
        if total == 0:
            break

        suivantes_filtrées = {lettre: freq for lettre, freq in suivantes.items() if lettre not in ['#', '@']}
        poids = [freq / total for freq in suivantes_filtrées.values()]

        if not poids:
            break

        lettre_actuelle = random.choices(list(suivantes_filtrées.keys()), weights=poids, k=1)[0]
        mot += lettre_actuelle

    return mot

mots = lire_fichier('./liste_francais.txt')
probabilites_lettres_precedentes = calculer_probabilites_lettres_precedentes(mots)

liste_mots_genere = generer_mot(probabilites_lettres_precedentes, 5)
print("Liste de mots générés :", liste_mots_genere)
