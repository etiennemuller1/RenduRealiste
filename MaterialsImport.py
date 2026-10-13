import bpy
import os

def remove_libraries():
    """
    Supprime toutes les bibliothèques chargées dans Blender.
    """
    bpy.data.batch_remove(bpy.data.libraries)

def remove_materials_with_prefix(prefix):
    """
    Supprime tous les matériaux dont le nom commence par le préfixe spécifié.
    
    Args:
    - prefix (str): Préfixe du nom des matériaux à supprimer.
    """
    # Liste des matériaux à supprimer
    materials_to_remove = [material for material in bpy.data.materials if material.name.startswith(prefix)]
    
    # Suppression des matériaux de la liste
    for material in materials_to_remove:
        bpy.data.materials.remove(material)

def link_blend_file_materials(blend_file_path, link=False):
    """
    Charge les matériaux à partir d'un fichier .blend et les ajoute à la scène Blender.
    Les matériaux sont renommés en fonction du nom du fichier .blend et d'un compteur d'importation.

    Args:
    - blend_file_path (str): Chemin vers le fichier .blend contenant les matériaux.
    - link (bool): Indique si les matériaux doivent être liés (True) ou copiés (False).
    """
    import_count = 1
    
    with bpy.data.libraries.load(blend_file_path, link=link) as (data_from, data_to):
        for material in data_from.materials:
            data_to.materials.append(material)
    
    with bpy.data.libraries.load(blend_file_path, link=link) as (data_from, data_to):
        for material in data_from.materials:
            # Renommage du matériau importé
            new_material_name = f"Material_Realist_{os.path.basename(blend_file_path).replace('.blend', '_')}{import_count:03d}"
            bpy.data.materials[material].name = new_material_name
            import_count += 1

def extract_material_name(object_name):
    """
    Extrait le nom du matériau à partir du nom de l'objet Blender.
    
    Args:
    - object_name (str): Nom de l'objet Blender.

    Returns:
    - str: Nom du matériau extrait, ou None si aucun matériau correspondant n'est trouvé.
    """
    if object_name.startswith("Label_"):
        parts = object_name.split('_')
        return parts[2]
    else:
        return None

def extract_materials_names():
    """
    Extrait tous les noms de matériaux des objets de la scène Blender.
    
    Returns:
    - list: Liste des noms de matériaux uniques extraits des objets de type 'MESH'.
    """
    material_names = []
    
    for obj in bpy.context.scene.objects:
        if obj.type == 'MESH':
            material_name = extract_material_name(obj.name)
            if material_name and material_name not in material_names:
                material_names.append(material_name)
                
    return material_names

def main_function(blend_folder_path):
    """
    Fonction principale pour gérer l'importation des matériaux à partir des fichiers .blend dans un dossier spécifié.
    Elle supprime d'abord tous les matériaux existants avec le préfixe "Material_Realist_", puis importe les nouveaux matériaux
    pour chaque nom de matériau extrait des objets de la scène.
    
    Args:
    - blend_folder_path (str): Chemin du dossier contenant les fichiers .blend des matériaux.
    """
    remove_libraries()
    remove_materials_with_prefix("Material_Realist_")
    
    material_names = extract_materials_names()
    
    # Importation des matériaux pour chaque nom de matériau extrait
    for material_name in material_names:
        blend_file_path = os.path.join(blend_folder_path, f"{material_name}.blend")
        link_blend_file_materials(blend_file_path)

# Exécution de la fonction principale avec le chemin du dossier contenant les fichiers .blend des matériaux
main_function(r"C:\Users\etien\Documents\ProjetRenduRealiste\Materiaux")
