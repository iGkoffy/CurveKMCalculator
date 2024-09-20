
### Script Blender : Calcul de la Longueur d'une Courbe

Ce script Python pour Blender permet de calculer avec précision la longueur totale d'une courbe (**Bezier**, **NURBS**, ou **POLY**) directement à partir des splines, sans conversion en mesh.

#### Fonctionnalités :
- Prend en charge les types de courbes : **Bezier**, **NURBS**, et **POLY**.
- Calcule la longueur en utilisant les points de contrôle des splines, avec prise en compte des transformations globales de l'objet.
- Affiche la longueur en **unités Blender** ainsi qu'en **kilomètres (km)**, avec une précision ajustable (par défaut 6 chiffres après la virgule).
- Affiche les résultats dans la console et dans un popup Blender.

#### Utilisation :
1. Sélectionnez un objet de type **courbe** dans Blender.
2. Exécutez le script depuis l'éditeur de texte de Blender.
3. Le script affichera la longueur totale de la courbe dans la console Blender ainsi que dans un popup.

#### Exemple :
- Longueur en unités Blender : `33262.078612 unités`
- Longueur convertie en kilomètres : `33.262079 km`

#### Configuration de précision :
Vous pouvez ajuster la précision des résultats en modifiant le format d'affichage (actuellement réglé sur 6 chiffres après la virgule).

---

#### Comment utiliser :
- Téléchargez le script.
- Ouvrez-le dans l'éditeur de texte de Blender.
- Sélectionnez une courbe, puis exécutez le script.

---

Ce script est utile pour ceux qui souhaitent obtenir une mesure précise de la longueur d'une courbe dans Blender sans avoir à la convertir en mesh, tout en conservant la flexibilité des types de courbes pris en charge.

---

#### Contributions :
Les contributions sont les bienvenues ! Si vous souhaitez améliorer le script ou ajouter des fonctionnalités, n'hésitez pas à soumettre des pull requests.
