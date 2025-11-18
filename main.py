import pygame
from text_box import TextBox
from fontObject import Fonts

pygame.init()

# SCREEN
screen = pygame.display.set_mode((500, 250))

# Textbox
textBox = TextBox(100, 50, 300, 50, "black")

# FONTS
displayFonts = Fonts(40, "black")
# Screen Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            displayFonts.fontHandling(event)

    screen.fill("white")

    # RENDER YOUR GAME HERE
    textBox.drawRect(screen)
    displayFonts.fonts(screen, textBox)

    pygame.display.update()

    pygame.display.flip()

pygame.quit()
