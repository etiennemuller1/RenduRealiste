import bpy

def main_function():
    # Désélectionne tous les objets dans la scène Blender
    bpy.ops.object.select_all(action='DESELECT')

    # Récupère les noms de tous les objets dans la scène
    object_names = [obj.name for obj in bpy.data.objects]

    # Parcourt tous les noms d'objets récupérés
    for object_name in object_names:
        # Vérifie si le nom de l'objet commence par "Label_" et ne commence pas par "Label_000"
        if object_name.startswith("Label_") and not object_name.startswith("Label_000"):
            # Sélectionne l'objet dans la scène
            bpy.data.objects[object_name].select_set(True)
        
    # Applique le lissage par angle sur les objets sélectionnés
    bpy.ops.object.shade_smooth_by_angle() 
    
main_function()
