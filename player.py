import pygame
from circleshape import * #CircleShape
from constants import * #PLAYER_TURN_SPEED, PLAYER_SPEED
from shot import *
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(
            x,
            y,
            radius,
        )
        self.rotation=0
        self.timer=0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation+=(PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
            # move forward
        if keys[pygame.K_a]:
            # turn left
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt) 
            # move backward
        if keys[pygame.K_d]:
            # turn right
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return 
        else:
            shot = Shot(self.position[0], self.position[1], SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
            self.timer = PLAYER_SHOOT_COOLDOWN
        
    # Player.containers = (group_a, group_b)
    # Player.containers = (group_updatable, group_drawable)
