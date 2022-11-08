import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota."""
    def __init__(self, ai_settings, screen):
        """Inicializa o alienígena e define sua posição inicial."""
        super().__init__()
        self.screen = screen
        self.ai_setings = ai_settings
        self.image = pygame.image.load('images/alien.bmp')  # Carrega a imagem do alienígena e define seu atributo rect
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width  # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)  # Armazena a posição exata do alienígena

    def blitme(self):
        """Desenha o alienígena em sua posição atual."""
        self.screen.blit(self.image, self.rect)
