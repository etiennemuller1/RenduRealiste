import bpy
import mathutils


def deplacer_center_vers_position_z():
    """
    Déplace l'objet 'Center_Empty' à la position (0, 0, z) où z est la coordonnée z actuelle de 'Center_Empty'.
    Renvoie les déplacements sur les axes X et Y nécessaires pour aligner l'objet sur (0, 0, z).
    """
    objet_center_empty = bpy.data.objects.get("Center_Empty")
    
    deplacement_x = 0
    deplacement_y = 0
    
    # Vérifier si l'objet "Center_Empty" existe
    if objet_center_empty:
        # Récupérer le z de l'objet "Center_Empty"
        z = objet_center_empty.location.z
        
        # Calculer le déplacement sur les axes X et Y
        deplacement_x -= objet_center_empty.location.x
        deplacement_y -= objet_center_empty.location.y
        
        # Déplacer l'objet "Center_Empty" à la position (0, 0, z)
        objet_center_empty.location.x = 0
        objet_center_empty.location.y = 0
        objet_center_empty.location.z = z
    
    return deplacement_x, deplacement_y


def deplacer_modeles_x_y(collection, x, y):
    """
    Déplace les objets de la collection dont le nom commence par 'Label_' selon les quantités spécifiées sur les axes X et Y.
    
    Args:
    collection (bpy.types.Collection): La collection d'objets Blender à parcourir.
    x (float): La quantité de déplacement sur l'axe X.
    y (float): La quantité de déplacement sur l'axe Y.
    """
    for objet in collection.objects:
        if objet.name.startswith("Label_") and not objet.name.startswith("Label_000"):
            objet.location.x += x
            objet.location.y += y


def creer_center_empty():
    """
    Crée un objet vide au barycentre de tous les vertex des objets dont le nom commence par 'Label_'.
    Supprime tout objet vide existant nommé "Center_Empty" avant de créer le nouveau.
    """
    # Vérifie s'il existe déjà un objet vide nommé "Center_Empty"
    existing_empty = bpy.data.objects.get("Center_Empty")

    # Si un tel objet existe, le supprime
    if existing_empty:
        bpy.data.objects.remove(existing_empty, do_unlink=True)

    # Récupère tous les objets de la scène dont le nom commence par "Label_"
    label_objects = [obj for obj in bpy.context.scene.objects if obj.name.startswith("Label_")]

    # Liste pour stocker les coordonnées des vertex de tous les objets
    all_vertices = []

    # Vérifie s'il y a des objets à traiter
    if label_objects:
        # Récupère les coordonnées des vertex de tous les objets
        for obj in label_objects:
            mesh = obj.data
            for vertex in mesh.vertices:
                world_vertex = obj.matrix_world @ vertex.co  # Convertit le vertex local en coordonnées mondiales
                all_vertices.append(world_vertex)

        # Calcule le barycentre des vertex
        center = mathutils.Vector()
        for vertex in all_vertices:
            center += vertex
        center /= len(all_vertices)

        # Crée un nouvel objet vide au barycentre des vertex
        bpy.ops.object.empty_add(location=center)
        empty_object = bpy.context.active_object
        empty_object.name = "Center_Empty"
        empty_object.empty_display_size = 0.5  # Réglez la taille d'affichage de l'objet vide selon vos préférences
        empty_object.empty_display_type = 'PLAIN_AXES'  # Réglez le type d'affichage de l'objet vide selon vos préférences
        print("Empty object created at the center of 'Label_' object vertices.")
    else:
        print("No objects with names starting with 'Label_' found in the scene.")


def configurer_camera_pour_suivre_center_empty():
    """
    Configure la caméra de la scène pour suivre l'objet vide "Center_Empty".
    Supprime toutes les contraintes de suivi existantes de la caméra et ajoute une nouvelle contrainte de suivi.
    """
    # Récupère la caméra de la scène
    camera = bpy.context.scene.camera

    # Supprime toutes les contraintes de suivi existantes de la caméra
    for constraint in camera.constraints:
        camera.constraints.remove(constraint)
        
    # Ajoute une nouvelle contrainte de suivi pour la caméra vers l'objet vide
    track_constraint = camera.constraints.new(type='TRACK_TO')
    track_constraint.target = bpy.data.objects.get("Center_Empty")
    track_constraint.track_axis = 'TRACK_NEGATIVE_Z'
    track_constraint.up_axis = 'UP_Y'
    print("Camera is now tracking the 'Center_Empty' object.")


def main_function():
    
    # Crée un objet vide au barycentre des objets "Label_"
    creer_center_empty()

    # Récupère les déplacements nécessaires pour aligner l'objet "Center_Empty" à la position (0, 0, z)
    deplacement_x, deplacement_y = deplacer_center_vers_position_z()

    # Déplace les objets de la collection selon les déplacements calculés
    collection = bpy.context.scene.collection
    deplacer_modeles_x_y(collection, deplacement_x, deplacement_y)

    # Configure la caméra pour suivre l'objet "Center_Empty"
    configurer_camera_pour_suivre_center_empty()
