import pygame


TEXT_GROUP = pygame.sprite.RenderUpdates()

class RenderText(pygame.sprite.Sprite):

    pos = None
    pos_rel = None

    def __init__(self, screen, text='text', pos=(0, 0), pos_rel=(1, 3),
                 font=None, size=20, color=(255, 255, 255), antialias=True):

        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.color = color
        self.text = text
        self.pos = pos
        self.pos_rel = pos_rel
        self.screen = screen
        self.antialias = antialias

        TEXT_GROUP.add(self)

        self.rerender()

    def update(self):
        pass

    def calculate_position(self):
        return (
            self.pos_rel[0] * (self.screen.get_size()[0] / 2 - self.rect.width / 2)
            + (1 - 2 * (self.pos_rel[0] / 2)) * self.pos[0],
            self.pos_rel[1] * (self.screen.get_size()[1] / 2 - self.rect.height / 2)
            + (1 - 2 * (self.pos_rel[1] / 2)) * self.pos[1],
        )

    def print_text(self, text, pos=None):
        self.text = text
        if pos: self.pos = pos
        self.rerender()

    def rerender(self):
        self.image = self.font.render(self.text, self.antialias, self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.calculate_position()
