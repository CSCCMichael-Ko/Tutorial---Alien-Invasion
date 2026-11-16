"""
Name: Michael Ko
File Name: alien.py
Program Name: Alien Shooter (Retro) - Track #2
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/15/2026
Purpose: Defines the Alien class. Alien(s) move side to side while moving down.
Starter Code: Based on Textbook
- Watched Video(s) in Blackboard under Chapter 12: Alien Invasion Tutorials
Source(s) for Alien Assets: 
- https://www.vecteezy.com/vector-art/1391609-set-of-video-game-space-icons
- https://mixkit.co/free-sound-effects/space-shooter/
"""

import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(self.settings.alien_file)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x