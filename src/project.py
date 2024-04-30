import pygame


def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    pygame.quit()



if __name__ == "__main__":
    main()