import pygame
from constants import *
from mainmenu import MainMenu
from pausemenu import PauseMenu
from rectshape import RectShape
from boundingbox import *



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
    TopLine.containers = (updtable, drawable)

    # 3. Instantiate Objects
    main_menu = MainMenu(
        screen_width//4,
        screen_height//4,
        screen_width//2,
        screen_height//2
    )

    

    while running:

        key = pygame.key.get_pressed()

        is_paused = any(isinstance(s, PauseMenu) for s in updtable)

        # Check if Escape is pressed AND a PauseMenu doesn't already exist
        if key[pygame.K_ESCAPE]:

            # Only create a new one if the 'updtable' group doesn't have a PauseMenu
            if not is_paused:
                pause_menu = PauseMenu(
                    screen_width // 4,
                    screen_height // 4,
                    screen_width // 2,
                    screen_height // 2
                )
                pause_menu.draw(screen)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle window resize event
            if event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                print(f"Window resized to: {screen_width}x{screen_height}")
                
                # Loop through all sprites and update their coordinates if they have a resize method
                for sprite in updtable:
                    if isinstance(sprite, MainMenu) or isinstance(sprite, PauseMenu):
                        sprite.resize(screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2)

        # Clear screen on each frame
        screen.fill("white")

        # Update all sprites
        updtable.update(dt)

        # Draw all sprites
        for sprite in drawable:
            if sprite is not isinstance(sprite, MainMenu):
                top_line = TopLine(0, screen_height, screen_width, screen_height)
                top_line.draw(screen)
            sprite.draw(screen)  

        pygame.display.flip()

        # dt is now in seconds (e.g., 0.016 for 60 FPS)
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()