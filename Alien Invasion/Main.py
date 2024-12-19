import sys, pygame
import pygame.font
from pygame.sprite import Sprite
from time import sleep


class Scoreboard:

    """A class to report scoring information."""

    def __init__(self, ai_game):

        """Initialize scorekeeping attributes."""

        self.screen = ai_game.screen

        self.screen_rect = self.screen.get_rect()

        self.settings = ai_game.settings

        self.stats = ai_game.stats

        # Font settings for scoring information.

        self.text_color = (255,128,1)

        self.font = pygame.font.SysFont('timesnewroman', 32,1,0)
        # Prepare the initial score image.

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        
    def prep_level(self):

        """Turn the level into a rendered image."""

        level_str = str(self.stats.level)
        level_str = f'Level: {level_str}'
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.

        self.level_rect = self.level_image.get_rect()

        self.level_rect.right = self.score_rect.right

        self.level_rect.top = self.score_rect.bottom + 10

        
    def prep_high_score(self):

        """Turn the high score into a rendered image."""

        high_score = round(self.stats.high_score, -1)

        high_score_str = f"High score: {high_score:,}"

        self.high_score_image = self.font.render(high_score_str, True,
self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.

        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.left = self.screen_rect.left+20
        self.high_score_rect.top = self.score_rect.top       
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)

        score_str = f"Your score: {rounded_score:,}"

        self.score_image = self.font.render(score_str, True,self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.

        self.score_rect = self.score_image.get_rect()

        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 40

        
    def show_score(self):

        """Draw score to the screen."""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
    def check_high_score(self):

        """Check to see if there's a new high score."""

        if self.stats.score > self.stats.high_score:

            self.stats.high_score = self.stats.score

            self.prep_high_score()


class Button:

    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):

        """Initialize button attributes."""

        self.screen = ai_game.screen

        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.

        self.width, self.height = 200, 100
        self.button_color = (190, 100, 0)

        self.text_color = (0, 0, 140)

        self.font = pygame.font.SysFont(None, 94,1,0)

        # Build the button's rect object and center it.

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.

        self.prep_msg(msg)
        
    def prep_msg(self, msg):

        """Turn msg into a rendered image and center text on the button."""

        self.msg_image = self.font.render(msg, True, self.text_color,
self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()

        self.msg_image_rect.center = self.rect.center
    def draw_button(self):

        """Draw blank button and then draw message."""

        self.screen.fill(self.button_color, self.rect)

        self.screen.blit(self.msg_image, self.msg_image_rect)

class GameStats:

    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):

        """Initialize statistics."""

        self.settings = ai_game.settings

        self.reset_stats()
        # High score should never be reset.

        self.high_score = 0
        self.level = 1


    def reset_stats(self):

        """Initialize statistics that can change during the game."""

        self.ships_left = self.settings.ship_limit
        self.score = 0


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('alien.png')
        self.image = pygame.transform.scale(self.image,(60,60))
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.settings = ai_game.settings

        
    def check_edges(self):

        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()

        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    
    def update(self):

        """Move the alien to the right or left."""

        self.x += self.settings.alien_speed * self.settings.fleet_direction

        self.rect.x = self.x



