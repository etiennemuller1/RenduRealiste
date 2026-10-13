import freecad
import FreeCAD
import MeshPart
import importOBJ
import Part
import os
import sys

def extraireMaillage(linearDeflection, angularDeflection, relative, outputFolder, documentName):
    # Ouvrir le document FreeCAD
    doc = FreeCAD.open(documentName)

    # Vérifier si doc.Objects n'est pas vide
    if not doc.Objects:
        print("Le document ne contient aucun objet.")
        return  # Sortir de la fonction

    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)

    # Appeler la fonction d'extraction pour chaque objet du document
    for obj in doc.Objects:
        if isinstance(obj, Part.Feature) and obj.Label.startswith("Label_"):  # Si l'objet est une partie et commence par "Label_"
            mesh = doc.addObject("Mesh::Feature", obj.Label + "_Meshed")

            # Générer le maillage à partir de la forme de l'objet
            shape = Part.getShape(obj, "")
            mesh.Mesh = MeshPart.meshFromShape(Shape=shape, LinearDeflection=linearDeflection,
                                               AngularDeflection=angularDeflection, Relative=relative)

            # Exporter le maillage au format OBJ dans le dossier de sortie
            meshName = os.path.join(outputFolder, obj.Label + ".obj")
            importOBJ.export([mesh], meshName)

def main_function(documentName, outputFolder, linearDeflection=2, angularDeflection=0.0174533, relative=False):
    # Appel de la fonction extraireMaillage avec les paramètres appropriés
    extraireMaillage(linearDeflection, angularDeflection, relative, outputFolder, documentName)

if __name__ == "__main__":
    # Récupérer les paramètres passés au script
    documentName = sys.argv[1]
    outputFolder = sys.argv[2]

    # Appeler la fonction avec les paramètres
    main_function(documentName, outputFolder)