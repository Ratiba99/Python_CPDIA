import os
import shutil
import logging

# Demander à l'utilisateur de spécifier le répertoire source
source_directory = input("Veuillez spécifier le répertoire source : ")

# Vérifier si le répertoire source existe
if not os.path.exists(source_directory):
    print(f"Le répertoire source {source_directory} n'existe pas.")
    
else :
    #Créer le fichier log
    logging.basicConfig(filename='fichier_classification.log', level=logging.INFO, 
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    def classify_files_by_extension(source_directory):
        # Scanner le répertoire source
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                # Obtenir l'extension du fichier
                file_extension = os.path.splitext(file)[1][1:]
                
                # Créer un sous-dossier pour l'extension de fichier si nécessaire
                subdirectory = os.path.join(source_directory, file_extension)
                if not os.path.exists(subdirectory):
                    os.makedirs(subdirectory)
                    logging.info(f"Création du répertoire : {subdirectory}")
                
                # Déplacer le fichier dans le sous-dossier
                source_file = os.path.join(root, file)
                destination_file = os.path.join(subdirectory, file)
                try:
                    shutil.move(source_file, destination_file)
                    logging.info(f"Fichier déplacé : {source_file} vers {destination_file}")
                except Exception as e:
                    logging.error(f"Erreur lors du déplacement du fichier : {source_file} vers {destination_file}. Erreur : {e}")

    # Classer les fichiers par leur extension
    classify_files_by_extension(source_directory)

    # Message indiquant que le processus est terminé
    print("Classification des fichiers terminée. Consultez le fichier de log pour plus de détails.")
