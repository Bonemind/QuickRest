from peewee import *

database = MySQLDatabase('dnd', **{'host': 'localhost', 'password': 'NvideA', 'user': 'root'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Class(BaseModel):
    alignment = CharField(null=True)
    class_skills = TextField(null=True)
    epic_feat_base_level = CharField(null=True)
    epic_feat_interval = CharField(null=True)
    epic_feat_list = TextField(null=True)
    epic_full_text = TextField(null=True)
    full_text = TextField(null=True)
    hit_die = CharField(null=True)
    name = CharField(index=True)
    proficiencies = TextField(null=True)
    reference = CharField(null=True)
    req_base_attack_bonus = CharField(null=True)
    req_epic_feat = CharField(null=True)
    req_feat = CharField(null=True)
    req_languages = CharField(null=True)
    req_psionics = CharField(null=True)
    req_race = CharField(null=True)
    req_skill = CharField(null=True)
    req_special = CharField(null=True)
    req_spells = CharField(null=True)
    req_weapon_proficiency = CharField(null=True)
    skill_points = CharField(null=True)
    skill_points_ability = CharField(null=True)
    spell_list_1 = TextField(null=True)
    spell_list_2 = CharField(null=True)
    spell_list_3 = CharField(null=True)
    spell_list_4 = CharField(null=True)
    spell_list_5 = CharField(null=True)
    spell_stat = CharField(null=True)
    spell_type = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'class'

class ClassTable(BaseModel):
    ac_bonus = CharField(null=True)
    base_attack_bonus = CharField(null=True)
    bonus_spells = CharField(null=True)
    caster_level = CharField(null=True)
    flurry_of_blows = CharField(null=True)
    fort_save = CharField(null=True)
    level = CharField(null=True)
    name = CharField(index=True)
    points_per_day = CharField(null=True)
    power_level = CharField(null=True)
    powers_known = CharField(null=True)
    ref_save = CharField(null=True)
    reference = CharField(null=True)
    slots_0 = CharField(null=True)
    slots_1 = CharField(null=True)
    slots_2 = CharField(null=True)
    slots_3 = CharField(null=True)
    slots_4 = CharField(null=True)
    slots_5 = CharField(null=True)
    slots_6 = CharField(null=True)
    slots_7 = CharField(null=True)
    slots_8 = CharField(null=True)
    slots_9 = CharField(null=True)
    special = CharField(null=True)
    spells_known_0 = CharField(null=True)
    spells_known_1 = CharField(null=True)
    spells_known_2 = CharField(null=True)
    spells_known_3 = CharField(null=True)
    spells_known_4 = CharField(null=True)
    spells_known_5 = CharField(null=True)
    spells_known_6 = CharField(null=True)
    spells_known_7 = CharField(null=True)
    spells_known_8 = CharField(null=True)
    spells_known_9 = CharField(null=True)
    unarmed_damage = CharField(null=True)
    unarmored_speed_bonus = CharField(null=True)
    will_save = CharField(null=True)

    class Meta:
        db_table = 'class_table'

class Domain(BaseModel):
    full_text = TextField(null=True)
    granted_powers = TextField(null=True)
    name = CharField(index=True)
    reference = CharField(null=True)
    spell_1 = CharField(null=True)
    spell_2 = CharField(null=True)
    spell_3 = CharField(null=True)
    spell_4 = CharField(null=True)
    spell_5 = CharField(null=True)
    spell_6 = CharField(null=True)
    spell_7 = CharField(null=True)
    spell_8 = CharField(null=True)
    spell_9 = CharField(null=True)

    class Meta:
        db_table = 'domain'

class Equipment(BaseModel):
    arcane_spell_failure_chance = CharField(null=True)
    armor_check_penalty = CharField(null=True)
    armor_shield_bonus = CharField(null=True)
    category = CharField(null=True)
    cost = CharField(null=True)
    critical = CharField(null=True)
    dmg_m = CharField(null=True)
    dmg_s = CharField(null=True)
    family = CharField(null=True)
    full_text = TextField(null=True)
    maximum_dex_bonus = CharField(null=True)
    name = CharField(index=True)
    range_increment = CharField(null=True)
    reference = CharField(null=True)
    speed_20 = CharField(null=True)
    speed_30 = CharField(null=True)
    subcategory = CharField(null=True)
    type = CharField(null=True)
    weight = CharField(null=True)

    class Meta:
        db_table = 'equipment'

class Feat(BaseModel):
    benefit = TextField(null=True)
    choice = CharField(null=True)
    full_text = TextField(null=True)
    multiple = CharField(null=True)
    name = CharField(index=True)
    normal = TextField(null=True)
    prerequisite = TextField(null=True)
    reference = CharField(null=True)
    special = TextField(null=True)
    stack = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'feat'

class Item(BaseModel):
    aura = CharField(null=True)
    caster_level = CharField(null=True)
    category = CharField(null=True)
    cost = CharField(null=True)
    full_text = TextField(null=True)
    manifester_level = CharField(null=True)
    name = CharField(index=True)
    prereq = TextField(null=True)
    price = CharField(null=True)
    reference = CharField(null=True)
    special_ability = CharField(null=True)
    subcategory = CharField(null=True)
    weight = CharField(null=True)

    class Meta:
        db_table = 'item'

class Monster(BaseModel):
    abilities = CharField(null=True)
    advancement = CharField(null=True)
    alignment = CharField(null=True)
    altname = CharField(null=True)
    armor_class = CharField(null=True)
    attack = CharField(null=True)
    base_attack = CharField(null=True)
    bonus_feats = CharField(null=True)
    challenge_rating = CharField(null=True)
    descriptor = CharField(null=True)
    environment = CharField(null=True)
    epic_feats = TextField(null=True)
    family = CharField(null=True)
    feats = TextField(null=True)
    full_attack = TextField(null=True)
    full_text = TextField(null=True)
    grapple = CharField(null=True)
    hit_dice = CharField(null=True)
    initiative = CharField(null=True)
    level_adjustment = CharField(null=True)
    name = CharField(index=True)
    organization = TextField(null=True)
    reach = CharField(null=True)
    reference = CharField(null=True)
    saves = CharField(null=True)
    size = CharField(null=True)
    skills = TextField(null=True)
    space = CharField(null=True)
    special_abilities = TextField(null=True)
    special_attacks = CharField(null=True)
    special_qualities = TextField(null=True)
    speed = CharField(null=True)
    stat_block = TextField(null=True)
    treasure = CharField(null=True)
    type = CharField(null=True)

    class Meta:
        db_table = 'monster'

class Power(BaseModel):
    area = CharField(null=True)
    augment = TextField(null=True)
    description = TextField(null=True)
    descriptor = CharField(null=True)
    discipline = CharField(null=True)
    display = CharField(null=True)
    duration = CharField(null=True)
    effect = CharField(null=True)
    full_text = TextField(null=True)
    level = CharField(null=True)
    manifesting_time = CharField(null=True)
    name = CharField(index=True)
    power_points = CharField(null=True)
    power_range = CharField(null=True)
    power_resistance = CharField(null=True)
    reference = CharField(null=True)
    saving_throw = CharField(null=True)
    short_description = TextField(null=True)
    subdiscipline = CharField(null=True)
    target = CharField(null=True)
    xp_cost = TextField(null=True)

    class Meta:
        db_table = 'power'

class Skill(BaseModel):
    action = TextField(null=True)
    armor_check = CharField(null=True)
    description = TextField(null=True)
    epic_use = TextField(null=True)
    full_text = TextField(null=True)
    key_ability = CharField(null=True)
    name = CharField(index=True)
    psionic = CharField(null=True)
    reference = CharField(null=True)
    restriction = TextField(null=True)
    skill_check = TextField(null=True)
    special = TextField(null=True)
    subtype = TextField(null=True)
    synergy = TextField(null=True)
    trained = CharField(null=True)
    try_again = TextField(null=True)
    untrained = TextField(null=True)

    class Meta:
        db_table = 'skill'

class Spell(BaseModel):
    altname = CharField(null=True)
    arcane_focus = CharField(null=True)
    arcane_material_components = CharField(null=True)
    area = CharField(null=True)
    bard_focus = CharField(null=True)
    casting_time = CharField(null=True)
    cleric_focus = CharField(null=True)
    components = TextField(null=True)
    description = TextField(null=True)
    descriptor = CharField(null=True)
    druid_focus = CharField(null=True)
    duration = CharField(null=True)
    effect = CharField(null=True)
    focus = TextField(null=True)
    full_text = TextField(null=True)
    level = CharField(null=True)
    material_components = TextField(null=True)
    name = CharField(index=True)
    reference = CharField(null=True)
    saving_throw = CharField(null=True)
    school = CharField(null=True)
    short_description = CharField(null=True)
    sorcerer_focus = CharField(null=True)
    spell_range = CharField(null=True)
    spell_resistance = CharField(null=True)
    spellcraft_dc = CharField(null=True)
    subschool = CharField(null=True)
    target = CharField(null=True)
    to_develop = TextField(null=True)
    verbal_components = CharField(null=True)
    wizard_focus = CharField(null=True)
    xp_cost = TextField(null=True)

    class Meta:
        db_table = 'spell'

