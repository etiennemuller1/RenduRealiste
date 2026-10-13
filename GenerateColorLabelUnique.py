import bpy
import colorsys

def delete_materials_with_prefix(prefix):
    """
    Supprime tous les matériaux dont le nom commence par le préfixe spécifié.

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
    Génère une couleur unique en fonction de l'index et du nombre total.

    Args:
    - label_number (int): Numéro de label utilisé pour générer la couleur.
    - total (int): Nombre total d'objets "Label_" pour normaliser l'index.

    Returns:
    - tuple: Tuple RGBA représentant la couleur générée.
    """
    # Calculer la teinte en fonction de l'index et du nombre total
    hue = (label_number / total) % 1.0  # Assure que la teinte reste dans l'intervalle [0, 1]
    
    # Utiliser une saturation et une valeur élevées pour des couleurs vives
    saturation = 1.0
    value = 1.0
    
    # Convertir de HSV à RGB
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    
    return (r, g, b, 1.0)  # RGBA

def generate_label_materials():
    """
    Génère et attribue des matériaux uniques à tous les objets dont le nom commence par "Label_".
    """
    i = 0
    # Parcourir tous les objets dans la scène
    for obj in bpy.data.objects:
        # Vérifier si le nom de l'objet commence par "Label_"
        if obj.name.startswith("Label_"):
            # Extraire le numéro de label de l'objet
            label_number = i
            i += 1
            
            # Construire le nom du matériau
            material_name = f"Material_Label_Unique_{label_number}"
            
            # Vérifier si un matériau avec ce nom existe déjà
            existing_material = bpy.data.materials.get(material_name)
            
            if not existing_material:
                # Générer une nouvelle couleur distincte à partir du numéro de label
                new_color = generate_color_from_index(label_number, len([obj for obj in bpy.data.objects if obj.name.startswith("Label_")]))
                
                # Créer un nouveau matériau avec la couleur générée
                new_material = bpy.data.materials.new(name=material_name)
                new_material.diffuse_color = new_color

# Appeler la fonction pour supprimer les anciens matériaux avec le préfixe spécifié
delete_materials_with_prefix("Material_Label_Unique_")

# Appeler la fonction pour générer et attribuer les nouveaux matériaux
generate_label_materials()
