import pygame
from pygame.math import Vector2
import time

def main():
    #Variables
    screen_height, screen_width = 1920, 1080
    screen = pygame.display.set_mode((1920,1080))
    #Game loop

    #title
    pygame.display.set_caption('Hiking Game')

    #clean screen
    pygame.display.update()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        #infinte running loop
        pygame.display.update()
        

if __name__ == "__main__":
    main() #run Main sequence