import sys

import pygame

class  AlieInvasion:
    """ This class manages the game assets and behavious """
    def __init__(self):
        """Initializes the game ad creates game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1500, 1000))
        pygame.display.set_caption("ALIEN INVASION")

    def run_game(self):
        """Starts the main loop for the game"""
        while True:
            """Watch for keyboard and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            """Make the most recently drawn screen visible"""
            pygame.display.flip()
if __name__ == '__main__':
    """Make a game instance and run the game"""

    ai = AlieInvasion()
    ai.run_game()