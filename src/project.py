import pygame

class Artworks():
    
    def __init__(self, image_path, title, artist, description):
        self.image = pygame.image.load(image_path)
        self.title = title
        self.artist = artist
        self.description = description
        
def load_artworks_from_text(filename):
    artworks = []
    with open(filename, 'r') as file:
        for line in file:
            image_path, title, artist, description = line.strip().split(',')
            image = pygame.image.load(image_path)
            artworks.append(Artworks(image,title,artist,description))
    return artworks


def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    running = True
    artworks = load_artworks_from_text('artworks.txt')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
    pygame.quit()



if __name__ == "__main__":
    main()