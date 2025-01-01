import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier de logs
def charger_logs(chemin_fichier):
    try:
        logs = pd.read_csv(chemin_fichier)  # Charger le fichier CSV
        print("Logs chargés avec succès.")
        return logs
    except Exception as e:
        print(f"Erreur lors du chargement des logs : {e}")
        return None

# Trouver les IP suspectes
def detecter_ips_suspectes(logs):
    comptes_ips = logs['IP'].value_counts()  # Compter le nombre de requêtes par IP
    ips_suspectes = comptes_ips[comptes_ips > 10]  # Filtrer les IP avec plus de 10 requêtes
    print("IP suspectes détectées :")
    print(ips_suspectes)
    return ips_suspectes

# Visualiser les IP les plus fréquentes
def visualiser_ips_frequentes(logs):
    top_ips = logs['IP'].value_counts().head(5)  # Les 5 IP les plus fréquentes
    top_ips.plot(kind='bar', color='blue')  # Créer un graphique en barres
    plt.title("Top 5 des IP les plus fréquentes")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre de requêtes")
    plt.show()

# Programme principal
if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer le chemin du fichier CSV
    chemin_fichier = input("Entrez le chemin du fichier de logs (format CSV) : ")
    logs = charger_logs(chemin_fichier)

    if logs is not None:  # Si le fichier a été chargé avec succès
        # Détecter les IP suspectes
        ips_suspectes = detecter_ips_suspectes(logs)
        
        # Visualiser les IP les plus fréquentes
        visualiser_ips_frequentes(logs)
