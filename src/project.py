import pygame


def loading_artworks():
    artwork_1 = pygame.image.load('girl-with_a_pearl_earring.jpg')
    artwork_2 = pygame.image.load('a_sunday_afternoon.jpg')
    artwork_3 = pygame.image.load('the_kiss.jpg')
    artwork_4 = pygame.image.load('the_scream.jpg')
    artwork_5 = pygame.image.load('mona_lisa.jpg')
    artwork_6 = pygame.image.load('the_starry_night.jpg')
    
    artworks = { 'Room1': [(artwork_1), (artwork_2)],
                 'Room2': [(artwork_3), (artwork_4)],
                 'Room3': [(artwork_5), (artwork_6)]}
    return artworks


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