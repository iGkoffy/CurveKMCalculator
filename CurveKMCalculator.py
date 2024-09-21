import bpy

# Obtenir tous les objets sélectionnés
context = bpy.context
selected_objects = context.selected_objects

# Initialiser la longueur totale pour toutes les courbes
longueur_totale_globale = 0.0

# Parcourir tous les objets sélectionnés
for obj in selected_objects:
    # Vérifier si l'objet est une courbe
    if obj.type == 'CURVE':
        longueur_totale = 0.0  # Initialiser la longueur pour chaque courbe

        # Parcourir les splines de la courbe
        for spline in obj.data.splines:
            if spline.type == 'BEZIER':
                # Pour les splines Bezier, calculer la distance entre les points de contrôle
                for i in range(len(spline.bezier_points) - 1):
                    p1 = obj.matrix_world @ spline.bezier_points[i].co
                    p2 = obj.matrix_world @ spline.bezier_points[i + 1].co
                    longueur_totale += (p2 - p1).length
            elif spline.type == 'NURBS' or spline.type == 'POLY':
                # Pour les splines NURBS et Poly, calculer la distance entre les points
                for i in range(len(spline.points) - 1):
                    p1 = obj.matrix_world @ spline.points[i].co.xyz
                    p2 = obj.matrix_world @ spline.points[i + 1].co.xyz
                    longueur_totale += (p2 - p1).length

        # Ajouter la longueur de cette courbe à la longueur globale
        longueur_totale_globale += longueur_totale

# Convertir la longueur totale en kilomètres
longueur_km_globale = longueur_totale_globale / 1000.0

# Afficher la longueur totale dans la console
print(f"Longueur totale des courbes sélectionnées : {longueur_totale_globale:.6f} unités")
print(f"Longueur totale des courbes sélectionnées : {longueur_km_globale:.6f} km")

# Afficher un popup avec la longueur totale en km avec précision
def draw(self, context):
    self.layout.label(text=f"Longueur totale des courbes : {longueur_km_globale:.6f} km")

bpy.context.window_manager.popup_menu(draw, title="Longueur totale des courbes", icon="INFO")
