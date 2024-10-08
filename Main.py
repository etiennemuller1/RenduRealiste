import bpy
import os

def creer_dossier_unique(chemin_dossier):
    """
    Crée un dossier avec un nom unique. Si le dossier existe déjà, ajoute un numéro à la fin jusqu'à trouver un nom unique.
    
    Args:
    - chemin_dossier (str): Chemin du dossier à créer.

    Returns:
    - str: Chemin du dossier unique créé.
    """
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)
        return chemin_dossier
    
    count = 1
    while True:
        dossier_unique = f"{chemin_dossier}_{count}"
        if not os.path.exists(dossier_unique):
            os.makedirs(dossier_unique)
            return dossier_unique
        count += 1

# Chemins des dossiers et fichiers
hdr_folder = r"C:\Users\etien\Documents\ProjetRenduRealiste\hdri"
render_output_path = r"C:\Users\etien\Documents\ProjetRenduRealiste\Rendu"

# Paramètres de rendu
num_heights = 1
frames_per_rotation = 1
radius = 4

# Générer les étiquettes de couleur pour tous les objets
generate_all_color_label_script = bpy.data.texts.get("GenerateAllColorLabel")
generate_all_color_label_script.as_module().main_function()

# Récupération du nom de fichier .blend sans extension
blend_file_path = bpy.context.blend_data.filepath
if blend_file_path:
    nom_fichier_blend_sans_extension = os.path.splitext(os.path.basename(blend_file_path))[0]
else:
    nom_fichier_blend_sans_extension = "nom_fichier_non_sauve"

# Création d'un dossier de sortie unique pour ce rendu
chemin_complet_sortie = os.path.join(render_output_path, nom_fichier_blend_sans_extension)
chemin_complet_sortie = creer_dossier_unique(chemin_complet_sortie)

# Chargement du script de rendu et exécution de la fonction principale avec les paramètres définis
rendu_script = bpy.data.texts.get("Rendu")
if rendu_script:
    rendu_script.as_module().main_function(num_heights, frames_per_rotation, radius, chemin_complet_sortie, hdr_folder)
else:
    print("Le script 'Rendu' n'a pas été trouvé dans les textes de Blender.")
