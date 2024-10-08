import bpy
import os

def main_function(renderNumber, list_render_output_masks):
    """
    Fonction principale pour générer les masques de couleur des labels.

    Args:
    - renderNumber (int): Numéro d'image à générer.
    - list_render_output_masks (list): Liste des chemins de sortie pour les masques.

    Cette fonction charge différents scripts Blender pour générer trois types de masques de couleur de labels :
    1. Masques identiques
    2. Masques de groupe
    3. Masques uniques
    Elle rend chaque type de masque séparément en définissant le chemin de sortie et en déclenchant le rendu.
    """

    # Charger le script pour les paramètres de rendu des couleurs des labels
    RenderColorLabelParameter = bpy.data.texts.get("RenderColorLabelParameter")
    RenderColorLabelParameter.as_module()

    # Charger et exécuter le script pour appliquer les couleurs aux labels de groupe
    ApplyColorLabelGroup = bpy.data.texts.get("ApplyColorLabelGroup")
    ApplyColorLabelGroup.as_module()
    group_path = os.path.join(list_render_output_masks[1], f"{renderNumber}.png")  # Chemin pour les masques de groupe
    bpy.context.scene.render.filepath = group_path  # Définir le chemin de sortie pour le rendu
    bpy.ops.render.render(write_still=True)  # Effectuer le rendu de l'image

    # Chargement et exécution des scripts pour les autres types de masques (identiques et uniques)
    # Ces parties de code sont mises en commentaire car elles ne sont pas utilisées actuellement.
    # Elles pourraient être décommentées et adaptées si nécessaire pour d'autres fonctionnalités.

    """
    # Charger et exécuter le script pour appliquer les couleurs aux labels identiques
    ApplyColorLabel = bpy.data.texts.get("ApplyColorLabel")
    ApplyColorLabel.as_module()
    identique_path = os.path.join(list_render_output_masks[0], f"{renderNumber}.png")  # Chemin pour les masques identiques
    bpy.context.scene.render.filepath = identique_path  # Définir le chemin de sortie pour le rendu
    bpy.ops.render.render(write_still=True)  # Effectuer le rendu de l'image

    # Charger et exécuter le script pour appliquer les couleurs aux labels uniques
    ApplyColorLabelUnique = bpy.data.texts.get("ApplyColorLabelUnique")
    ApplyColorLabelUnique.as_module()
    unique_path = os.path.join(list_render_output_masks[2], f"{renderNumber}.png")  # Chemin pour les masques uniques
    bpy.context.scene.render.filepath = unique_path  # Définir le chemin de sortie pour le rendu
    bpy.ops.render.render(write_still=True)  # Effectuer le rendu de l'image
    """
