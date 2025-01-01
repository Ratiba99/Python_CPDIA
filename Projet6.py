import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fonction pour charger les logs de sécurité
def charger_logs(fichier):
    # Charger le fichier CSV avec les logs
    try:
        logs = pd.read_csv(fichier)
        print(f"Logs chargés depuis {fichier}")
        return logs
    except FileNotFoundError:
        print("Le fichier spécifié n'a pas été trouvé.")
        return None

# Fonction pour rechercher les tentatives de connexion échouées
def rechercher_connexions_echouees(logs):
    # Supposons que les logs contiennent une colonne 'EventID' et 'Message'
    # Les tentatives de connexion échouées peuvent être identifiées par un EventID spécifique (par exemple, 529 pour un échec d'authentification)
    
    # Rechercher les événements liés aux tentatives de connexion échouées
    connexions_echouees = logs[logs['EventID'] == 529]
    print(f"{len(connexions_echouees)} tentatives de connexion échouées détectées.")
    
    return connexions_echouees

# Fonction pour visualiser les types d'événements et leur fréquence
def visualiser_frequence_evenements(logs):
    # Compter la fréquence des types d'événements (par exemple, EventID)
    evenement_frequence = logs['EventID'].value_counts()

    # Visualisation avec un graphique
    plt.figure(figsize=(10, 6))
    sns.barplot(x=evenement_frequence.index, y=evenement_frequence.values, palette='viridis')
    plt.title("Fréquence des types d'événements")
    plt.xlabel("EventID")
    plt.ylabel("Fréquence")
    plt.xticks(rotation=90)
    plt.show()

# Fonction pour générer un rapport des activités suspectes
def generer_rapport(connexions_echouees, fichier_rapport="rapport_suspect.csv"):
    # Enregistrer les tentatives de connexion échouées dans un fichier CSV
    connexions_echouees.to_csv(fichier_rapport, index=False)
    print(f"Le rapport des activités suspectes a été généré : {fichier_rapport}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger les logs depuis un fichier CSV
    fichier_logs = 'C:/Users/Hp/Documents/Logs.csv'  # Mettez le chemin de votre fichier de logs
    logs = charger_logs(fichier_logs)

    if logs is not None:
        # Rechercher les tentatives de connexion échouées
        connexions_echouees = rechercher_connexions_echouees(logs)

        # Visualiser les types d'événements et leur fréquence
        visualiser_frequence_evenements(logs)

        # Générer un rapport des activités suspectes
        generer_rapport(connexions_echouees)
