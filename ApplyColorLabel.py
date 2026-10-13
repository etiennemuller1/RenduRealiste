import bpy

def assign_existing_materials_to_label_objects():
    """
    Assigne les matériaux existants aux objets dont le nom commence par "Label_".
    Le nom du matériau est construit à partir du numéro de label de l'objet.
    """
    for obj in bpy.data.objects:
        # Vérifier si le nom de l'objet commence par "Label_"
        if obj.name.startswith("Label_"):
            try:
                # Extraire le numéro de label de l'objet
                label_number = int(obj.name.split("_")[1])
                
                # Construire le nom du matériau
                material_name = f"Material_Label_Unique_{label_number}"
                
                # Vérifier si un matériau avec ce nom existe déjà
                existing_material = bpy.data.materials.get(material_name)
                
                if existing_material:
                    # Si un matériau existe déjà, assigner ce matériau à l'objet
                    obj.data.materials.clear()  # Supprimer tous les autres matériaux de l'objet
                    obj.data.materials.append(existing_material)
            except (IndexError, ValueError):
                # Gérer les cas où le nom ne contient pas de numéro valide
                print(f"Objet {obj.name} n'a pas un numéro de label valide.")

# Appeler la fonction pour assigner les matériaux existants aux objets "Label_"
assign_existing_materials_to_label_objects()
s