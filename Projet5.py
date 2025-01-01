import itertools
import time
import matplotlib.pyplot as plt

# Liste de mots de passe courants pour simuler l'attaque
# Liste de mots de passe courants pour simuler l'attaque
mots_de_passe_communs = ["123456", "password", "123456789", "12345", "abc123", "admin", "password123"]


# Fonction pour simuler la vérification d'un mot de passe
def verifier_mot_de_passe(mot_de_passe):
    # Mot de passe correct pour la simulation
    mot_de_passe_correct = "password123"
    return mot_de_passe == mot_de_passe_correct

# Fonction de brute-force sur les mots de passe
def attaque_brute_force(liste_mots_de_passe):
    nombre_reussites = 0
    nombre_echecs = 0
    tentatives_reussies = []
    
    for mot_de_passe in liste_mots_de_passe:
        time.sleep(0.2)  
        if verifier_mot_de_passe(mot_de_passe):
            print(f"Mot de passe trouvé : {mot_de_passe}")
            nombre_reussites += 1
            tentatives_reussies.append(mot_de_passe)
        else:
            nombre_echecs += 1
    
    return nombre_reussites, nombre_echecs, tentatives_reussies

# Fonction pour visualiser les résultats
def visualiser_resultats(nombre_reussites, nombre_echecs):
    labels = ['Réussites', 'Échecs']
    tailles = [nombre_reussites, nombre_echecs]
    
    plt.pie(tailles, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') 
    plt.title('Résultats de l\'attaque brute-force')
    plt.show()

# Fonction principale
def principal():
    print("Lancement de l'attaque brute-force sur les mots de passe...")
    
    # Lancer l'attaque brute-force
    nombre_reussites, nombre_echecs, tentatives_reussies = attaque_brute_force(mots_de_passe_communs)
    
    # Afficher les résultats de l'attaque
    print(f"\nTotal de tentatives réussies : {nombre_reussites}")
    print(f"Total de tentatives échouées : {nombre_echecs}")
    
    # Afficher les mots de passe réussis
    if tentatives_reussies:
        print(f"Mots de passe trouvés : {', '.join(tentatives_reussies)}")
    
    # Visualisation des résultats
    visualiser_resultats(nombre_reussites, nombre_echecs)

# Lancer le programme principal
if __name__ == '__main__':
    principal()
