import sys

import pygame

class  AlieInvasion:
    """ This class manages the game assets and behavious """
    def __init__(self):
        """Initializes the game ad creates game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ALIEN INVASION")

        # set the background color
        self.bg_color = (210, 235, 240)

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            """Watch for keyboard and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the screen during each pass through the loop
            self.screen.fill(self.bg_color)

            """Make the most recently drawn screen visible"""
            pygame.display.flip()
            self.clock.tick(75)
if __name__ == '__main__':
    """Make a game instance and run the game"""

    ai = AlieInvasion()
    ai.run_game()