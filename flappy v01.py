#it's a test program....&&.eitate kichu provlem ache ';
#flappy cat v01 ...test run pass ..with gravity = 0;::
import pygame
import random

pygame.init()


WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Cat")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN =(0,128,0)

cat_img = pygame.image.load("cat.png")
cat_img = pygame.transform.scale(cat_img, (50, 50))
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img,(WIDTH, HEIGHT))

cat_x = 50
cat_y = HEIGHT // 2
cat_velocity = 0
gravity = 0.3
jump_strength = 8
gap =  250         
pipe_width = 50
pipe_speed = 2
pipes =[]
score =0
font = pygame.font.Font(None, 35)

def draw_cat(x, y):
    screen.blit(cat_img, (x, y))

def draw_background():
    screen.blit(background_img, (0,0))

def draw_pipe(pipe):
    pygame.draw.rect(screen, GREEN, pipe)

def generate_pipe():
    top_pipe_height = random.randint(50, HEIGHT//2)
    bottom_pipe_height = HEIGHT - top_pipe_height - gap
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, top_pipe_height)
    bottom_pipe = pygame.Rect(WIDTH, HEIGHT - bottom_pipe_height, pipe_width, bottom_pipe_height)
    return top_pipe, bottom_pipe

def move_pipes():
    for pipe in pipes:
        pipe.x -= pipe_speed

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

def check_collision():
    for pipe in pipes:
        if cat_rect.colliderect(pipe):
            return True
    if cat_y <= 0 or cat_y >= HEIGHT - 50:
        return True
    return False

def draw_score(score):
    score_text = font.render("Score: " + str(score), True, YELLOW)
    screen.blit(score_text, (10, 10))
  
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cat_velocity = -jump_strength


    cat_velocity += gravity
    cat_y += cat_velocity

    if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
        pipes.extend(generate_pipe())


    pipes = [pipe for pipe in pipes if pipe.x > -pipe_width]


    move_pipes()
    screen.fill(BLACK)
    draw_background()
    draw_pipes()


    cat_rect = pygame.Rect(cat_x, cat_y, 50, 50)
    draw_cat(cat_x, cat_y)

    if check_collision():
        running = False
     
    for pipe in pipes:
        if pipe.x == cat_x:
            score += 1

    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    draw_score(score)

    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
             