import bpy
import random
import os

def clear_console():
    """Efface la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_unique_elements():
    """
    Extrait les éléments uniques à partir des noms d'objets qui commencent par "Label".
    Retourne une liste des éléments uniques extraits.
    """
    elements_uniques = {}

    for obj in bpy.data.objects:
        if obj.type == 'MESH' and obj.name.startswith("Label"):
            elements = obj.name.split("_")
            if len(elements) >= 4:
                element_concat = "_".join(elements[2:4])
                elements_uniques[element_concat] = 1

    return list(elements_uniques.keys())

def get_prefix(obj_name):
    """
    Extrait le préfixe "mot1_mot2" à partir du nom de l'objet.
    Retourne le préfixe ou None si le nom ne suit pas le format attendu.
    """
    parts = obj_name.split("_")
    if len(parts) >= 3:
        return "_".join(parts[2:-1])
    else:
        return None

def get_random_material(prefix):
    """
    Récupère aléatoirement un matériau dont le nom commence par le préfixe donné.
    Retourne le matériau trouvé ou None s'il n'y en a pas.
    """
    materials = [mat for mat in bpy.data.materials if mat.name.startswith(prefix)]
    if materials:
        return random.choice(materials)
    else:
        return None

def apply_materials_to_objects(materials_dict):
    """
    Applique les matériaux correspondants aux objets dont le nom se termine par ".obj".
    Utilise le dictionnaire materials_dict pour mapper les préfixes d'objets aux matériaux correspondants.
    """
    for obj in bpy.data.objects:
        if obj.name.endswith(".obj"):
            obj_prefix = get_prefix(obj.name)
            if obj_prefix:
                matching_materials = materials_dict.get(obj_prefix)
                if matching_materials:
                    obj.data.materials.clear()
                    obj.data.materials.append(matching_materials)
                else:
                    print("Aucun matériau trouvé pour l'objet", obj.name)

# Efface la console
clear_console()

# Extraction des éléments uniques
elements_uniques = extract_unique_elements()
print("Éléments uniques:", elements_uniques)

# Dictionnaire pour stocker les matériaux correspondants à chaque élément unique
materials_dict = {}

# Récupération aléatoire des matériaux pour chaque élément unique
for element in elements_uniques:
    materials_dict[element] = get_random_material(element)

print("Matériaux correspondants:", materials_dict)

# Application des matériaux aux objets
apply_materials_to_objects(materials_dict)
