import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot 

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
    # Create Groups
    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)
    
    group_asteroids = pygame.sprite.Group()
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)

    AsteroidField.containers=(group_updatable)

    group_shots = pygame.sprite.Group()
    Shot.containers = (group_shots, group_updatable, group_drawable)



    # Initialize player object
    player_radius=PLAYER_RADIUS
    player=Player(x,y,player_radius)
    asteroid_field=AsteroidField()
    quit=False
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.update(dt)
        #player.draw(screen)
        group_updatable.update(dt)
        for asteroid in group_asteroids:
            if player.collision_check(asteroid):
                print(f"Game Over!")
                return quit==True
        for drawable in group_drawable:
            drawable.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()
