import pygame, sys
from button import Button
import subprocess


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.jpg")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def game1():
    subprocess.run(["python", "RedLightGreenLight.py"])
    
def game2():
    subprocess.run(["python", "dalgona.py"])

def game3():
    subprocess.run(["python", "HOPSCOTCH.py"])



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        GAME1_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 230),
                            text_input="RGLIGHTS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        GAME2_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 380),
                            text_input="DALGONA", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        GAME3_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 530),
                            text_input="HOPSCOTCH", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 650),
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [GAME1_BUTTON, GAME2_BUTTON, GAME3_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game1()
                if GAME2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game2()
                if GAME3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game3()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()