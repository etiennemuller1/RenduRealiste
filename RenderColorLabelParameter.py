import bpy

#parametre de rendu d'image pour le label
bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
bpy.context.scene.display.render_aa = "OFF"
bpy.context.scene.display.shading.light = 'FLAT'
bpy.context.scene.display.shading.color_type = 'MATERIAL'
bpy.context.scene.display.shading.show_backface_culling = False
bpy.context.scene.display.shading.show_cavity = False
bpy.context.scene.display.shading.show_object_outline = False
bpy.context.scene.render.use_high_quality_normals = True
bpy.context.scene.display.shading.show_object_outline = False
bpy.context.scene.render.film_transparent = False
bpy.context.scene.render.use_simplify = False
bpy.context.scene.grease_pencil_settings.antialias_threshold = 1
bpy.context.scene.render.use_freestyle = False
bpy.context.scene.display_settings.display_device = 'sRGB'
bpy.context.scene.view_settings.view_transform = 'Raw'
bpy.context.scene.view_settings.look = 'None'
bpy.context.scene.view_settings.exposure = 0
bpy.context.scene.view_settings.gamma = 1
bpy.context.scene.sequencer_colorspace_settings.name = 'sRGB'
bpy.context.scene.view_settings.use_curve_mapping = False