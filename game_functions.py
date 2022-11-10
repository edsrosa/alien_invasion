import sys
import pygame
from bullet import Bullet
from alien import Alien


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
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Redesenha todos os projéteis atrás da espaçonave e dos alienígenas."""
    screen.fill(ai_settings.bg_color)  # Redesenha a tela a cada passagem pelo laço
    for bullet in bullets.sprites():
        bullet.draw_bullet()  # Redesenha todos os projéteis atras da espaçonave e dos alienígenas
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()  # Deixa a tela mais recente visível


def update_bullets(bullets):
    """Atualiza a posição dos projéteis e se livra dos projétis antigos."""
    bullets.update()  # Atualiza as posições dos projéteis
    for bullet in bullets.copy():  # Livra-se dos projéteis que desapareceram
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determina o número de alienígenas que cabem em uma linha."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina  número de linhas com alienígenas que cabem na tela."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Cria um alienígena e o posiciona na linha."""
    alien = Alien(ai_settings, screen)  # Cria uma alienígena e o posiciona na linha
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienígenas."""
    alien = Alien(ai_settings, screen)  # Cria um alienígena e calcula o número de alienígenas em uma linha
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):  # Cria uma frota de alienígenas
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienígena alcançou uma borda."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda a sua direção."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """Verifica se a frota está em uma das bordas e então atualiza as posições de todos os alienígenas da frota."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
