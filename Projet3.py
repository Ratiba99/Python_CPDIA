import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration du fichier de log pour enregistrer les événements
logging.basicConfig(filename='file_modification.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Liste des événements pour la visualisation
events = []

class FileModificationHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Ne surveiller que le fichier logs_web.csv
        if event.src_path == "C:/Users/Hp/Documents/logs_web.csv":  # Chemin du fichier à surveiller
            logging.info(f"Modification détectée: {event.src_path}")
            events.append(datetime.now())

# Spécifier le chemin du fichier à surveiller
file_to_watch = "C:/Users/Hp/Documents/logs_web.csv"  # Chemin du fichier à surveiller

# Créer l'observateur et démarrer la surveillance du fichier
event_handler = FileModificationHandler()
observer = Observer()
observer.schedule(event_handler, path="C:/Users/Hp/Documents", recursive=False)  # chemin du dossier 
observer.start()

print("Surveillance en cours... Appuyez sur Ctrl+C pour arrêter.")

# Attendre indéfiniment pour détecter les événements
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# Affichage d'un graphique simple après avoir arrêté la surveillance
if events:
    # Extraire les heures des événements
    event_times = [event.strftime('%H:%M:%S') for event in events]
    plt.hist(event_times, bins=30, edgecolor='black')
    plt.title('Fréquence des modifications de logs_web.csv')
    plt.xlabel('Heure')
    plt.ylabel('Nombre d\'événements')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
