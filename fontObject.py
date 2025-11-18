import pygame

pygame.init()

class Fonts:
    def __init__(self, size, color):
        self.text = ""
        self.size = size
        self.color = color
    
    def displayFont(self, screen, textbox):
        createFont = pygame.font.SysFont("Arial", self.size)

        textUpdated = self.text.replace("\r", "")

        renderFont = createFont.render(self.text, False, self.color)
        
        textbox_x = textbox.x_pos + 10
        textbox_y = textbox.y_pos + 5
        
        screen.blit(renderFont, (textbox_x, textbox_y))
    
    def fontHandling(self, event):
        if event.key == pygame.K_RETURN:
            self.text = ""

        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if len(self.text) < 22:
                self.text += event.unicode
