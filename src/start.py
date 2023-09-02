from os import environ

import collision_detection
from src.game_statistics import GameStatistics

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
# noqa: E402
import pygame
from ants.colony import Colony
from game_settings import SCREEN_WIDTH, SCREEN_HEIGHT, AMOUNT_OF_ANTS, ANT_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ants")
font = pygame.font.Font(None, 24)  # You can replace 'None' with a font file path if needed

clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
running_for = 0
running = True
dt = 0
drawn = 0

text_x = 100
text_y = 200

green = (0, 255, 0)
red = (255, 0, 0)

# colony
colony = Colony("red", int(AMOUNT_OF_ANTS / 2), ANT_SIZE, red)
colony_2 = Colony("green", int(AMOUNT_OF_ANTS / 2), ANT_SIZE, green)

game_statistics = GameStatistics()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    colony.update()
    colony_2.update()




    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw colony / find out if this is truly 60fps
    colony.draw(screen)
    colony_2.draw(screen)
    # end update

    collision_detection.fight(colony, colony_2)
    # draw statistics
    game_statistics.update(dt)
    game_statistics.draw_statistics(screen, font, [colony, colony_2])



    # END OF DRAWING
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
pygame.quit()
