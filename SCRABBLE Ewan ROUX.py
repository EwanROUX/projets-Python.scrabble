import random

mots_niveau_1 = ['chat', 'lire', 'race', 'rose', 'tire', 'trou', 'haut', 'tour', 'tuer', 'ivre', 'crie', 'lune', 'nuit', 'jour']  # difficulté Facile
mots_niveau_2 = ['maison', 'camion', 'chaise', 'chalet', 'bonne', 'lapin', 'banque', 'boire', 'joueur', 'cahier']  # difficulté Moyenne
mots_niveau_3 = ['vertical', 'plongeur', 'trancher','hachera', 'changer', 'manager']  # difficulté Difficile

def melanger_lettres(mots):
    lettres = "".join(mots)  # .join = Mets tous les mots en une seule chaîne
    lettres_unique = "".join(set(lettres))  # Supprime les doublons
    lettres_melangees = "".join(random.sample(lettres_unique, len(lettres_unique)))  # Mélange les lettres aléatoirement
    return lettres_melangees

def choisir_mots_pour_manche(manche):
    if manche == 1:
        mots_a_trouver = random.sample(mots_niveau_1, 3)
    elif manche == 2:
        mots_a_trouver = random.sample(mots_niveau_2, 3)
    else:
        mots_a_trouver = random.sample(mots_niveau_3, 3)
    return mots_a_trouver

def jouer_manche(manche):
    mots_a_trouver = choisir_mots_pour_manche(manche)  # Permets de recuprer les mots à trouver pour la manche actuelle
    lettres_melangees = melanger_lettres(mots_a_trouver)  # Mélange les lettres de ces mots pour les afficher en une liste aleatoire

    print(f"-- Manche {manche} --")
    print(f"Difficulté : {'Facile' if manche == 1 else 'Moyenne' if manche == 2 else 'Difficile'}")
    print(f"Les lettres mélangées sont :", lettres_melangees)
    print("Trouvez les mots cachés.")

    mots_trouves = []
    for _ in range(3):  # 3 tentatives par manche
        mot = input("Entrez un mot ou 'quit' pour passer à la prochaine manche : ").lower()  # .lower permet de convertir les mots en minuscule
        if mot == 'quit':
            print("Passage à la prochaine manche.")
            return mots_trouves
        if mot in mots_a_trouver and mot not in mots_trouves:
            mots_trouves.append(mot)
            print(f"Bravo ! Vous avez trouvé le mot : {mot}")
        elif mot in mots_trouves:
            print(f"Le mot '{mot}' a déjà été trouvé dans cette manche.")
        else:
            print(f"Le mot '{mot}' n'est pas dans la liste.")

    return mots_trouves


def jeu_scrabble():
    print("Bienvenue au 'Mini Scrabble' !")
    print("Votre but est de trouver les 3 mots cachés parmi les 3 manches qui vont suivre, dans chacunes des listes de lettres mélangées qui vous seront fournies.")
    print("Vous avez 3 manches, chacune comportant 3 tentatives pour trouver les 3 mots cachés.")
    print("Chaque manche a une difficulté différente :")
    print("-- Facile : 3 mots de 4 lettres")
    print("-- Moyenne : 3 mots de 6 lettres")
    print("-- Difficile : 3 mots de 7 à 8 lettres")
    print("Les mots sont de difficulté croissante à chaque manche.")
    print("Amusez-vous et bonne chance !")

    score_total = 0

    for manche in range(1, 4):
        mots_trouves = jouer_manche(manche)
        score_manche = len(mots_trouves)
        score_total += score_manche
        print(f"Vous avez gagné {score_manche} point(s) cette manche.")
    print(f"Votre score total est : {score_total} point(s).")
    print("Merci d'avoir joué !")

jeu_scrabble()