import pygame

class Artwork():
    
    def __init__(self, image_path, title, artist, description):
        self.image = pygame.image.load(image_path)
        self.title = title
        self.artist = artist
        self.description = description
        


def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    pygame.quit()



if __name__ == "__main__":
    main()