"""
    Models
"""
from django.db import models


class Player(models.Model):
    """
        Player table.
        Basic fields for maximun compatibility
    """
    account_id = models.PositiveIntegerField()
    name = models.CharField(max_length=24)
    job = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    exp = models.IntegerField()

    class Meta:
        """
            Add Meta information
        """
        managed = False
        db_table = "player"

    def __str__(self):
        return f"{self.name}"


class Guild(models.Model):
    """
        Guild Table
        Basic fields for maximun compatibility
    """
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

    class Meta:
        """
            Meta Information
        """
        managed = False
        db_table = "guild"

    def __str__(self):
        return f"{self.name}"
