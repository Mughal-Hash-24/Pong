import pygame
import math

pygame.init()

width, height = 900, 600

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vel, angle, radius, color):
        super().__init__()
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)  # Create a surface with alpha channel
        pygame.draw.circle(self.image, color, (radius, radius), radius)  # Draw a circle on the surface
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.vel = vel
        self.angle = angle
        self.radius = radius
        

    # Rest of the code...


    def update(self):
        self.rect.x += self.vel * math.cos(self.angle)
        self.rect.y += self.vel * math.sin(self.angle)

        if self.rect.colliderect(pad1.rect):
            self.angle = math.pi - self.angle

        if self.rect.colliderect(pad2.rect):
            self.angle = math.pi - self.angle

    def reflect_horizontal(self):

        self.angle = math.pi - self.angle

    def reflect_vertical(self):
        self.angle = -self.angle


class Pad1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 120))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.midleft = (5, height // 2)  # Adjust the x-coordinate as needed
        self.vel = 8

    def move_up(self):
        self.rect.y -= self.vel

    def move_down(self):
        self.rect.y += self.vel


class Pad2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 120))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = width -25
        self.rect.y = height//2 - 60 # Adjust the x-coordinate as needed
        self.vel = 8

    def move_up(self):
        self.rect.y -= self.vel

    def move_down(self):
        self.rect.y += self.vel

all_sprites = pygame.sprite.Group()

ball = Ball(400, 300, 6, math.pi/6, 10, (255,0,0))
pad1 = Pad1()
pad2 = Pad2()

all_sprites.add(ball, pad1, pad2)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ball Reflection")

running = True
while running:
    pygame.time.delay(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and pad2.rect.y >0:
        pad2.rect.y -= 5

    if keys[pygame.K_DOWN] and pad2.rect.y < height - 120:
        pad2.rect.y += 5
    
    if keys[pygame.K_w] and pad1.rect.y >0:
        pad1.rect.y -= 5

    if keys[pygame.K_s] and pad1.rect.y < height - 120:
        pad1.rect.y += 5

    if ball.rect.center[0] <= 10 or ball.rect.center[0] >= width - 10:
        running = False

    if ball.rect.center[1] <= 10 or ball.rect.center[1] >= height - 10:
        ball.angle = -ball.angle

    screen.fill((255, 255, 255))

    all_sprites.draw(screen)

    all_sprites.update()

    pygame.display.flip()

pygame.quit()
