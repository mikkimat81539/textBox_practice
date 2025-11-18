import pygame
from textBoxObject import TextBox
from fontObject import Fonts

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))
pygame.display.set_caption("Textbox")

# TextBox
textbox = TextBox(50, 100, 400, 50, "black")

# FONTS
display_Font = Fonts(30, "black")

# Screen Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            display_Font.fontHandling(event)
        
    screen.fill("white")

    # RENDER CODE HERE
    textbox.draw_rect(screen)
    display_Font.displayFont(screen, textbox)

    pygame.display.flip()

pygame.quit()
