import pygame.image


class Ship:

    def __init__(self, ai_settings, screen):
        """Inicializa a espaçonave e define sua posição inicial."""
        self.screen = screen
        self.ai_settings = ai_settings
        self. image = pygame.image.load('images/ship.bmp')  # Carrega a imagem da espaçonave e obtém o rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False  # Flag de movimento
        self.moving_left = False  # Flag de movimento

    def update(self):
        """Atualiza a posição da espaçonave de acordo com as flags de movimento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Atualiza a posição da espaçoanve e
            self.center += self.ai_settings.ship_speed_factor  # não o retângulo.
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center  # Atualiza o objeto rect de acordo com self.center

    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)
