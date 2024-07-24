import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
bird_size = 30
bird_x = 50
bird_y = HEIGHT // 2
bird_drop_speed = 0
gravity = 0.25
jump_strength = -5
pipe_width = 50
pipe_gap = 150
pipe_speed = 3
pipes = []

# Fonts
font = pygame.font.Font(None, 36)

def draw_bird():
    pygame.draw.rect(screen, WHITE, (bird_x, bird_y, bird_size, bird_size))

def draw_pipe(pipe):
    pygame.draw.rect(screen, WHITE, pipe)

def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def generate_pipe():
    top_pipe_height = random.randint(50, HEIGHT//2)
    bottom_pipe_height = HEIGHT - pipe_gap - top_pipe_height
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, top_pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, HEIGHT - bottom_pipe_height, pipe_width, bottom_pipe_height)
    pipes.extend((top_pipe, bottom_pipe))

def move_pipes():
    for pipe in pipes:
        pipe.x -= pipe_speed

def draw_pipes():
    for pipe in pipes:
        draw_pipe(pipe)

def check_collision():
    for pipe in pipes:
        if pipe.colliderect(pygame.Rect(bird_x, bird_y, bird_size, bird_size)) or bird_y <= 0 or bird_y >= HEIGHT - bird_size:
            return True
    return False

def reset_game():
    global bird_y, bird_drop_speed, pipes
    bird_y = HEIGHT // 2
    bird_drop_speed = 0
    pipes.clear()

# Game loop
clock = pygame.time.Clock()
score = 0
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_drop_speed = jump_strength
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_game()
            game_over = False

    screen.fill(BLACK)

    if not game_over:
        bird_drop_speed += gravity
        bird_y += bird_drop_speed

        if len(pipes) == 0 or pipes[-1].x <= WIDTH - 200:
            generate_pipe()

        move_pipes()
        draw_pipes()

        if pipes[0].x + pipe_width < 0:
            pipes.pop(0)
            pipes.pop(0)
            score += 1

        if check_collision():
            game_over = True

        draw_bird()
        display_score(score)
    else:
        game_over_text = font.render("Game Over - Press SPACE to Restart", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(game_over_text, game_over_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
