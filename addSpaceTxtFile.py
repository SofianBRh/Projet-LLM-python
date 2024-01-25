with open('./liste_francais.txt', 'r', encoding='utf-8') as f:
    lignes = f.readlines()


with open('./liste_francais.txt', 'w', encoding='utf-8') as f:
    for ligne in lignes:
        f.write(ligne.rstrip() + " \n")

