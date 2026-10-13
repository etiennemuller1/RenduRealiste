import os
import bpy

def trouver_vertex_le_plus_bas(collection):
    """Trouve le vertex le plus bas parmi tous les objets dans une collection."""
    vertex_le_plus_bas = None
    plus_basse_hauteur = float('inf')  # Initialisation à une valeur infinie

    # Parcours tous les objets dans la collection
    for objet in collection.objects:
        # Vérifie si l'objet est un maillage (mesh) et commence par le préfixe "Label_"
        if objet.type == 'MESH' and objet.name.startswith("Label_"):
            # Parcours tous les vertices de l'objet
            for vertex in objet.data.vertices:
                # Calcule la position globale du vertex dans le monde
                global_vertex = objet.matrix_world @ vertex.co
                # Vérifie si la hauteur Z du vertex global est inférieure à la plus basse hauteur actuellement enregistrée
                if global_vertex.z < plus_basse_hauteur:
                    plus_basse_hauteur = global_vertex.z
                    vertex_le_plus_bas = global_vertex

    return vertex_le_plus_bas

def deplacer_modeles_vers_haut(collection, hauteur):
    """Déplace tous les modèles avec le préfixe 'Label' dans une collection vers le haut de la hauteur spécifiée."""
    for objet in collection.objects:
        # Vérifie si le nom de l'objet commence par "Label_"
        if objet.name.startswith("Label_"):
            # Déplace l'objet vers le haut en ajoutant la hauteur spécifiée à sa position Z
            objet.location.z -= hauteur

def delete_table():
    """Supprime l'objet de type 'Label_000_table_table_table' s'il existe déjà."""
    object_name = "Label_000_table_table_table"
    
    existing_object = bpy.data.objects.get(object_name)
    if existing_object:
        # Supprime l'objet de la scène
        bpy.data.objects.remove(existing_object, do_unlink=True)

def create_table(width=10, depth=10, height=0.5):
    """Crée un objet de type table avec les dimensions spécifiées."""
    object_name = "Label_000_table_table_table"
        
    # Crée un cube (primitive_cube_add crée un cube centré à l'origine)
    bpy.ops.mesh.primitive_cube_add(size=1)
    cube = bpy.context.active_object
    
    # Met à l'échelle le cube selon les dimensions spécifiées
    cube.scale = (width/2, depth/2, height/2)
    
    # Place le cube avec la face supérieure à la hauteur spécifiée
    cube.location.z = -height/4
    
    # Renomme le cube avec le nom spécifié
    cube.name = object_name

def main_function():
    """Fonction principale pour le traitement des objets et la création de la table."""
    os.system('cls')  # Efface la console (commande spécifique à Windows)
    delete_table()  # Supprime la table s'il existe déjà
    bpy.context.view_layer.update()  # Met à jour la vue Blender pour refléter les changements

    # Récupère la collection principale de la scène
    collection = bpy.context.scene.collection

    # Trouve le vertex le plus bas parmi tous les objets dans la collection
    vertex_plus_bas = trouver_vertex_le_plus_bas(collection)

    # Récupère la hauteur Z du vertex le plus bas trouvé
    hauteur = vertex_plus_bas.z

    # Déplace tous les modèles dont le nom commence par "Label_" vers le haut de la hauteur trouvée
    deplacer_modeles_vers_haut(collection, hauteur)

    # Crée une nouvelle table avec des dimensions par défaut
    create_table()

    bpy.context.view_layer.update()  # Met à jour la vue Blender pour refléter les changements

    # Affiche un message confirmant que tous les modèles ont été déplacés de la hauteur trouvée
    print("Tous les modèles ont été déplacés de", hauteur)

main_function()  # Appel de la fonction principale pour exécuter le script
