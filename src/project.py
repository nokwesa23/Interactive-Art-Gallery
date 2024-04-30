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


def display_artworks(screen, artworks, start_index, artworks_per_page):
    screen.fill((0,0,0))
    max_artwork_width = (screen.get_width() - (artworks_per_page + 1) * 20) // artworks_per_page
    max_artwork_height = (screen.get_height() - 3 * 30) // 2
    y_offset = 50
    for i, artwork in enumerate(artworks[start_index:start_index + artworks_per_page]):
        image_path, title, artist, description = artwork
        artwork_image = pygame.image.load(image_path)
        artwork_resized_image = pygame.transform.scale(artwork_image, (max_artwork_width, max_artwork_height))
        x_offset = (i * (max_artwork_width + 20)) + 20
        if i >= artworks_per_page // 2:
            y_offset += max_artwork_height + 20
        screen.blit(artwork_resized_image, (x_offset,y_offset))

        # need to add other things on screen to display
    pygame.display.flip()

def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    artworks = load_artworks_from_file('artworks.txt')
    # current_room = 'Room 1'
    artworks_per_page = 2
    current_page = 0
    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        current_page = max(current_page - 1, 0)
                    elif event.key == pygame.K_RIGHT:
                        current_page = min(current_page + 1, len(artworks) // artworks_per_page )
        display_artworks(screen, artworks, current_page * artworks_per_page, artworks_per_page )

    pygame.quit()



if __name__ == "__main__":
    main()