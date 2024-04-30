import pygame

def load_artworks_from_file(filename):
    artworks = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 4:
                image_path = parts[0].strip()
                name = parts[1].strip()
                artist = parts[2].strip()
                description = parts[3].strip()
                artworks.append((image_path, name, artist, description))
    return artworks


def display_artworks(screen, artworks, start_index, current_room):
    screen.fill((0,0,0))
    y_offset = 50
    for artwork in artworks[start_index:start_index+2]:
        image_path, title, artist, description = artwork
        artwork_image = pygame.image.load(image_path)
        screen.blit(artwork_image, (50,y_offset))
        y_offset += artwork_image.get_height() + 20
        # need to add other things on screen to display
    pygame.display.flip()

def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    artworks = load_artworks_from_file('artworks.txt')
    current_room = 'Room 1'
    artworks_per_page = 2
    current_page = 0
    running = True
    while running:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_page = max(current_page - 1, 0)
                    elif event.key == pygame.K_RIGHT:
                        current_page = min(current_page + 1, len(artworks) // artworks_per_page )
            display_artworks(screen, artworks, current_room * artworks_per_page, current_room)

    pygame.quit()



if __name__ == "__main__":
    main()