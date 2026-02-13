import arcade
attack_animations = arcade.SpriteList()
sprite_rock_idle = arcade.Sprite("fichier_images/srock.png", 1, 200, 100)
sprite_rock_attack = arcade.Sprite("fichier_images/srock-attack.png", 1, 200, 100)
sprite_paper_idle = arcade.Sprite("fichier_images/spaper.png", 1, 300, 100)
sprite_paper_attack = arcade.Sprite("fichier_images/spaper-attack.png", 1, 300, 100)
sprite_scissors_idle = arcade.Sprite("fichier_images/scissors.png", 1, 400, 100)
sprite_scissors_attack = arcade.Sprite("fichier_images/scissors-close.png", 1, 400, 100)

attack_animations.append(sprite_rock_idle)
attack_animations.append(sprite_rock_attack)
attack_animations.append(sprite_paper_idle)
attack_animations.append(sprite_paper_attack)
attack_animations.append(sprite_scissors_idle)
attack_animations.append(sprite_scissors_attack)



