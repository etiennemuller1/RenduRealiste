#pour utiliser le GPU il faut a chaque lancement de blender aller dans preference system cycle render devices est séléctionner celui souhaité, ici je prends CUDA et je le mets sur ma CG
import bpy

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.feature_set = 'SUPPORTED'
bpy.context.scene.cycles.device = 'GPU'
bpy.context.scene.cycles.adaptive_threshold = 0.01
bpy.context.scene.cycles.samples = 4096
bpy.context.scene.cycles.adaptive_min_samples = 0
bpy.context.scene.cycles.time_limit = 0
bpy.context.scene.cycles.use_denoising = True
bpy.context.scene.cycles.denoiser = 'OPENIMAGEDENOISE'
bpy.context.scene.cycles.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
bpy.context.scene.cycles.denoising_prefilter = 'ACCURATE'
bpy.context.scene.cycles.denoising_use_gpu = True
bpy.context.scene.cycles.use_light_tree = True
bpy.context.scene.cycles.seed = 0
bpy.context.scene.cycles.sample_offset = 0
bpy.context.scene.cycles.auto_scrambling_distance = False
bpy.context.scene.cycles.preview_scrambling_distance = False
bpy.context.scene.cycles.scrambling_distance = 1
bpy.context.scene.cycles.min_light_bounces = 0
bpy.context.scene.cycles.min_transparent_bounces = 0
bpy.context.scene.cycles.max_bounces = 7
bpy.context.scene.cycles.diffuse_bounces = 4
bpy.context.scene.cycles.glossy_bounces = 4
bpy.context.scene.cycles.transmission_bounces = 4
bpy.context.scene.cycles.volume_bounces = 0
bpy.context.scene.cycles.transparent_max_bounces = 8
bpy.context.scene.cycles.sample_clamp_direct = 0
bpy.context.scene.cycles.sample_clamp_indirect = 10
bpy.context.scene.cycles.blur_glossy = 1
bpy.context.scene.cycles.caustics_reflective = True
bpy.context.scene.cycles.caustics_refractive = True
bpy.context.scene.cycles.use_fast_gi = False
bpy.context.scene.cycles.volume_step_rate = 1
bpy.context.scene.cycles.volume_preview_step_rate = 1
bpy.context.scene.cycles.volume_max_steps = 1024
bpy.context.scene.cycles_curves.shape = 'RIBBONS'
bpy.context.scene.cycles_curves.subdivisions = 2
bpy.context.scene.render.use_simplify = False
bpy.context.scene.render.use_motion_blur = False
bpy.context.scene.cycles.film_exposure = 1
bpy.context.scene.cycles.film_exposure = 1
bpy.context.scene.cycles.filter_width = 1.5
bpy.context.scene.cycles.filter_width = 1.5
bpy.context.scene.render.threads_mode = 'AUTO'
bpy.context.scene.cycles.use_auto_tile = True
bpy.context.scene.cycles.tile_size = 2048
bpy.context.scene.cycles.debug_use_spatial_splits = False
bpy.context.scene.cycles.debug_bvh_time_steps = 0
bpy.context.scene.cycles.debug_use_hair_bvh = True
bpy.context.scene.cycles.debug_use_compact_bvh = False
bpy.context.scene.render.use_persistent_data = False
bpy.context.scene.grease_pencil_settings.antialias_threshold = 1
bpy.context.scene.grease_pencil_settings.antialias_threshold = 1
bpy.context.scene.display_settings.display_device = 'sRGB'
bpy.context.scene.view_settings.view_transform = 'Filmic'
bpy.context.scene.view_settings.look = 'None'
bpy.context.scene.view_settings.exposure = 0
bpy.context.scene.view_settings.gamma = 1
bpy.context.scene.sequencer_colorspace_settings.name = 'sRGB'
bpy.context.scene.view_settings.use_curve_mapping = False