from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    bio = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    picture = models.FileField(blank=True, upload_to="")
    content_type = models.CharField(max_length=50)


class Game(models.Model):
    GM = models.ForeignKey(User, on_delete=models.PROTECT, related_name="game_master")
    PLs = models.ManyToManyField(User, related_name="players")


class Chat(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)


class Log(models.Model):
    text = models.CharField(max_length=200)
    game = models.ForeignKey(Game, default=None, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)


class CharacterCOC(models.Model):
    # relationships
    PL = models.ForeignKey(User, on_delete=models.PROTECT)
    in_game = models.BooleanField(default=False)

    # basic information
    name = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    age = models.IntegerField()

    # characteristics
    strength = models.IntegerField()
    constitution = models.IntegerField()
    dexterity = models.IntegerField()
    size = models.IntegerField()
    power = models.IntegerField()
    appearance = models.IntegerField()
    intelligence = models.IntegerField()
    education = models.IntegerField()
    luck = models.IntegerField()

    # status
    current_hit_points = models.IntegerField()
    current_magic_points = models.IntegerField()
    current_sanity = models.IntegerField()
    temporary_insanity = models.BooleanField(default=False)
    indefinite_insanity = models.BooleanField(default=False)
    major_wound = models.BooleanField(default=False)
    unconscious = models.BooleanField(default=False)
    dying = models.BooleanField(default=False)

    # descriptions
    my_story = models.CharField(max_length=200)
    wealth = models.CharField(max_length=200)
    items = models.CharField(max_length=200)
    personal_description = models.CharField(max_length=200)
    ideology_beliefs = models.CharField(max_length=200)
    significant_people = models.CharField(max_length=200)
    meaningful_locations = models.CharField(max_length=200)
    treasured_possessions = models.CharField(max_length=200)
    traits = models.CharField(max_length=200)
    injuries_scars = models.CharField(max_length=200)
    phobias_manias = models.CharField(max_length=200)
    arcane_spells = models.CharField(max_length=200)
    encounters_with_strange_entities = models.CharField(max_length=200)

    # skills
    accounting = models.IntegerField(default=0)
    anthropology = models.IntegerField(default=0)
    appraise = models.IntegerField(default=0)
    archaeology = models.IntegerField(default=0)
    art_craft = models.IntegerField(default=0)
    charm = models.IntegerField(default=0)
    climb = models.IntegerField(default=0)
    credit_rating = models.IntegerField(default=0)
    cthulhu_mythos = models.IntegerField(default=0)
    disguise = models.IntegerField(default=0)
    dodge = models.IntegerField(default=0)
    drive_auto = models.IntegerField(default=0)
    elec_repair = models.IntegerField(default=0)
    fast_talk = models.IntegerField(default=0)
    fighting = models.IntegerField(default=0)
    firearms = models.IntegerField(default=0)
    first_aid = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    intimidate = models.IntegerField(default=0)
    jump = models.IntegerField(default=0)
    language = models.IntegerField(default=0)
    law = models.IntegerField(default=0)
    library = models.IntegerField(default=0)
    listen = models.IntegerField(default=0)
    locksmith = models.IntegerField(default=0)
    mech_repair = models.IntegerField(default=0)
    medicine = models.IntegerField(default=0)
    natural_world = models.IntegerField(default=0)
    navigate = models.IntegerField(default=0)
    occult = models.IntegerField(default=0)
    persuade = models.IntegerField(default=0)
    pilot = models.IntegerField(default=0)
    psychoanalysis = models.IntegerField(default=0)
    psychology = models.IntegerField(default=0)
    ride = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    sleight_of_hand = models.IntegerField(default=0)
    spot_hidden = models.IntegerField(default=0)
    stealth = models.IntegerField(default=0)
    survival = models.IntegerField(default=0)
    swim = models.IntegerField(default=0)
    throw = models.IntegerField(default=0)
    track = models.IntegerField(default=0)
    others = models.IntegerField(default=0)
    describe = models.CharField(max_length=200)