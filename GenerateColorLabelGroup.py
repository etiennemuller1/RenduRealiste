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

def generate_material_color(index, total_colors):
    """
    Génère une couleur en fonction de l'index et du nombre total de couleurs.

    Args:
    - index (int): Index de la couleur à générer.
    - total_colors (int): Nombre total de couleurs à générer.

    Returns:
    - tuple: Tuple RGBA représentant la couleur générée.
    """
    # Calculer la teinte en fonction de l'index et du nombre total de couleurs
    hue = (index / total_colors) % 1.0
    
    # Utiliser une saturation et une valeur élevées pour des couleurs vives
    saturation = 1.0
    value = 1.0
    
    # Convertir de HSV à RGB
    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
    
    return (r, g, b, 1.0)  # RGBA

def create_material_for_object_type(object_type, index, total_colors):
    """
    Crée un nouveau matériau pour un type d'objet spécifié avec une couleur générée.

    Args:
    - object_type (str): Type d'objet pour lequel créer le matériau.
    - index (int): Index utilisé pour générer la couleur du matériau.
    - total_colors (int): Nombre total de couleurs à générer.

    Returns:
    - bpy.types.Material: Le nouveau matériau créé.
    """
    # Générer une couleur pour le type d'objet donné
    color = generate_material_color(index, total_colors)
    
    # Créer un nouveau matériau
    new_material = bpy.data.materials.new(name=f"Material_Label_Group_{object_type}")
    new_material.diffuse_color = color
    
    return new_material

def generate_materials():
    """
    Génère une liste de matériaux pour différents types d'objets spécifiés par des mots-clés.

    Returns:
    - list: Liste des matériaux générés.
    """
    generated_materials = []
    # Types d'objets à traiter avec des matériaux
    keywords = ["nut", "narrow", "bolt", "default", "table"]
    
    # Générer les matériaux pour chaque type d'objet
    for i, keyword in enumerate(keywords):
        material = create_material_for_object_type(keyword, i, len(keywords))
        generated_materials.append(material)
    
    return generated_materials

# Appeler la fonction pour supprimer les anciens matériaux et générer les nouveaux
delete_materials_with_prefix("Material_Label_Group_")
generated_materials = generate_materials()
