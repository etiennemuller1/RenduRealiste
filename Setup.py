import bpy
import os

# Sauvegarde du chemin du fichier .blend actif
def save_initial_blend_file():
    initial_blend_file = bpy.data.filepath
    return initial_blend_file

# Restauration du fichier .blend initial
def restore_initial_blend_file(initial_blend_file):
    bpy.ops.wm.open_mainfile(filepath=initial_blend_file)

# Sauvegarde de l'état initial de la scène
def save_initial_state():
    initial_state = {}
    
    # Sauvegarde des objets sélectionnés
    initial_state['selected_objects'] = [obj.name for obj in bpy.context.selected_objects]
    
    # Ajoutez d'autres propriétés à sauvegarder si nécessaire
    
    return initial_state

# Restauration de l'état initial de la scène
def restore_initial_state(initial_state):
    # Désélectionne tous les objets
    bpy.ops.object.select_all(action='DESELECT')
    
    # Restaure les objets sélectionnés
    for obj_name in initial_state.get('selected_objects', []):
        obj = bpy.data.objects.get(obj_name)
        if obj:
            obj.select_set(True)
    
    # Réinitialise d'autres paramètres selon les besoins

# Fonction principale pour traiter chaque modèle CAO
def main_function(modele_cao_folder, output_folder_meshes, materiel_folder, scenes_folder):
    # Sauvegarder le chemin du fichier .blend initial
    initial_blend_file = save_initial_blend_file()
    
    # Sauvegarder l'état initial avant de commencer le traitement
    initial_state = save_initial_state()
    
    # Liste tous les fichiers dans le dossier modele_cao_folder
    model_files = os.listdir(modele_cao_folder)
    
    for model_file in model_files:
        if model_file.endswith(".FCStd"):
            # Chemin complet vers le fichier modèle
            model_file_path = os.path.join(modele_cao_folder, model_file)
            
            # Extraction du maillage depuis le modèle CAO
            extraction_de_maillage_script = bpy.data.texts.get("ExtractionDeMaillage")
            output_folder_mesh = extraction_de_maillage_script.as_module().main_function(model_file_path, output_folder_meshes)
            
            # Importer l'objet extrait
            object_import_script = bpy.data.texts.get("ObjectImport")
            object_import_script.as_module().main_function(output_folder_mesh)
            
            # Appliquer l'échelle correcte à l'objet importé
            scale_object_script = bpy.data.texts.get("ScaleObject")
            scale_object_script.as_module().main_function()
            
            # Appliquer le lissage de surface (Shade Smooth)
            shade_smooth_script = bpy.data.texts.get("ShadeSmooth")
            shade_smooth_script.as_module().main_function()
            
            # Générer la scène
            scene_generator_script = bpy.data.texts.get("SceneGenerator")
            scene_generator_script.as_module().main_function()
            
            # Orienter la caméra vers le barycentre de l'objet
            camera_look_at_barycentre_script = bpy.data.texts.get("CameraLookAtBarycentre")
            camera_look_at_barycentre_script.as_module().main_function()
            
            # Importer les matériaux depuis le dossier spécifié
            materials_import_script = bpy.data.texts.get("MaterialsImport")
            materials_import_script.as_module().main_function(materiel_folder)
            
            # Générer les étiquettes de couleur pour tous les objets
            generate_all_color_label_script = bpy.data.texts.get("GenerateAllColorLabel")
            generate_all_color_label_script.as_module().main_function()
            
            # Sauvegarder la scène en tant que fichier .blend
            scene_name = os.path.splitext(model_file)[0]  # Nom du modèle sans extension
            blend_file_path = os.path.join(scenes_folder, scene_name + ".blend")
            bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)
            
            # Restaurer l'état initial pour la prochaine itération
            restore_initial_state(initial_state)
            bpy.context.view_layer.update()

    # Recharger le fichier .blend initial
    restore_initial_blend_file(initial_blend_file)

# Définir les chemins des dossiers
modele_cao_folder = r"C:\Users\etien\Documents\ProjetRenduRealiste\ModèlesCAO"
output_folder_meshes = r"C:\Users\etien\Documents\ProjetRenduRealiste\Maillages"
materiel_folder = r"C:\Users\etien\Documents\ProjetRenduRealiste\Materiaux"
scenes_folder = r"C:\Users\etien\Documents\ProjetRenduRealiste\Scènes"

# Appeler la fonction principale pour chaque modèle CAO dans le dossier spécifié
main_function(modele_cao_folder, output_folder_meshes, materiel_folder, scenes_folder)
