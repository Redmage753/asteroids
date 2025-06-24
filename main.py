import pygame
from constants import *
from circleshape import CircleShape
from player import Player

def main():
    print(f"Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
    dt=0 
    clock=pygame.time.Clock()

    x=SCREEN_WIDTH/2
    y=SCREEN_HEIGHT/2
    player_radius=PLAYER_RADIUS
    player=Player(x,y,player_radius)
    quit=False
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
    dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()
