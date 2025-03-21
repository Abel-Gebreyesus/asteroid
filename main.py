import pygame 
from constants import *

def main():
  print('Starting Asteroids!')
  
  dt = 0.0
  clock = pygame.time.Clock()

  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(BLACK)
    dt = clock.tick(60) / 1000
    pygame.display.flip()
    
if __name__ == '__main__':
  main()