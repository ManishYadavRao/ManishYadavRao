import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Dodge: The Galactic Escape")

# Player settings
player_width = 50
player_height = 50
player_speed = 5

# Obstacle settings
obstacle_width = 90
obstacle_height = 60
obstacle_speed = 11

# Fonts
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("Press SPACE to play again", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                main()

def main():
    player_x = SCREEN_WIDTH // 2 - player_width // 2
    player_y = SCREEN_HEIGHT - player_height - 20
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacles = []

    score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
            player_x += player_speed

        # Move obstacles
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > SCREEN_HEIGHT:
                obstacles.remove(obstacle)
                score += 1

        # Create new obstacles
        if random.randint(0, 100) < 2:
            obstacle_x = random.randint(0, SCREEN_WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))

        # Check for collisions
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                game_over()

        # Draw everything
        screen.fill(BLACK)
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        pygame.draw.rect(screen, WHITE, player_rect)
        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, obstacle)
        draw_text(f"Score: {score}", font, WHITE, 10, 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
