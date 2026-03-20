import pygame
from constants import *
from menus import *
from rectshape import *
from boundingbox import *
from paddles import *
from ball import *



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
    WinConditionMenu.containers = (updtable, drawable)
    top_bottom_lines = pygame.sprite.Group()
    TopLine.containers = (top_bottom_lines, updtable, drawable)
    BottomLine.containers = (top_bottom_lines, updtable, drawable)
    LeftLine.containers = (updtable, drawable)
    RightLine.containers = (updtable, drawable)
    players = pygame.sprite.Group()
    PlayerPaddle.containers = (players, updtable, drawable)
    AIPaddle.containers = (players, updtable, drawable)
    balls = pygame.sprite.Group()
    Ball.containers = (balls, updtable, drawable)


    # 3. Instantiate Objects

    margin = LINE_WIDTH

    main_menu = MainMenu(
        screen_width//4,
        screen_height//4,
        screen_width//2,
        screen_height//2
    )
    top_line = TopLine(0, margin, screen_width, margin)
    bottom_line = BottomLine(0, screen_height - margin, screen_width, screen_height - margin)
    left_line = LeftLine(margin, 0, margin, screen_height)
    right_line = RightLine(screen_width - margin, 0, screen_width - margin, screen_height)
    player = PlayerPaddle(25, screen_height//2 - PADDLE_HEIGHT//2, 25, screen_height//2 + PADDLE_HEIGHT//2)
    ai = AIPaddle(screen_width - 25, screen_height//2 - PADDLE_HEIGHT//2, screen_width - 25, screen_height//2 + PADDLE_HEIGHT//2)
    ball = Ball(screen_width//2, screen_height//2, BALL_RADIUS)

    

    while running:

        key = pygame.key.get_pressed()
            
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
                    if isinstance(sprite, MainMenu) or isinstance(sprite, PauseMenu) or isinstance(sprite, WinConditionMenu):
                        sprite.resize(screen_width // 4, screen_height // 4, screen_width // 2, screen_height // 2)
                    if isinstance(sprite, TopLine):
                        sprite.resize(0, 0, screen_width, 0)
                    if isinstance(sprite, BottomLine):
                        sprite.resize(0, screen_height, screen_width, screen_height)
                    if isinstance(sprite, LeftLine):
                        sprite.resize(0, 0, 0, screen_height)
                    if isinstance(sprite, RightLine):
                        sprite.resize(screen_width, 0, screen_width, screen_height)
                    if isinstance(sprite, PlayerPaddle):
                        sprite.resize(25, screen_height//2 - PADDLE_HEIGHT//2, 25, screen_height//2 + PADDLE_HEIGHT//2)
                    if isinstance(sprite, AIPaddle):
                        sprite.resize(screen_width - 25, screen_height//2 - PADDLE_HEIGHT//2, screen_width - 25, screen_height//2 + PADDLE_HEIGHT//2)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Only spawn a pause menu if one doesn't already exist
                    if not any(isinstance(s, PauseMenu) for s in updtable) and not any(isinstance(s, WinConditionMenu) for s in updtable):
                        pause_menu = PauseMenu(
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

        # Draw win condition menu if it exists
        if any(isinstance(s, WinConditionMenu) for s in updtable):
            win_menu.draw(screen)

        if any(isinstance(s, Ball) for s in updtable):

            # Simple AI to follow the ball
            if ball.position.y < ai.center[1]:
                ai.move(-dt/2)
            elif ball.position.y > ai.center[1]:
                ai.move(dt/2)

        for ball in balls:
            
            # Handle ball collisions with paddles and walls
            if ball.collides_with(player):
                ball.velocity.x *= -1
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    ball.velocity.y -= 100
                if keys[pygame.K_DOWN]:
                    ball.velocity.y += 100
            if ball.collides_with(ai):
                ball.velocity.x *= -1
            if ball.collides_with(top_line):
                ball.velocity.y *= -1
            if ball.collides_with(bottom_line):
                ball.velocity.y *= -1
            if ball.collides_with(left_line):
                ball.kill()
                ai.score += 1
                print(f"AI Score: {ai.score}")
                Ball(screen_width//2, screen_height//2, BALL_RADIUS)
                ball.draw(screen)
            if ball.collides_with(right_line):
                ball.kill()
                player.score += 1
                print(f"Player Score: {player.score}")
                Ball(screen_width//2, screen_height//2, BALL_RADIUS)
                ball.draw(screen)

        if player.score >= 10:
            win_menu = WinConditionMenu(
                screen_width//4,
                screen_height//4,
                screen_width//2,
                screen_height//2,
                "Player"
            )
        elif ai.score >= 1:
            win_menu = WinConditionMenu(
                screen_width//4,
                screen_height//4,
                screen_width//2,
                screen_height//2,
                "AI"
            )

        # Only draw when main menu or pause menu is not present to avoid overlap
        if not any(isinstance(s, MainMenu) for s in updtable) and not any(isinstance(s, PauseMenu) for s in updtable) and not any(isinstance(s, WinConditionMenu) for s in updtable): 
            top_line.draw(screen)
            bottom_line.draw(screen)
            left_line.draw(screen)
            right_line.draw(screen)
            player.draw(screen)
            ai.draw(screen)
            ball.draw(screen)

        pygame.display.flip()

        # Logic to freeze the game when the main menu or pause menu is active
        if not any(isinstance(s, MainMenu) for s in updtable) and not any(isinstance(s, PauseMenu) for s in updtable):
            dt = clock.tick(FRAME_RATE) / 1000
            #print(dt)
        else:
            dt = 0

    pygame.quit()


if __name__ == "__main__":
    main()