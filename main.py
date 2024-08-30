import pygame
import constants as const

def main():
    #print("Starting asteroids!")
    #print(f'Screen width: {const.SCREEN_WIDTH}')
    #print(f'Screen height: {const.SCREEN_HEIGHT}')
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black", rect=None, special_flags=0)
        pygame.display.flip()

if __name__ == "__main__":
    main()