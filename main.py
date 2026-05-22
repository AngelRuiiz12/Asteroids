import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        log_state()  # Log para que Boot.dev pueda comprobar que el programa funciona.

        # Para manejar eventos
        for event in pygame.event.get():
            # Evento para cerrar el programa con la X
            if event.type == pygame.QUIT:
                return

        # Con Screen.fill("black") hacemos que la pantalla se rellene de color negro.
        screen.fill("black")

        # display.flip() sirve para refrescar la pantalla.
        # Debe ir siempre al final de loop
        pygame.display.flip()

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
