import bpy
import os

def main_function(folder_path):
    """
    Importe tous les objets d'un dossier spécifié après avoir supprimé tous les objets
    dont le nom commence par "Label_" dans la scène.
    
    :param folder_path: Le chemin du dossier contenant les fichiers OBJ à importer.
    """
    # Supprimer tous les objets dont le nom commence par "Label_"
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.name.startswith("Label_"):
            obj.select_set(True)
    bpy.ops.object.delete()

    # Parcourir tous les fichiers dans le dossier
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".obj"):  # Vérifier si le fichier est un fichier OBJ
            file_path = os.path.join(folder_path, file_name)
            
            # Importer le fichier OBJ
            bpy.ops.wm.obj_import(filepath=file_path)

    print("Importation terminée.")