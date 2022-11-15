class GameStats:
    """Armazena dados estatísticos da Invasão Alienígena."""
    def __init__(self, ai_setting):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_setting

        self.reset_stats()
        # Inicia a Invasão Alienígena em um estado inativo
        self.game_active = False

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
