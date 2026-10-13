import bpy

def assign_group_materials_to_objects():
    """
    Assigne les matériaux dont le nom commence par "Material_Label_Group_" aux objets dont le nom
    contient le type récupéré à partir du nom du matériau.
    """
    # Parcourir tous les matériaux dans la scène
    for material in bpy.data.materials:
        # Vérifier si le nom du matériau commence par "Material_Label_Group_"
        if material.name.startswith("Material_Label_Group_"):
            # Diviser le nom du matériau en parties en utilisant "_"
            parts = material.name.split("_")
            # Récupérer le type à partir de la dernière partie
            type_value = parts[-1]
            
            print("Matériau trouvé :", material.name)
            print("Type récupéré :", type_value)
            
            # Parcourir tous les objets dans la scène
            for obj in bpy.data.objects:
                # Vérifier si le nom de l'objet contient le type récupéré
                if type_value in obj.name:
                    print("Objet trouvé :", obj.name)
                    
                    # Supprimer tous les autres matériaux de l'objet
                    obj.data.materials.clear()
                    
                    # Appliquer le matériau à l'objet
                    obj.data.materials.append(material)

# Appeler la fonction pour assigner les matériaux aux objets appropriés
assign_group_materials_to_objects()
