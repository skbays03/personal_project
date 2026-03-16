import pygame
from constants import *
from mainmenu import MainMenu

def main():
    print(f"Starting Pong with pygame version: {pygame.version.ver}\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    # 1. Define Groups
    updtable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # 2. Assign Containers Before Instantiation
    MainMenu.containers = (updtable, drawable)

    # 3. Instantiate Objects
    main_menu = MainMenu(
        SCREEN_WIDTH//4,
        SCREEN_HEIGHT//4,
        SCREEN_WIDTH//2,
        SCREEN_HEIGHT//2
    )

    

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen on each frame
        screen.fill("white")

        # Update all sprites
        updtable.update(dt)

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)  

        pygame.display.flip()

        # dt is noww in seconds (e.g., 0.016 for 60 FPS)
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
