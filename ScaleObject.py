import bpy

# Fonction pour trouver la plus grande dimension d'un objet
def find_largest_dimension(obj):
    dimensions = obj.dimensions  # Récupère les dimensions de l'objet
    return max(dimensions)  # Retourne la plus grande dimension parmi les trois (longueur, largeur, hauteur)

# Fonction pour trouver la hauteur maximale d'un objet
def find_max_height(obj):
    return obj.dimensions.z  # Retourne la dimension en hauteur (z) de l'objet

# Fonction principale pour redimensionner les objets dont le nom commence par "Label_"
def main_function():
    """
    Redimensionne les objets dont le nom commence par "Label_" de manière à ce que l'objet le plus haut ait une hauteur de 1 mètre.
    """

    # Désélectionne tous les objets dans la scène
    bpy.ops.object.select_all(action='DESELECT')
    
    # Sélectionne tous les objets dont le nom commence par "Label_"
    selected_objects = [obj for obj in bpy.context.scene.objects if obj.name.startswith("Label_")]

    # Vérifie s'il y a des objets sélectionnés
    if not selected_objects:
        print("Aucun objet trouvé avec le préfixe 'Label_'")
        return

    # Trouve la hauteur maximale parmi tous les objets sélectionnés
    max_height = max([find_max_height(obj) for obj in selected_objects])

    # Calcul du facteur d'échelle pour que l'objet le plus haut fasse 1 mètre de hauteur
    scale_factor = 1.0 / max_height

    # Applique l'échelle à tous les objets sélectionnés
    for obj in selected_objects:
        obj.scale *= scale_factor  # Multiplie l'échelle actuelle de l'objet par le facteur d'échelle calculé

