from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField
    item_name = models.CharField(max_length=30)
    item_description = models.CharField(max_length=2056)
    item_cost = models.IntegerField

    class Item_Type(models.TextChoices):
        WEAPON = "weapon", "Weapon";
        ARMOUR = "armour", "Armour";
        POTION = "potion", "Potion";
        RING = "ring", "Ring";
        ROD = "rod", "Rod";
        SCROLL = "scroll", "Scroll";
        STAFF = "staff", "Staff";
        WAND = "wand", "Wand";

    class Item_Rarity(models.TextChoices):
        COMMON = "common", "Common";
        UNCOMMON = "uncommon", "Uncommon";
        RARE = "rare", "Rare";
        VERY_RARE = "very rare", "Very Rare";
        LEGENDARY = "legendary", "Legnedary";
        



