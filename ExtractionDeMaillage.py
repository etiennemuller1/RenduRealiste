import subprocess
import os

def main_function(documentName, outputFolder):
    """
    Fonction principale pour exécuter un script Python externe avec des paramètres spécifiés.

    Args:
    documentName (str): Chemin complet du document FCStd à traiter.
    outputFolder (str): Chemin du dossier où les résultats de l'extraction seront sauvegardés.

    Returns:
    str: Chemin du dossier où les maillages ont été enregistrés.
    """
    # Chemin vers l'interpréteur Python spécifique
    chemin_interpreteur = r"C:\Users\etien\miniconda3\envs\fcenv\python.exe"

    # Chemin vers le script Python externe pour l'extraction de maillage
    chemin_script_extraction = r"C:\Users\etien\Documents\ProjetRenduRealiste\ExtractionDeMaillage\main.py"

    # Extraire le nom du document FCStd sans l'extension
    nom_document = os.path.splitext(os.path.basename(documentName))[0]

    # Créer un sous-dossier pour les maillages spécifique au document
    outputFolderDocument = os.path.join(outputFolder, nom_document)
    os.makedirs(outputFolderDocument, exist_ok=True)
    
    # Appel du script externe avec l'interpréteur Python et les arguments nécessaires
    subprocess.call([chemin_interpreteur, chemin_script_extraction, documentName, outputFolderDocument])
    
    return outputFolderDocument