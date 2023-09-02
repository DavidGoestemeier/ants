from src.game_settings import AMOUNT_OF_ANTS, SCREEN_WIDTH, SCREEN_HEIGHT


class GameStatistics:

    def __init__(self):
        self.drawn = 0
        self.dt = 0
        self.fps = 0

    def update(self, dt):
        self.dt = dt
        self.drawn += 1
        if dt > 0 and self.drawn % 10 == 0:
            self.fps = round(1 / dt)
            self.drawn = 0

    def draw_statistics(self, screen, font, colonies):
        font_color = (0, 255, 0)
        # Define the text content
        text_content = [
            "Running Ant Simulation",
            "Started with: " + str(AMOUNT_OF_ANTS) + " Ants",
            #"Screen Size: " + str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT),
            "FPS: " + str(self.fps)
        ]
        for colony in colonies:
            text_content.append("Colony: " + str(colony.name) + " Ants: " + str(len(colony.ants)))

        # Render and blit each line of text onto the screen
        vertical_position = 10
        for line in text_content:
            text_surface = font.render(line, True, font_color)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, vertical_position)
            screen.blit(text_surface, text_rect)
            vertical_position += text_surface.get_height() + 5  # Add some spacing
