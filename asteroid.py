from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS 
import pygame, random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(20.0, 50.0)
    velocity1 = pygame.Vector2(self.velocity.x, self.velocity.y)
    velocity1 = velocity1.rotate(angle)
    velocity2 = pygame.Vector2(self.velocity.x, self.velocity.y)
    velocity2 = velocity2.rotate(-angle)
    asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    asteroid1.velocity += velocity1 * 1.2
    asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    asteroid2.velocity += velocity2 * 1.2