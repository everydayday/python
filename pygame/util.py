import pygame
import setting
import sys


def create():
    screen = pygame.display.set_mode((setting.WIDTH,setting.HEIGHT))
    screen_rect = screen.get_rect()
    clock = pygame.time.Clock()


    image = pygame.image.load(setting.SHIP_IMAGE_PATH)

    ship = pygame.Rect(500,500,100,100)
    ship_rect = image.get_rect()
    ship_rect.midbottom = screen_rect.midbottom
    return screen,screen_rect,clock,image,ship,ship_rect

def update_bullet(screen, bullets):
    for bullet in bullets:
        pygame.draw.rect(screen,setting.BULLET_COLOR,bullet)


def update_key(screen_rect, ship, ship_rect, create_bullet, bullets, event):
    if event.key == pygame.K_LEFT:                
        ship.left -= setting.SHIP_SPEED
    elif event.key == pygame.K_RIGHT:
        ship.left += setting.SHIP_SPEED
    elif event.key == pygame.K_UP:
        ship.top -= setting.SHIP_SPEED
    elif event.key == pygame.K_DOWN:
        if ship.top < screen_rect.height:
            ship.top += setting.SHIP_SPEED
    elif event.key == pygame.K_SPACE:
        b = create_bullet(ship)
        bullets.append(b)


def create_bullet(ship):
    bullet = pygame.Rect(0,0,5,50)
    bullet.midbottom = ship.midtop
    bullet.centerx = ship.centerx

    
    return bullet