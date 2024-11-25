import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

import sys

def main():
  print("Starting asteroids!\nScreen width: 1280\nScreen height: 720")
  pygame.init()

  # Instantiating game objects
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()

  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable

  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  asteroidField = AsteroidField()

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill((0,0,0))
    for sprite in updatable:
      sprite.update(dt)
    for sprite in drawable:
      sprite.draw(screen)

    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()