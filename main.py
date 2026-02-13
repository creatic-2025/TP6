import arcade
from game_state import GameState
import time
import attack_animation

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Roche, Papier, Ciseaux mais low quality"

text_that_hurts_your_eyes = True




class GameView(arcade.View):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self):
        super().__init__()

        self.soustitre_jeu_roundfinijoueur = None
        self.soustitre_jeu_init = None
        self.soustitre_jeu_round = None
        self.sprite_list = arcade.SpriteList()
        self.background_color = arcade.color.DARK_GRAY
        self.rock = attack_animation.sprite_rock_idle
        sprite_person = arcade.Sprite("fichier_images/person.jpg", 1.5, 350, 350)
        sprite_computer = arcade.Sprite("fichier_images/computer.jpg", 1.35, 950, 350)
        self.sprite_list.append(sprite_person)
        self.sprite_list.append(sprite_computer)
        self.current_status = GameState.NOT_STARTED
        self.player_attack_type = None

        self.reset()

        # If you have sprite lists, you should create them here,
        # and set them to None

    def reset(self):
        """Reset the game to the initial state."""
        # Do changes needed to restart the game here if you want to support that
        self.soustitre_jeu_round = arcade.Text("appuye sur une image pour faire une attaque", 300, 500,
                                               arcade.csscolor.DARK_BLUE,
                                               25, 1, "center", "Arial")

        self.soustitre_jeu_init = arcade.Text("appuye sur espace pour commencer une nouvelle ronde", 230, 500,
                                              arcade.csscolor.DARK_BLUE,
                                              25, 1, "center", "Arial")
        self.soustitre_jeu_roundfinijoueur = arcade.Text("Le joueur a gagné la ronde", 230, 400,
                                                         arcade.csscolor.DARK_BLUE,
                                                         25, 1, "center", "Arial")

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()
        titre_jeu = arcade.Text("roche, papier, ciseaux", 375, 600, arcade.csscolor.BLACK, 40, 1, "center", "Arial")
        titre_jeu.draw()
        if self.current_status == GameState.NOT_STARTED:
            self.soustitre_jeu_init.draw()
        elif self.current_status == GameState.ROUND_ACTIVE:
            self.soustitre_jeu_round.draw()
            attack_animation.idle_animations.draw()
        elif self.current_status == GameState.ROUND_DONE:
            self.soustitre_jeu_roundfinijoueur.draw()
        else:
            pass

        self.sprite_list.draw()

        # Call draw() on all your sprite lists below

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        if key == arcade.key.SPACE and self.current_status == GameState.NOT_STARTED:
            self.current_status = GameState.ROUND_ACTIVE
            print(f"{self.current_status}")

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        if self.current_status == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                #self.rock.set_texture(attack_animation.sprite_rock_attack)
                print("changed sprite to the attack variant")
                self.player_attack_type = attack_animation.AttackType.ROCK


def main():
    """ Main function """
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
