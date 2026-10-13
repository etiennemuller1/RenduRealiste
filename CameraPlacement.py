import bpy
import math

def main_function(i, num_heights, j, frames_per_rotation, radius):
    """
    Positionne la caméra sur une orbite autour de l'objet à des hauteurs et angles différents,
    et insère des clés d'animation pour chaque position.

    Args:
    i (int): Indice de la hauteur de la caméra.
    num_heights (int): Nombre total de hauteurs de la caméra.
    j (int): Indice de la frame actuelle.
    frames_per_rotation (int): Nombre total de frames pour un tour complet.
    radius (float): Rayon de l'orbite de la caméra.
    """
    
    # Calcule l'angle d'incrémentation pour un tour complet
    angle_increment = 2 * math.pi / frames_per_rotation
    
    # Calcule la hauteur de la caméra en fonction de l'indice
    height = i * 2 * radius / num_heights
    
    # Positionne initialement la caméra à la hauteur désirée
    bpy.context.scene.camera.location.z = height
    
    # Calcule l'angle pour la frame actuelle
    angle = j * angle_increment
    
    # Calcule la position de la caméra sur l'orbite en fonction de l'angle
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    
    # Positionne la caméra sur l'orbite à la position calculée
    bpy.context.scene.camera.location.x = x
    bpy.context.scene.camera.location.y = y
    
    # Insère une nouvelle clé d'animation pour la position de la caméra
    bpy.context.scene.camera.keyframe_insert(data_path="location", index=-1)