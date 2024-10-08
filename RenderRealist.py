import bpy
import os
import random

def main_function(renderNumber, hdrFolder, render_output_path_images):
    """
    Fonction principale pour gérer le rendu réaliste avec différents paramètres d'environnement HDR.

    Args:
    - renderNumber (int): Numéro de rendu.
    - hdrFolder (str): Chemin du dossier contenant les images HDR.

    Cette fonction exécute plusieurs étapes de rendu :
    1. Applique les matériaux réalistes.
    2. Gère l'environnement HDR.
    3. Effectue le rendu de la scène.

    Chaque étape utilise des scripts externes chargés dans bpy.data.texts.
    """
    
    # Charger le script de configuration des paramètres de rendu réaliste
    RenderRealisteParameter = bpy.data.texts.get("RenderRealisteParameter")
    RenderRealisteParameter.as_module()
    
    # Charger et exécuter le script d'application des matériaux réalistes
    ApplyMaterialRealist = bpy.data.texts.get("ApplyMaterialRealist")
    ApplyMaterialRealist.as_module().main_function()
    
    # Charger et exécuter le script de gestion de l'environnement HDR
    EnvironnementManager = bpy.data.texts.get("EnvironnementManager")
    
    # Lister les fichiers HDR dans le dossier spécifié
    hdr_files = [f for f in os.listdir(hdrFolder) if f.endswith(".hdr")]
    
    # Vérifier le nombre de fichiers HDR trouvés
    num_hdr_files = len(hdr_files)
    print(f"Il y a {num_hdr_files} fichiers HDR dans le dossier.")
    
    if not hdr_files:
        raise FileNotFoundError("Aucun fichier HDR trouvé dans le dossier spécifié.")
    
    # Choisir un index aléatoire dans la plage des indices disponibles
    random_index = random.randint(0, num_hdr_files - 1)
    
    # Utiliser random_index pour appeler EnvironnementManager
    EnvironnementManager.as_module().main_function(hdrFolder, random_index)
    
    # Définir le chemin de sortie pour l'image rendue
    filepath = os.path.join(render_output_path_images, f"{renderNumber}.png")
    bpy.context.scene.render.filepath = filepath
    
    # Effectuer le rendu de l'image
    bpy.ops.render.render(write_still=True)

# Exemple d'utilisation :
# render_output_path = r"C:\Users\etien\Documents\ProjetRenduRealiste\Rendu"
# hdrFolder = r"C:\Users\etien\Documents\ProjetRenduRealiste\hdri"
# renderNumber = 0
# main_function(renderNumber, hdrFolder)
