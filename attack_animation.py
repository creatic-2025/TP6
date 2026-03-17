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


class AttackAnimation(arcade.Sprite):
    ATTACK_SCALE = 0.50
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        super().__init__()
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0
        self.attack_type = attack_type
        if self.attack_type == AttackType.ROCK:
            self.textures = [
                arcade.load_texture("fichier_images/srock.png"),
                arcade.load_texture("fichier_images/srock-attack.png"),
            ]
        elif self.attack_type == AttackType.PAPER:
            self.textures = [
                arcade.load_texture("fichier_images/spaper.png"),
                arcade.load_texture("fichier_images/spaper-attack.png"),
            ]
        else:
            self.textures = [
                arcade.load_texture("fichier_images/scissors.png"),
                arcade.load_texture("fichier_images/scissors-close.png"),
            ]
        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

    def on_update(self, delta_time: float = 1 / 60):
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture < len(self.textures):
                self.set_texture(self.current_texture)
            else:
                self.current_texture = 0
                self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0


# attack_animations = arcade.SpriteList()
# idle_animations = arcade.SpriteList()
# sprite_rock_idle = arcade.Sprite("fichier_images/srock.png", 0.75, 190, 135)
# player_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 0.50, 455, 349)
# cpu_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 0.50, 825, 349)
# sprite_paper_idle = arcade.Sprite("fichier_images/spaper.png", 0.75, 340, 120)
# player_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 0.55, 465, 349)
# cpu_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 0.55, 835, 349)
# sprite_scissors_idle = arcade.Sprite("fichier_images/scissors.png", 0.75, 490, 120)
# player_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 0.55, 460, 349)
# cpu_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 0.50, 825, 349)
#
# attack_animations.append(player_rock_attack)
# attack_animations.append(player_paper_attack)
# attack_animations.append(player_scissors_attack)
#
# attack_animations.append(cpu_rock_attack)
# attack_animations.append(cpu_paper_attack)
# attack_animations.append(cpu_scissors_attack)
#
# idle_animations.append(sprite_rock_idle)
# idle_animations.append(sprite_paper_idle)
# idle_animations.append(sprite_scissors_idle)
