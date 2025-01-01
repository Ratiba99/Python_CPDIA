import socket
import matplotlib.pyplot as plt

# Fonction pour scanner les ports
def scanner_ports(ip, ports):
    ports_ouverts = []
    for port in ports:
        try:
            # Crée une socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Définit un délai d'attente
            # Tente de se connecter au port
            result = s.connect_ex((ip, port))
            if result == 0:
                ports_ouverts.append(port)  # Port ouvert
            s.close()
        except Exception as e:
            print(f"Erreur pour le port {port}: {e}")
    return ports_ouverts

# Adresse IP cible et liste de ports à tester
ip_cible = input("Entrez l'adresse IP cible : ")
ports_a_tester = list(range(1, 1025))  # Tester les ports de 1 à 1024

print(f"Scan en cours sur {ip_cible}...")
ports_ouverts = scanner_ports(ip_cible, ports_a_tester)

# Résultats
print(f"Ports ouverts sur {ip_cible} : {ports_ouverts}")

# Visualisation des résultats
if ports_ouverts:
    plt.bar(range(len(ports_ouverts)), ports_ouverts, color='blue')
    plt.xlabel('Index des Ports')
    plt.ylabel('Ports Ouverts')
    plt.title(f"Ports ouverts sur {ip_cible}")
    plt.xticks(range(len(ports_ouverts)), ports_ouverts, rotation=90)
    plt.tight_layout()
    plt.show()
else:
    print("Aucun port ouvert détecté.")
