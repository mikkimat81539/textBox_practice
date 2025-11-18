import pygame

pygame.init()

class Fonts:
    def __init__(self, size, color):
        self.size = size
        self.color = str(color)
        self.text = ""


    def fonts(self, screen, textBox):
        createFonts = pygame.font.SysFont("Arial", self.size)
        textUpdated = self.text.replace("\r", "")
        renderFont = createFonts.render(textUpdated, False, self.color)

        text_x = textBox.x_pos + 10
        text_y = textBox.y_pos + 5

        screen.blit(renderFont, (text_x, text_y))
    
    def fontHandling(self, event):
        if event.key == pygame.K_RETURN:
            self.text = ""

        if event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]

        else:
            if len(self.text) < 12:
                self.text += event.unicode

# ENTER box is still there just hidden