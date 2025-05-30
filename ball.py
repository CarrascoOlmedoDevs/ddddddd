import pygame

class Pelota:
    def __init__(self, x, y, radio, color):
        self.posicion = pygame.math.Vector2(x, y)
        self.velocidad = pygame.math.Vector2(0, 0) # Velocidad inicial puede ser cero
        self.radio = radio
        self.color = color

    def update(self, dt):
        # Este es un método placeholder.
        # La lógica real de actualización (ej. movimiento, colisiones) iría aquí.
        pass

    def draw(self, screen):
        # Este es un método placeholder.
        # La lógica real de dibujo (ej. pygame.draw.circle) iría aquí.
        pass