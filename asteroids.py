import pygame
import constants
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        new_rotation = pygame.Vector2.rotate(self.velocity, new_angle)
        new_rotation_2 = pygame.Vector2.rotate(self.velocity, -new_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = new_rotation * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_rotation_2 * 1.2
       
        
        