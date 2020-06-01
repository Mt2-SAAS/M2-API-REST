"""
    Models
"""
from django.db import models


class Player(models.Model):
    account_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    job = models.PositiveIntegerField()
    voice = models.IntegerField()
    dir = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    map_index = models.IntegerField()
    exit_x = models.IntegerField()
    exit_y = models.IntegerField()
    exit_map_index = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    stamina = models.SmallIntegerField()
    random_hp = models.SmallIntegerField()
    random_sp = models.SmallIntegerField()
    playtime = models.IntegerField()
    level = models.PositiveIntegerField()
    level_step = models.IntegerField()
    st = models.SmallIntegerField()
    ht = models.SmallIntegerField()
    dx = models.SmallIntegerField()
    iq = models.SmallIntegerField()
    exp = models.IntegerField()
    gold = models.IntegerField()
    stat_point = models.SmallIntegerField()
    skill_point = models.SmallIntegerField()
    quickslot = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    part_main = models.IntegerField()
    part_base = models.IntegerField()
    part_hair = models.IntegerField()
    part_sash = models.PositiveSmallIntegerField()
    skill_group = models.IntegerField()
    skill_level = models.TextField(blank=True, null=True)
    alignment = models.IntegerField()
    prestige = models.PositiveSmallIntegerField()
    last_play = models.DateTimeField()
    change_name = models.IntegerField()
    mobile = models.CharField(max_length=24, blank=True, null=True)
    sub_skill_point = models.SmallIntegerField()
    stat_reset_count = models.IntegerField()
    horse_hp = models.SmallIntegerField()
    horse_stamina = models.SmallIntegerField()
    horse_level = models.PositiveIntegerField()
    horse_hp_droptime = models.PositiveIntegerField()
    horse_riding = models.IntegerField()
    horse_skill_point = models.SmallIntegerField()
    pz = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'player'

    def __str__(self):
        return self.name 


class Guild(models.Model):
    name = models.CharField(max_length=12)
    sp = models.SmallIntegerField()
    master = models.PositiveIntegerField()
    level = models.IntegerField(blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    skill_point = models.IntegerField()
    skill = models.TextField(blank=True, null=True)
    win = models.IntegerField()
    draw = models.IntegerField()
    loss = models.IntegerField()
    ladder_point = models.IntegerField()
    gold = models.IntegerField()
    dungeon_ch = models.IntegerField()
    dungeon_map = models.PositiveIntegerField()
    dungeon_cooldown = models.PositiveIntegerField()
    dungeon_start = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guild'

    def __str__(self):
        return self.name
