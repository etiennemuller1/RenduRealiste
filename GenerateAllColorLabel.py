import bpy

def main_function():
    """
    Fonction principale pour exécuter des scripts Blender en tant que modules.

    Cette fonction récupère les scripts par leur nom depuis bpy.data.texts et les exécute en tant que modules.
    Assurez-vous que les scripts sont présents dans bpy.data.texts avant d'appeler cette fonction.

    Usage:
    - Assurez-vous que les scripts "GenerateColorLabel", "GenerateColorLabelGroup" et "GenerateColorLabelUnique"
      sont disponibles dans bpy.data.texts avant d'appeler cette fonction.
    """
    
    # Récupération des scripts par leur nom depuis bpy.data.texts
    generate_color_label = bpy.data.texts.get("GenerateColorLabel")
    generate_color_label_group = bpy.data.texts.get("GenerateColorLabelGroup")
    generate_color_label_unique = bpy.data.texts.get("GenerateColorLabelUnique")

    # Vérification que les scripts existent
    
    # Exécution des scripts en tant que module
    generate_color_label.as_module()
    generate_color_label_group.as_module()
    generate_color_label_unique.as_module()

main_function()