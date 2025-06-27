import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(
                x,
                y,
                radius,
                )
        self.rotation=0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

#    def split(self, dt):
#        self.kill()
#        if self.radius <= ASTEROID_MIN_RADIUS:
#            return
#        else:
#            split_angle_pos = random.uniform(20,50)
#            split_angle_neg = random.uniform(20,50)*-1
#            #print(f"{split_asteroid1}")
#            #print(f"{split_angle_neg}")
#            #print(f"{split_angle_pos}")
#            new_radius = self.radius - ASTEROID_MIN_RADIUS
#            split_asteroid1 = Asteroid(self.position.x,self.position.y,new_radius)
#            #split_asteroid1.velocity = (pygame.Vector2(0,1).rotate(split_asteroid1.rotation) + split_angle_pos) * 1.2 
#            split_asteroid1.velocity = self.velocity.rotate(split_angle_pos) * 1.2
#            #split_asteroid1.velocity = dt * 1.2
#            split_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
#            #split_asteroid2.rotation += (split_angle_neg)
#            split_asteroid2.velocity = self.velocity.rotate(split_angle_neg) * 1.2
#            #split_asteroid2.velocity = (pygame.Vector2(0,1).rotate(split_asteroid2.rotation) + split_angle_neg) * 1.2
#            #print(type(split_asteroid1.position), type(split_asteroid1.velocity), type(dt))
##            #print(type(split_asteroid2.position), type(split_asteroid2.velocity), type(dt))
    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            
            Asteroid(self.position.x,self.position.y,(self.radius-ASTEROID_MIN_RADIUS)).velocity = self.velocity.rotate(random.uniform(20,50))
            asteroid = Asteroid(self.position.x,self.position.y,(self.radius-ASTEROID_MIN_RADIUS))
            asteroid.velocity = self.velocity.rotate(random.uniform(20,50)*-1)
