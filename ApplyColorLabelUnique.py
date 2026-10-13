import bpy

def assign_existing_materials_to_label_objects():
    """
    Assigne des matériaux existants aux objets dont le nom commence par "Label_".
    Les matériaux sont nommés de manière séquentielle : "Material_Label_Unique_{label_number}".
    """
    i = 1  # Initialise le compteur pour les labels

    # Parcourir tous les objets dans la scène
    for obj in bpy.data.objects:
        # Vérifier si le nom de l'objet commence par "Label_"
        if obj.name.startswith("Label_"):
            # Utiliser le compteur comme numéro de label
            label_number = i
            i += 1  # Incrémenter le compteur pour le prochain label

            # Construire le nom du matériau
            material_name = f"Material_Label_Unique_{label_number}"
            
            # Vérifier si un matériau avec ce nom existe déjà
            existing_material = bpy.data.materials.get(material_name)
            
            if existing_material:
                # Si un matériau existe déjà, l'assigner à l'objet
                obj.data.materials.clear()  # Supprimer tous les autres matériaux de l'objet
                obj.data.materials.append(existing_material)

# Appeler la fonction pour assigner les matériaux existants aux objets "Label_"
assign_existing_materials_to_label_objects()
