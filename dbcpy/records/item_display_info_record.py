import dataclasses

_fields = {
    'id': int,
    'left_model': str,
    'right_model': str,
    'left_model_texture': str,
    'right_model_texture': str,
    'icon_1': str,
    'icon_2': str,
    'geoset_group_1': int,
    'geoset_group_2': int,
    'geoset_group_3': int,
    'flags': int,
    'spell_visual_id': int,
    'group_sound_index': int,
    'helmet_geoset_vis_male': int,
    'helmet_geoset_vis_female': int,
    'upper_arm_texture': str,
    'lower_arm_texture': str,
    'hands_texture': str,
    'upper_torso_texture': str,	
    'lower_torso_texture': str,
    'upper_leg_texture': str,
    'lower_leg_texture': str,
    'foot_texture': str,
    'item_visual': int,
    'particle_color_id': int
}

ItemDisplayInfoRecord = dataclasses.make_dataclass('ItemDisplayInfoRecord', zip(_fields.keys(), _fields.values()))
ItemDisplayInfoRecord.field_types = staticmethod(_fields.values())