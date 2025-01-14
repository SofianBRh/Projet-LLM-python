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


    probabilites = {lettre: (compteur / total_lettres)*100 for lettre, compteur in compteur_lettres.items()}

    return probabilites

def compter_lettres_precedentes(fichier):
    alphabet = string.ascii_lowercase + "#" + "@"
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

def compter_double_lettres_precedentes(fichier):
    alphabet = string.ascii_lowercase + "#" + "@"
    compteur_lettres = {lettre: {premiere_precedente + deuxieme_precedente: 0 for premiere_precedente in alphabet for deuxieme_precedente in alphabet} for lettre in alphabet}
    total_lettres = {lettre: 0 for lettre in alphabet}

    with open(fichier, 'r', encoding='utf-8') as f:
        for lettre_globale in alphabet:
            f.seek(0)
            for ligne in f:
                mots = ligne.strip().lower().split()
                for mot in mots:
                    for i in range(1, len(mot)):
                        if mot[i] == lettre_globale:
                            premiere_precedente = mot[i-1]
                            if i >= 2:
                                deuxieme_precedente = mot[i-2]
                            else:
                                deuxieme_precedente = "#"

                            paire_precedentes = premiere_precedente + deuxieme_precedente
                            if paire_precedentes in compteur_lettres[lettre_globale]:
                                compteur_lettres[lettre_globale][paire_precedentes] += 1
                                total_lettres[lettre_globale] += 1

            print(lettre_globale, " : ", total_lettres[lettre_globale])

    probabilites = {lettre: {paire_precedentes: (compteur / total_lettres[lettre])*100 if total_lettres[lettre] != 0 else 0 for paire_precedentes, compteur in compteur_lettres[lettre].items()} for lettre in alphabet}

    return probabilites




# probabilites_lettres = compter_lettres('./liste_francais.txt')

# for lettre, probabilité in probabilites_lettres.items():
#     print(f"La lettre '{lettre}' apparaît avec une probabilité de {probabilité:.4f}")


# probabilites_lettres_precedentes = compter_lettres_precedentes('./liste_francais.txt')

# for lettre, precedentes in probabilites_lettres_precedentes.items():
#     print(f"Lettre: {lettre}")
#     for precedente, proba in precedentes.items():
#         print(f"  Précédente: {precedente}, Fréquence: {proba:.4f}%")
#     print("----")


probabilites_double_lettres_precedentes = compter_double_lettres_precedentes('./liste_francais.txt')

for lettre, double_precedentes in probabilites_double_lettres_precedentes.items():
    print(f"Lettre: {lettre}")
    for double_precedentes, proba in double_precedentes.items():
        print(f"  Précédente: {double_precedentes}, Fréquence: {proba:.8f}%")
    print("----")
