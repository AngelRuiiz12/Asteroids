import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()  # Log para que Boot.dev pueda comprobar que el programa funciona.

        # Para manejar eventos
        for event in pygame.event.get():
            # Evento para cerrar el programa con la X
            if event.type == pygame.QUIT:
                return

        # Con Screen.fill("black") hacemos que la pantalla se rellene de color negro.
        screen.fill("black")

        player.update(dt)
        # Dibujamos el triangulo del player
        player.draw(screen)

        dt = clock.tick(60) / 1000
        # display.flip() sirve para refrescar la pantalla.
        # Debe ir siempre al final de loop
        pygame.display.flip()

    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
