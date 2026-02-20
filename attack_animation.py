import arcade
from enum import Enum


class AttackType(Enum):
    """
   Simple énumération pour représenter les différents types d'attaques.
   """
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2


attack_animations = arcade.SpriteList()
idle_animations = arcade.SpriteList()
sprite_rock_idle = arcade.Sprite("fichier_images/srock.png", 0.75, 190, 135)
sprite_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 0.75, 190, 100)
sprite_paper_idle = arcade.Sprite("fichier_images/spaper.png", 0.75, 340, 120)
sprite_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 0.75, 340, 100)
sprite_scissors_idle = arcade.Sprite("fichier_images/scissors.png", 0.75, 490, 120)
sprite_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 0.75, 490, 100)

attack_animations.append(sprite_rock_attack)
attack_animations.append(sprite_paper_attack)
attack_animations.append(sprite_scissors_attack)

idle_animations.append(sprite_rock_idle)
idle_animations.append(sprite_paper_idle)
idle_animations.append(sprite_scissors_idle)

