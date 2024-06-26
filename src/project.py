import pygame

def main():
    pygame.init() 
    pygame.display.set_caption("Interactive Art Gallery")
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    artworks = load_artworks_from_file('artworks.txt')
    artworks_per_page = 2
    font = pygame.font.SysFont(None, 24)
    current_page = 0
    display_info = False
    info_index = None
    running = True
    max_pages = len(artworks) // artworks_per_page
    if len(artworks) % artworks_per_page != 0:
        max_pages += 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_page = max(current_page - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    current_page = min(current_page + 1, max_pages - 1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] < screen.get_width() / 2:
                    index = 0
                else:
                    index = 1
                display_info = True
                info_index = index
        if display_info:
            display_artwork_info(screen, font, artworks, current_page, info_index)
            pygame.display.flip()
            waiting_for_click = True
            while waiting_for_click:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        waiting_for_click = False 
            display_info = False
        display_artworks(screen, artworks, current_page * artworks_per_page, artworks_per_page, current_page)
    
    pygame.quit()


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

def display_artworks(screen, artworks, start_index, artworks_per_page, current_page):
    screen.fill((0,0,0))
    max_artwork_width = (screen.get_width() - (artworks_per_page + 1) * 20) // artworks_per_page
    max_artwork_height = (screen.get_height() - 3 * 30) // 2
    y_offset = (screen.get_height() - max_artwork_height) // 2 
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(f"Interactive Art Gallery - Room {current_page + 1}", True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = screen.get_width() // 2
    text_rect.y = 20
    screen.blit(text_surface, text_rect)
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
        render_button(screen, pygame.font.SysFont(None, 24), max_artwork_height, x_offset, y_offset)
    pygame.display.flip()

def render_button(screen, font, max_artwork_height, x_offset, y_offset):
    button_text = "Learn more about this artwork"
    button_text_surface = font.render(button_text, True, (255,255,255))
    button_text_rect = button_text_surface.get_rect()
    button_text_rect.topleft = (x_offset, y_offset + max_artwork_height + 10)
    screen.blit(button_text_surface, button_text_rect)

def display_artwork_info(screen, font, artworks, current_page, index):
    artworks_per_page = 2
    artwork_info = artworks[current_page * artworks_per_page + index]
    if len(artwork_info) >= 4:
        name, artist, description = artwork_info[1:4]
        info_lines = [
            f"Name: {name}",
            f"Artist: {artist}",
            f"Description: {description}"
        ]
        render_text(screen, font, info_lines)
    else:
        print("Invalid artwork information:", artwork_info)

def render_text(screen, font, lines):
    line_height = font.get_height() + 5
    box_width = 600
    box_height = len(lines) * line_height + 50
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.fill((255,255,255))
    y_offset = 10
    for line in lines:
        words = line.split()
        wrapped_lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= box_width - 20:
                current_line = test_line
            else:
                wrapped_lines.append(current_line)
                current_line = word + " "
        wrapped_lines.append(current_line)
        for wrapped_line in wrapped_lines:
            text_surface = font.render(wrapped_line, True, (0,0,0))
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, y_offset)
            box_surface.blit(text_surface, text_rect)
            y_offset += line_height
    screen.blit(box_surface, (screen.get_width() // 2 - box_width // 2, screen.get_height() // 2 - box_height // 2))
    pygame.display.flip()


if __name__ == "__main__":
    main()
