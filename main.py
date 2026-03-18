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
    BottomLine.containers = (updtable, drawable)
    LeftLine.containers = (updtable, drawable)
    RightLine.containers = (updtable, drawable)

    # 3. Instantiate Objects
    main_menu = MainMenu(
        screen_width//4,
        screen_height//4,
        screen_width//2,
        screen_height//2
    )
    top_line = TopLine(0, 0, screen_width, 0)
    bottom_line = BottomLine(0, screen_height, screen_width, screen_height)
    left_line = LeftLine(0, 0, 0, screen_height)
    right_line = RightLine(screen_width, 0, screen_width, screen_height)

    

    while running:

        key = pygame.key.get_pressed()

        is_paused = any(isinstance(s, PauseMenu) for s in updtable)
            
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
                    if isinstance(sprite, TopLine):
                        sprite.resize(0, 0, screen_width, 0)
                    if isinstance(sprite, BottomLine):
                        sprite.resize(0, screen_height, screen_width, screen_height)
                    if isinstance(sprite, LeftLine):
                        sprite.resize(0, 0, 0, screen_height)
                    if isinstance(sprite, RightLine):
                        sprite.resize(screen_width, 0, screen_width, screen_height)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Only spawn a pause menu if one doesn't already exist
                    if not any(isinstance(s, PauseMenu) for s in updtable):
                        pause_menu =PauseMenu(
                            screen_width//4,
                            screen_height//4,
                            screen_width//2,
                            screen_height//2
                        )

        # Clear screen on each frame
        screen.fill("white")

        # Update all sprites
        updtable.update(dt)

        # Draw main menu first
        if any(isinstance(s, MainMenu) for s in updtable):
            main_menu.draw(screen)

        # Draw pause menu if it exists
        if any(isinstance(s, PauseMenu) for s in updtable):
            pause_menu.draw(screen)

        # Only draw when main menu or pause menu is not present to avoid overlap
        if not any(isinstance(s, MainMenu) for s in updtable) and not any(isinstance(s, PauseMenu) for s in updtable): 
            top_line.draw(screen)
            bottom_line.draw(screen)
            left_line.draw(screen)
            right_line.draw(screen)

        pygame.display.flip()

        # dt is now in seconds (e.g., 0.016 for 60 FPS)
        dt = clock.tick(60) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()