class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings
        self.screen_width = 700
        self.screen_height = 1200
        self.bg_color = ('black')
        
        # Ship settings
        self.ship_speed = 15
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 20
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (255,150,0)
        self.bullets_allowed = 20
        
        # Alien settings

        self.alien_speed = 10
        self.fleet_drop_speed = 50

        # How quickly the game speeds up

        self.speedup_scale = 3
        # How quickly the alien point values increase

        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 15

        self.bullet_speed = 20
        self.alien_speed = 10
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.

        self.fleet_direction = 1
        # Scoring settings

        self.alien_points = 5

    def increase_speed(self):

        """Increase speed settings."""

        self.ship_speed += self.speedup_scale

        self.bullet_speed += self.speedup_scale

        self.alien_speed += self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('jet.png')
        self.image = pygame.transform.scale(self.image,(150,150))
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = (360,1300)       
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
            
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):

        """Center the ship on the screen."""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        bg = pygame.image.load('bg.png')
        self.bg = pygame.transform.scale(bg,(self.settings.screen_width,self.settings.screen_height))
        # Create an instance to store game statistics.

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()
        # Start Alien Invasion in an inactive state.

        self.game_active = False
        pygame.mouse.set_visible(True)
 
        # Make the Play button.

        self.play_button = Button(self, "Play")
      
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()
            if self.game_active:
                self.ship.update()
                self.update_bullets()
                self.update_aliens()
    
            self.update_screen()
            pygame.display.flip()
            self.clock.tick(30)
            
    def check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(pygame)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.down_events(event)
                mouse_pos = event.pos
                self.check_play_button(mouse_pos)
                
            if event.type == pygame.MOUSEBUTTONUP:
                self.up_events(event)
        
    def check_play_button(self, mouse_pos):

        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            # Reset the game statistics.
            # Reset the game settings.

            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()

            self.game_active = True
            # Get rid of any remaining bullets and aliens.

            self.bullets.empty()

            self.aliens.empty()
    
            # Create a new fleet and center the ship.

            self.create_fleet()

            self.ship.center_ship()
            # Hide the mouse cursor.

            pygame.mouse.set_visible(False)
        
    def down_events(self,event):
        x,y = event.pos
        if y > 1000 and x > 500:
            # Move the ship to the right.
            self.ship.moving_right = True
        if y > 1000 and x < 250:
            # Move the ship to the right.
            self.ship.moving_left = True
        if y < 50 and x > 650:
            sys.exit(pygame)
        if y > 1000:
            if x > 150 and x < 550:
                self.fire_bullet()
            
    def up_events(self,event):
        x,y = event.pos
        if y > 1000 and x > 500:
            # Move the ship to the right.
            self.ship.moving_right = False
        if y > 1000 and x < 250:
            # Move the ship to the right.
            self.ship.moving_left = False
            
    def fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                
    def update_screen(self):
        self.screen.blit(self.bg,(0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Draw the score information.

        self.sb.show_score()
        # Draw the play button if the game is inactive.
        if self.game_active == False:

            self.play_button.draw_button()
        
    
    def update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()            
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        self.check_bullet_alien_collisions()

        
    def check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""

        # Remove any bullets and aliens that have collided.

        collisions = pygame.sprite.groupcollide(
self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():

                self.stats.score += self.settings.alien_points * len(aliens)

            self.stats.score += self.settings.alien_points

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.check_high_score()


        
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self.create_fleet()
            self.settings.increase_speed()
            # Increase level.

            self.stats.level += 1

            self.sb.prep_level()

    
    def create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 12 * alien_height):
            while current_x < (self.settings.screen_width - 1 * alien_width):
                self.create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Finished a row; reset x value, and increment y value.

            current_x = alien_width

            current_y += 2 * alien_height

            
    def create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position

        self.aliens.add(new_alien)
        
    def update_aliens(self):

        """Update the positions of all aliens in the fleet."""

        """Check if the fleet is at an edge, then update positions."""

        self.check_fleet_edges()

        self.aliens.update()
        # Look for alien-ship collisions.

        if pygame.sprite.spritecollideany(self.ship, self.aliens):

            self.ship_hit()
        # Look for aliens hitting the bottom of the screen.

        self.check_aliens_bottom()
    
    def check_fleet_edges(self):

        """Respond appropriately if any aliens have reached an edge."""

        for alien in self.aliens.sprites():

            if alien.check_edges():

                self.change_fleet_direction()

                break

             
    def change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""

        for alien in self.aliens.sprites():

            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1
    
    def ship_hit(self):

        """Respond to the ship being hit by an alien."""

        if self.stats.ships_left > 0:

            # Decrement ships_left.

            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.

            self.bullets.empty()

            self.aliens.empty()

            # Create a new fleet and center the ship.

            self.create_fleet()

            self.ship.center_ship()
            # Pause.
            sleep(0.5)
            
        else:

            self.game_active = False

    
    def check_aliens_bottom(self):

        """Check if any aliens have reached the bottom of the screen."""

        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:

                # Treat this the same as if the ship got hit.

                self.ship_hit()

                break

    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()