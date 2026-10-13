import bpy
import random

def main_function():
    """
    Assigne un matériau aléatoire à chaque groupe d'objets dont le nom commence par "Label_" et ont le même numéro.
    Le matériau est choisi parmi les matériaux qui possèdent le même label.
    """
    # Dictionnaire pour stocker la liste des matériaux par label
    materials_by_label = {}
    # Dictionnaire pour stocker le matériau assigné à chaque numéro de label
    assigned_materials = {}

    # Parcourir tous les matériaux pour les regrouper par label
    for material in bpy.data.materials:
        if material.name.startswith("Material_Realist_"):
            try:
                parts = material.name.split("_")
                if len(parts) < 3:
                    continue
                nom_materiau = parts[2]

                if nom_materiau not in materials_by_label:
                    materials_by_label[nom_materiau] = []
                materials_by_label[nom_materiau].append(material)
            except IndexError:
                continue

    # Parcourir tous les objets de la scène
    for obj in bpy.data.objects:
        # Vérifier si le nom de l'objet commence par "Label_"
        if obj.name.startswith("Label_"):
            try:
                # Extraire les parties pertinentes du nom de l'objet
                parts = obj.name.split("_")
                if len(parts) < 3:
                    raise IndexError

                label_number = parts[1]
                nom_materiau = parts[2]

                # Si ce numéro de label n'a pas encore de matériau assigné, en sélectionner un aléatoirement
                if label_number not in assigned_materials:
                    # Vérifier si des matériaux correspondant à ce label existent
                    if nom_materiau in materials_by_label:
                        material_list = materials_by_label[nom_materiau]
                        # Sélectionner un matériau aléatoirement dans la liste
                        assigned_materials[label_number] = random.choice(material_list)
                    else:
                        print(f"Aucun matériau trouvé pour le label '{nom_materiau}' pour l'objet '{obj.name}'.")
                        continue

                # Récupérer le matériau assigné pour ce numéro de label
                material = assigned_materials[label_number]

                # Assigner le matériau à l'objet
                if obj.data.materials:
                    # Si l'objet a déjà un matériau, le remplacer
                    obj.data.materials[0] = material
                else:
                    # Sinon, ajouter le matériau à l'objet
                    obj.data.materials.append(material)

            except IndexError:
                print(f"L'objet {obj.name} n'a pas le format attendu 'Label_xxx_yyy'.")
            except Exception as e:
                print(f"Erreur lors de l'assignation du matériau pour l'objet '{obj.name}': {e}")

# Appeler la fonction principale
main_function()
