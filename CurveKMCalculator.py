import bpy

# Obtenir l'objet actif
context = bpy.context
aobj = context.active_object

# Vérifier si l'objet est une courbe
if aobj and aobj.type == 'CURVE':
    longueur_totale = 0.0  # Initialiser la longueur totale

    # Parcourir les splines de la courbe
    for spline in aobj.data.splines:
        if spline.type == 'BEZIER':
            # Pour les splines Bezier, calculer la distance entre les points de contrôle
            for i in range(len(spline.bezier_points) - 1):
                p1 = aobj.matrix_world @ spline.bezier_points[i].co
                p2 = aobj.matrix_world @ spline.bezier_points[i + 1].co
                longueur_totale += (p2 - p1).length
        elif spline.type == 'NURBS' or spline.type == 'POLY':
            # Pour les splines NURBS et Poly, calculer la distance entre les points
            for i in range(len(spline.points) - 1):
                p1 = aobj.matrix_world @ spline.points[i].co.xyz
                p2 = aobj.matrix_world @ spline.points[i + 1].co.xyz
                longueur_totale += (p2 - p1).length

    # Convertir la longueur en kilomètres
    longueur_km = longueur_totale / 1000.0

    # Afficher la longueur totale avec plus de précision (6 chiffres après la virgule)
    print(f"Longueur totale de la courbe : {longueur_totale:.6f} unités")
    print(f"Longueur totale de la courbe : {longueur_km:.6f} km")

    # Afficher un popup avec la longueur totale en km avec précision
    def draw(self, context):
        self.layout.label(text=f"Longueur de la courbe : {longueur_km:.6f} km")
    
    bpy.context.window_manager.popup_menu(draw, title="Longueur de la courbe", icon="INFO")

else:
    print("Veuillez sélectionner un objet de type courbe.")
