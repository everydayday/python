
import pygame
import sys
import setting
from alien import Alien
from util import update_bullet, create, update_key, create_bullet

pygame.init()


screen, screen_rect, clock, image, ship, ship_rect = create()


bullet = create_bullet(ship_rect)


bullets = []
#bullet = create_bullet(ship_rect)
#bullets.append(bullet)




while True:
    pygame.draw.rect(screen,setting.BULLET_COLOR,bullet )
    
    # Process player inputs.
    for event in pygame.event.get(): # 키보드, 마우스
        if event.type == pygame.QUIT or event.type == pygame.K_q :
            pygame.quit()
            sys.exit()
            raise SystemExit # exception 발생 시키는 것
        elif event.type == pygame.KEYDOWN:
            update_key(screen_rect, ship, ship_rect, create_bullet, bullets, event)

    screen.fill("light green")  # Fill the display with a solid color

    # Render the graphics here.
    
    
    new_bullets = []
    for bullet in bullets:
        if screen_rect.top < bullet.top:
            
            bullet.top -= setting.BULLET_SPEED
            new_bullets.append(bullet)
        else :
            bullets.remove(bullet)

    alien = Alien(image)
    
    
        

    screen.blit(alien.image,alien)
    screen.blit(image,ship)

    update_bullet(screen, bullets)
    
    

    pygame.display.flip()  # Refresh on-screen display
    
    clock.tick(setting.FRAME_PER_SECOND)         # wait until next frame (at 60 FPS)






