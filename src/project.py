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
    y_offset = (screen.get_height() - max_artwork_height) // 2 
    for i, artwork in enumerate(artworks[start_index:start_index + artworks_per_page]):
        image_path, title, artist, description = artwork
        artwork_image = pygame.image.load(image_path)
        artwork_aspect_ratio = artwork_image.get_width() / artwork_image.get_height()
        if artwork_aspect_ratio >1:
            new_width = max_artwork_width
            new_height = int(max_artwork_height + artwork_aspect_ratio)
        else:
            new_height = max_artwork_height
            new_width = int (max_artwork_height * artwork_aspect_ratio)
        artwork_image = pygame.transform.scale(artwork_image, (new_width,new_height))
        x_offset = max_artwork_width * i - (new_width - max_artwork_width) // 2
        screen.blit(artwork_image, (x_offset,y_offset))
        render_button(screen, max_artwork_height, x_offset, y_offset)

        # need to add other things on screen to display
    pygame.display.flip()

def render_button(screen, font, max_artwork_height, x_offset, y_offset):
    button_text = "Learn more about this artwork"
    button_text_surface = font.render(button_text, True, (255,255,255))
    button_text_rect = button_text_surface.get_rect()
    button_text_rect.topleft = (x_offset, y_offset + max_artwork_height + 10)
    screen.blit(button_text_surface, button_text_rect)

def display_artwork_info(artworks, current_page, index):
    artworks_per_page = 2
    name, artist, description = artworks[current_page * artworks_per_page + index]
    print(f"Name: {name}\nArtist: {artist}\nDescription: {description}")

def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    artworks = load_artworks_from_file('artworks.txt')
    # current_room = 'Room 1'
    artworks_per_page = 2
    current_page = 0
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render("Learn more about the artwork", True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (50,50)
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