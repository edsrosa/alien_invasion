import sys
import pygame
from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não foi alcançado."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)  # Cria um novo projeto e o adiciona ao grupo de projéteis
        bullets.add(new_bullet)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responde a pressionamentos de tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responde a solturas da tecla."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de pressionamento de teclas e de mouse."""
    for event in pygame.event.get():  # Observa eventos do teclado e do mouse
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza as imagens nas tela e alterna para a nova tela."""
    screen.fill(ai_settings.bg_color)  # Redesenha a tela a cada passagem pelo laço
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # Redesenha todos os projéteis atras da espaçonave e dos alienígenas
    ship.blitme()
    pygame.display.flip()  # Deixa a tela mais recente visível


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projétis antigos."""
    bullets.update()  # Atualiza as posições dos projéteis
    for bullet in bullets.copy():  # Livra-se dos projéteis que desapareceram
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
