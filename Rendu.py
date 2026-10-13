import bpy
import math
import os

def main_function(num_heights, frames_per_rotation, radius, render_output_path, hdrFolder):
    """
    Fonction principale pour orchestrer le processus de rendu réaliste avec différents paramètres.

    Args:
    - num_heights (int): Nombre de hauteurs à parcourir.
    - frames_per_rotation (int): Nombre de frames par rotation.
    - radius (float): Rayon pour le positionnement de la caméra.
    - render_output_path (str): Chemin de sortie pour les images rendues.
    - hdrFolder (str): Chemin du dossier contenant les images HDR.

    Cette fonction coordonne les étapes suivantes :
    1. Création des répertoires de sortie pour les images et les masques.
    2. Appel aux scripts externes pour le positionnement de la caméra, le rendu des labels et le rendu réaliste.
    3. Boucle principale pour générer les images rendues en fonction des hauteurs et des rotations spécifiées.
    """

    bpy.context.view_layer.update()

    # Création des répertoires de sortie pour les images et les masques
    render_output_path_images = os.path.join(render_output_path, "images")
    render_output_path_masks = os.path.join(render_output_path, "masks")

    os.makedirs(render_output_path_images, exist_ok=True)
    os.makedirs(render_output_path_masks, exist_ok=True)

    # Création des sous-répertoires pour les masques
    render_output_path_masks_identique = os.path.join(render_output_path_masks, "_label_identique")
    render_output_path_masks_groupe = os.path.join(render_output_path_masks, "_label_groupe")
    render_output_path_masks_unique = os.path.join(render_output_path_masks, "_label_unique")

    os.makedirs(render_output_path_masks_identique, exist_ok=True)
    os.makedirs(render_output_path_masks_groupe, exist_ok=True)
    os.makedirs(render_output_path_masks_unique, exist_ok=True)

    # Liste des chemins de sortie pour les masques et les images
    list_render_output_masks = [
        render_output_path_masks_identique,
        render_output_path_masks_groupe,
        render_output_path_masks_unique
    ]



    # Déterminer le nombre de l'image de départ
    startimagenumber = 0
    starti = startimagenumber // frames_per_rotation
    startj = startimagenumber % frames_per_rotation

    # Charger les scripts externes nécessaires
    CameraPlacement = bpy.data.texts.get("CameraPlacement")
    RenduLabel = bpy.data.texts.get("RenduLabel")
    RenderRealist = bpy.data.texts.get("RenderRealist")

    # Boucle principale pour le rendu en fonction des hauteurs et rotations
    for i in range(starti, num_heights):
        for j in range(frames_per_rotation):
            renderNumber = frames_per_rotation * i + j

            # Positionnement de la caméra pour cette configuration
            CameraPlacement.as_module().main_function(i, num_heights, j, frames_per_rotation, radius)

            # Rendu des labels pour générer les masques
            RenduLabel.as_module().main_function(renderNumber, list_render_output_masks)

        for j in range(frames_per_rotation):
            renderNumber = frames_per_rotation * i + j

            # Positionnement de la caméra pour cette configuration
            CameraPlacement.as_module().main_function(i, num_heights, j, frames_per_rotation, radius)

            # Rendu réaliste pour générer les images finales
            RenderRealist.as_module().main_function(renderNumber, hdrFolder,render_output_path_images)

# Exemple d'utilisation :
# num_heights = 1
# frames_per_rotation = 1
# radius = 2
# modeleCAOFolder = r"C:\Users\etien\Documents\ProjetRenduRealiste\ModèlesCAO\hydro.FCStd"
# render_output_path = r"C:\Users\etien\Documents\ProjetRenduRealiste\Rendu"
# hdrFolder = r"C:\Users\etien\Documents\ProjetRenduRealiste\hdri"
# main_function(num_heights, frames_per_rotation, radius, render_output_path, hdrFolder)