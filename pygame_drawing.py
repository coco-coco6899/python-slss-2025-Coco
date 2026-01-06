# pygame drawing
# Author: Coco
# Date: Jan 5

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (105, 190, 40)  # rgb numbers
    BLUE = (0, 191, 255)
    GREY = (128, 128, 128)
    ORANGE = (255, 183, 0)
    YELLOW = (255, 243, 0)
    PURPLE = (195, 115, 255)

    # CONSTANTS
    WIDTH = 1920
    HEIGHT = 1080
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Pretty drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()
    pi = 3.1415

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)  # background
        # draw a rectangle in the middle of the screen
        # and make it red

        pygame.draw.rect(screen, RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))
        pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2), 50)
        pygame.draw.arc(screen, RED, [420, 150, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, ORANGE, [417, 147, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, YELLOW, [414, 144, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, GREEN, [411, 141, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, GREEN, [411, 141, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, BLUE, [408, 138, 300, 250], 3 * pi / 2, 2 * pi, 2)
        pygame.draw.arc(screen, PURPLE, [406, 136, 300, 250], 3 * pi / 2, 2 * pi, 2)

        # draw 7 purple line from the top middle right of the screen
        # repeats by translating down 75 px
        for offset in range(7):
            pygame.draw.line(
                screen,
                (228, 45, 216),
                (WIDTH / 2 + 20, 20 + offset * 75),
                (WIDTH - 20, HEIGHT / 2 - 20 + offset * 75),
            )

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
