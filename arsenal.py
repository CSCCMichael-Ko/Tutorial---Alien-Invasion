"""
Name: Michael Ko
File Name: arsenal.py
Program Name: Alien Shooter (Retro) - Track #2
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/15/2026
Purpose: Manages the laser(s) the ship fires. It creates, moves, draws, and removes them.
Starter Code: The code is based on the Alien Invasion (Drawing and firing lasers with sound) - 6 located on Blackboard
- https://courses.cscc.edu/ultra/courses/_238746_1/lti/launchFrame?toolHref=https:~2F~2Fcourses.cscc.edu~2Fwebapps~2Fblackboard~2Fexecute~2Fblti~2FlaunchLink%3Fcourse_id%3D_238746_1%26content_id%3D_28740812_1%26from_ultra%3Dtrue&toolTitle=Alien%20Invasion%20(%20Drawing%20and%20firing%20lasers%20with%20sound)%20-%206&contentId=_28740812_1&linkContentId=_28740812_1
- Watched Video(s) in Blackboard under Chapter 12: Alien Invasion Tutorials
Source(s) for Alien Assets: 
- https://www.vecteezy.com/vector-art/1391609-set-of-video-game-space-icons
- https://mixkit.co/free-sound-effects/space-shooter/
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING 

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """A class that manages the ships lasers."""

    def __init__(self, ai_game):
        """Creates empty arsenal."""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Moves every laser, then remove laser(s) that left the screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Deletes lasers that have moved past the top of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draws every laser in the arsenal."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullets(self):
        """Fires a new laser if under the limit. Return True if one fired."""
        if len(self.arsenal) < self.settings.bullets_allowed:
            self.arsenal.add(Bullet(self.ai_game))
            return True
        return False