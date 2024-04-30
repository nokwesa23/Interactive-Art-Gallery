import pygame

def load_artworks_from_file(filename):
    artworks = []
    with open(filename, 'r') as file:
        for line in file:
            image_path, title, artist, description = line.strip().split(',')
            artworks.append((image_path, title, artist, description))
    return 


def display_artworks(screen, artworks, current_room):
    return

def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    artworks = load_artworks_from_file('artworks.txt')
    current_room = 'Room 1'
    running = True
    while running:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            display_artworks(screen, artworks, current_room)

    pygame.quit()



if __name__ == "__main__":
    main()