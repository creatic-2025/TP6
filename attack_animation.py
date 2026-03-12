import arcade
from enum import Enum


class AttackType(Enum):
    """
   Simple énumération pour représenter les différents types d'attaques.
   """
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2
    NONE = 3


attack_animation_rock_player = arcade.SpriteList()
attack_animation_paper_player = arcade.SpriteList()
attack_animation_scissors_player = arcade.SpriteList()
attack_animation_rock_cpu = arcade.SpriteList()
attack_animation_paper_cpu = arcade.SpriteList()
attack_animation_scissors_cpu = arcade.SpriteList()
idle_animations = arcade.SpriteList()
sprite_rock_idle = arcade.Sprite("fichier_images/srock.png", 0.75, 190, 135)
player_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 0.50, 455, 349)
cpu_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 0.50, 825, 349)
sprite_paper_idle = arcade.Sprite("fichier_images/spaper.png", 0.75, 340, 120)
player_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 0.55, 465, 349)
cpu_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 0.55, 835, 349)
sprite_scissors_idle = arcade.Sprite("fichier_images/scissors.png", 0.75, 490, 120)
player_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 0.55, 460, 349)
cpu_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 0.50, 825, 349)

attack_animation_rock_player.append(player_rock_attack)
attack_animation_paper_player.append(player_paper_attack)
attack_animation_scissors_player.append(player_scissors_attack)

attack_animation_rock_cpu.append(cpu_rock_attack)
attack_animation_paper_cpu.append(cpu_paper_attack)
attack_animation_scissors_cpu.append(cpu_scissors_attack)

idle_animations.append(sprite_rock_idle)
idle_animations.append(sprite_paper_idle)
idle_animations.append(sprite_scissors_idle)

