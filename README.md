# ProjetRenduRealiste
 génération d'image photoréaliste pour Yolo


Ce Projet à pour but de générer des images photoréalistes labélisées.
Les labélisations actuelles sont : les écrous, les vis, les rondelles, les axes et les engrenages.

Le but de générer ces images est de créer une base de donnée d'image pour faire de l'apprentissage machine.
Yolo est utiliser pout tester la base de donnée générée.


Description des différents fichiers et dossiers:

-ExtractionDeMaillage : ce dossiers contient la méthode python pour extraire le maillage d'un ensemble de fichier CAO. Ces modèles seront à placer dans le dossier "ModèlesCAO". Ils doivent être enregister au format FCStd. De plus FreeCAD(python) est nécessaire à l'utilisation de cette méthode.

-hdri : ce dossier contient un ensemble de fichier hdr qui ont pour but de rajouter des jeux de lumières(ici le dossiers est vide car ces fichiers sont volumineux).

-Maillages : ce dossier contient l'ensemble de tout les maillages extrait par le programme ExtractionDeMaillage. Chaque sous dossiers contient l'ensemble des maillages d'un seul modèle.

-Materiaux : ce dossier contient une liste de fichier .blend. Chacun de ces fichier ont un nom de matériaux choisis. Pour selectionner les matériaux à importer dans ces fichier .blend, il faut utiliser blender kit et les télécharger.

-ModèlesCAO : ce dossier contient tout les modèles CAO que l'on veut extraire avec la méthode extraction de maillage. Ils doivent être enregister au format .FCStd.

-Rendu: contient l'ensemble des rendus d'images photoréalistes et labélisées.

-Scènes : contient l'ensemble des scènes générer par la méthode setup.py. La méthode rendu devra être utilisé sur ces scènes.

-ApplyColorLabel.py : méthode pour appliquer la couleur associée aux labels des différents pièces de la scène.

-ApplyColorLabelSorted.py : pas utilisé

-ApplyColorLabelUnique.py : pas utilisé

-ApplyMaterialRealist.py : méthode pour appliquer les matériaux réalistes associée aux différents pièces de la scène.

-CameraLookAtBarycentre.py : méthode pour que la caméra regarde toujour la centre de du modèle importer.

-CameraPlacement.py : méthode pour placer la caméra autour du modèle.

-EnvironnementManager.py : import de l'hdri et application.

-ExtractionDeMaillage.py : méthode qui appel utilise la méthode dans le dossier ExtractionDeMaillage.

-GenerateAllColorLabel.py : méthode pour créer tout type de texture de labélisation.

-GenerateColorLabel.py : génère une texture par numéro de pièces (généré mais pas utilisé).

-GenerateColorLabelGroup.py : génére une texture par labels.

-GenerateColorLabelUnique.py : génére une texture par pièces (généré mais pas utilisé).

-Main.py : méthode à utiliser pour effectuer le rendu de la scène courante. Les paramètres de nombre de prise de vue, nombre de hauteur de vue et distance de caméra sont modifiable ici.

-MaterialsImport.py : méthode pour importer les matériaux, présent dans le dossier Matériaux, qui sont nécessaire à la scène.

-MaterialsLink.py :

-ObjectImport.py : permet d'importer l'ensemble de tout les maillages d'un modèle à la scène.

-RenderColorLabelParameter.py : liste de paramètres de rendu labélisé.

-RenderRealist.py : méthode de rendu réaliste

-RenderRealisteParameter.py : liste de paramètres de rendu réaliste.

-Rendu.py : méthode pour lancer tout les rendu.

-RenduLabel.py : méthode de rendu labélisé.

-ScaleObject.py : méthode de mise à l'échelle du modèle de la scène.

-SceneGenerator.py : méthode pour créer la scène. Création de la table, scale de du modèle et déplacement du modèle sur la table.

-Setup.py :

-ShadeSmooth.py : lisse les surfaces du modèle de la scène.

-renduRealiste.blend :




