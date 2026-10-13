import bpy
import colorsys

def delete_materials_with_prefix(prefix):
    """
    Supprime tous les matériaux dont le nom commence par le préfixe donné.

    Args:
    - prefix (str): Préfixe des noms des matériaux à supprimer.
    """
    # Parcourir tous les matériaux dans la scène
    for material in bpy.data.materials:
        # Vérifier si le nom du matériau commence par le préfixe donné
        if material.name.startswith(prefix):
            # Supprimer le matériau
            bpy.data.materials.remove(material)
            
def generate_color_from_index(label_number, total):
    """
    Génère une couleur unique en fonction de l'indice du label.

    Args:
    - label_number (int): Numéro du label.
    - total (int): Nombre total de labels.

    Returns:
    - tuple: Tuple RGBA représentant la couleur générée.
    """
    # Calculer la teinte en fonction de l'indice i
    hue = (label_number / total) % 1.0  # Assure que la teinte reste dans l'intervalle [0, 1]
    
    # Utiliser une saturation et une valeur plus élevées pour des couleurs plus saturées
    saturation = 1.0
    value = 1.0
    
    # Convertir de HSV à RGB
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    
    return (r, g, b, 1.0)  # RGBA

def generate_label_materials():
    """
    Génère et assigne des matériaux uniques à tous les objets dont le nom commence par "Label_".
    Les matériaux sont basés sur un système de couleurs distinctes en fonction des indices des labels.
    """
    # Parcourir tous les objets dans la scène
    for obj in bpy.data.objects:
        # Vérifier si le nom de l'objet commence par "Label_"
        if obj.name.startswith("Label_"):
            # Extraire le numéro de label de l'objet
            label_number = int(obj.name.split("_")[1])
            
            # Construire le nom du matériau
            material_name = f"Material_Label_Identique_{label_number}"
            
            # Vérifier si un matériau avec ce nom existe déjà
            existing_material = bpy.data.materials.get(material_name)
            
            if not existing_material:
                # Générer une nouvelle couleur distincte à partir du numéro de label
                new_color = generate_color_from_index(label_number, len([obj for obj in bpy.data.objects if obj.name.startswith("Label_")]))
                
                # Créer un nouveau matériau avec la couleur générée
                new_material = bpy.data.materials.new(name=material_name)
                new_material.diffuse_color = new_color

# Appel de la fonction pour supprimer les anciens matériaux et générer les nouveaux
delete_materials_with_prefix("Material_Label_Identique_")
generate_label_materials()
