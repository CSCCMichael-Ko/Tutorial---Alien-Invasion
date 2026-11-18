"""
Name: Michael Ko
File Name: settings.py
Program Name: Alien Shooter (Retro) - Track #2
Class: CSCI-1511-W03L (Python Programming)
Professor: Travis Burke
Date: 11/15/2026
Purpose: Stores game settings (screen, ship, laser, sound, and alien) and pathlib to the images/sound
Starter Code: Based on the Textbook
- Watched Video(s) in Blackboard under Chapter 12: Alien Invasion Tutorials
Source(s) for Alien Assets: 
- https://www.vecteezy.com/vector-art/1391609-set-of-video-game-space-icons
- https://mixkit.co/free-sound-effects/space-shooter/
"""

from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3
        self.ship_file = Path.cwd() / 'images' / 'spaceship.png'


        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 45
        self.bullets_allowed = 3
        self.bullet_file = Path.cwd() / 'images' / 'laser.png'
        self.laser_sound_file = Path.cwd() / 'sound' / 'laser_fire.wav'

        # Alien settings 
        self.fleet_drop_speed = 10
        self.alien_file = Path.cwd() / 'images'  'alien0.png'

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # Background Image
        self.bg_file = Path(__file__).parent / 'images' / 'background.png'

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 0.7

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)