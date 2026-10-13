import bpy 
import os

def importer_hdri(hdri_image_path):
    """
    Importe un fichier HDR dans l'environnement de Blender.

    Args:
    hdri_image_path (str): Chemin du fichier HDR à importer.
    """
    # Configuration de l'environnement
    world = bpy.context.scene.world
    world.use_nodes = True
    nodes = world.node_tree.nodes
    links = world.node_tree.links

    # Supprime tous les nœuds existants dans l'arbre des nodes de l'environnement
    for node in nodes:
        nodes.remove(node)

    # Ajoute les nœuds nécessaires
    node_environment = nodes.new(type='ShaderNodeTexEnvironment')
    node_environment.image = bpy.data.images.load(hdri_image_path)
    node_background = nodes.new(type='ShaderNodeBackground')
    node_background_2 = nodes.new(type='ShaderNodeBackground')
    node_background_2.inputs['Color'].default_value = (0, 0, 0, 1)  # Noir
    node_light_path = nodes.new(type='ShaderNodeLightPath')
    node_mix_shader = nodes.new(type='ShaderNodeMixShader')
    node_output = nodes.new(type='ShaderNodeOutputWorld')
    
    # Positionnement des nœuds pour une meilleure lisibilité (optionnel)
    node_environment.location = (-300, 300)
    node_background.location = (-100, 300)
    node_background_2.location = (-100, 0)
    node_light_path.location = (-300, 0)
    node_mix_shader.location = (100, 100)
    node_output.location = (300, 100)
    
    # Connexions des nœuds
    links.new(node_environment.outputs['Color'], node_background.inputs['Color'])
    links.new(node_background.outputs['Background'], node_mix_shader.inputs[1])
    links.new(node_background_2.outputs['Background'], node_mix_shader.inputs[2])
    links.new(node_light_path.outputs['Is Camera Ray'], node_mix_shader.inputs['Fac'])
    links.new(node_mix_shader.outputs['Shader'], node_output.inputs['Surface'])

def main_function(hdrFolder, file_number):
    """
    Fonction principale pour importer un fichier HDR à partir d'un dossier spécifié.

    Args:
    hdrFolder (str): Chemin du dossier contenant les fichiers HDR.
    file_number (int): Numéro du fichier à importer dans la liste des fichiers HDR trouvés.
    """
    # Liste pour stocker les chemins des fichiers HDR
    hdr_files = []

    # Parcourir tous les fichiers dans le dossier spécifié
    for file in os.listdir(hdrFolder):
        # Vérifier si le fichier est un fichier HDR
        if file.endswith(".hdr"):
            hdr_files.append(os.path.join(hdrFolder, file))
    
    # Vérifier s'il y a des fichiers HDR trouvés
    if hdr_files:
        # Calculer le nombre de fichiers HDR trouvés
        hdr_files_length = len(hdr_files)
    
        # Calculer le numéro de fichier ajusté pour éviter les dépassements
        file_number = file_number % hdr_files_length

        # Récupérer le chemin du fichier HDR à partir de la liste en fonction du numéro fourni
        hdrFile = hdr_files[file_number]

        # Appeler la fonction pour importer le fichier HDR dans Blender
        importer_hdri(hdrFile)
        
    else:
        print("Aucun fichier HDR trouvé dans le dossier spécifié.")

# Exemple d'utilisation
hdrFolder = r"C:\Users\etien\Documents\ProjetRenduRealiste\hdri"
file_number = 1
main_function(hdrFolder, file_number)
