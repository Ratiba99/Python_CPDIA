import ssl
import socket
import matplotlib.pyplot as plt
from datetime import datetime

# Fonction pour obtenir les informations SSL du certificat d'un site web
def verifier_certificat_ssl(hote):
    try:
        # Connexion au site via SSL
        contexte = ssl.create_default_context()
        connexion = contexte.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hote)
        connexion.connect((hote, 443))  # Port 443 pour HTTPS

        # Extraire les informations du certificat SSL
        certificat = connexion.getpeercert()
        connexion.close()

        # Extraire la date d'expiration du certificat
        date_expiration = certificat['notAfter']
        date_expiration = datetime.strptime(date_expiration, "%b %d %H:%M:%S %Y GMT")

        return date_expiration

    except Exception as e:
        print(f"Erreur lors de la vérification du certificat pour {hote}: {e}")
        return None

# Fonction pour générer un graphique des certificats valides et expirés
def visualiser_certificats(certificats):
    # Calculer les certificats expirés et valides
    valides = sum(1 for exp in certificats if exp and exp > datetime.now())
    expires = len(certificats) - valides

    # Créer le graphique
    labels = ['Certificats Valides', 'Certificats Expirés']
    values = [valides, expires]

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['green', 'red'], startangle=90)
    plt.title("Répartition des Certificats SSL: Valides vs Expirés")
    plt.show()

# Liste des sites web à vérifier
sites_web = ['google.com', 'example.com', 'yahoo.com']

# Vérifier les certificats SSL pour les sites dans la liste
certificats_expiration = []

for site in sites_web:
    date_expiration = verifier_certificat_ssl(site)
    if date_expiration:
        certificats_expiration.append(date_expiration)
        print(f"Le certificat SSL de {site} expire le {date_expiration}")
    else:
        certificats_expiration.append(None)

# Visualiser les certificats valides et expirés
visualiser_certificats(certificats_expiration)
