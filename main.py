import pygame
from constants import *
from mainmenu import MainMenu
from pausemenu import PauseMenu



def main():

    screen_width = SCREEN_WIDTH
    screen_height = SCREEN_HEIGHT

    print(f"Starting Pong with pygame version: {pygame.version.ver}\nScreen width: {screen_width}\nScreen height: {screen_height}")
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    # 1. Define Groups
    updtable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # 2. Assign Containers Before Instantiation
    MainMenu.containers = (updtable, drawable)
    PauseMenu.containers = (updtable, drawable)

    # 3. Instantiate Objects
    main_menu = MainMenu(
        screen_width//4,
        screen_height//4,
        screen_width//2,
        screen_height//2
    )

    

    while running:
        # Check for pause menu trigger
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pause_menu = PauseMenu(
                screen_width//4,
                screen_height//4,
                screen_width//2,
                screen_height//2
            )
            pause_menu.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                print(f"Screen resized to: {screen_width}x{screen_height}")

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