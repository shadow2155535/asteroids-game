from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width = 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_velocity1 = self.velocity.rotate(angle) * 2.8
            new_velocity2 = self.velocity.rotate(angle * -1) * 2.8
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)

            ast1.velocity = new_velocity1
            ast2.velocity = new_velocity2 