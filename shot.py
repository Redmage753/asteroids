import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
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
#        print(f"circle type: ${type(self.position)}, ${type(self.velocity)}, ${type(dt)}")
        self.position += (self.velocity * dt)

