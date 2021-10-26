import pygame
import os
pygame.font.init()


HEIGHT = 500
WIDTH = 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("PONG GAME")


#COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

#BACKGROUND
bg_ground = pygame.Color("grey12")
BORDER = pygame.Rect(WIDTH//2 - 5,0,2.5,HEIGHT)

#FONT
SCORE_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)


#CONSTANTS
FPS = 60
VELOCITY = 10



#PLAYERS
PLAYER_1 = pygame.Rect(10,HEIGHT/2-60,10,100)
PLAYER_2 = pygame.Rect(WIDTH-20,HEIGHT/2-60,10,100)


#BALL
BALL = pygame.Rect(WIDTH/2-15,HEIGHT/2,25,25)

def draw_win(p1_score,p2_score):
    
    WIN.fill(bg_ground)
    pygame.draw.rect(WIN,WHITE,BORDER)

    player_1_score_text = SCORE_FONT.render("Lives: " + str(p1_score),1,WHITE)
    player_2_score_text = SCORE_FONT.render("Lives: " + str(p2_score),1,WHITE)
    pygame.draw.rect(WIN,WHITE,PLAYER_1)
    pygame.draw.rect(WIN,WHITE,PLAYER_2)
    pygame.draw.ellipse(WIN,WHITE,BALL)

    WIN.blit(player_1_score_text,(10,10))
    WIN.blit(player_2_score_text,(WIDTH - player_2_score_text.get_width() - 10,10))
    pygame.display.update()


def player1_movement(key_pressed,PLAYER_1):

    if key_pressed[pygame.K_w] and PLAYER_1.y - VELOCITY > 0:
        PLAYER_1.y -= VELOCITY
    if key_pressed[pygame.K_s] and PLAYER_1.y + VELOCITY + PLAYER_1.height < HEIGHT + 5:
        PLAYER_1.y += VELOCITY

def player2_movement(key_pressed,PLAYER_2):

    if key_pressed[pygame.K_UP] and PLAYER_2.y - VELOCITY > 0:
        PLAYER_2.y -= VELOCITY
    if key_pressed[pygame.K_DOWN] and PLAYER_2.y + VELOCITY + PLAYER_1.height < HEIGHT + 5:
        PLAYER_2.y += VELOCITY

def draw_winner(text):
    winner_font_text = WINNER_FONT.render(text,1,WHITE)
    WIN.blit(winner_font_text,(WIDTH/2 - winner_font_text.get_width()/2 , HEIGHT/2 - winner_font_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_timer(timer,color):
    winner_font_text = SCORE_FONT.render(timer,1,color)
    WIN.blit(winner_font_text,(WIDTH//2 - 20,10))
    pygame.display.update()


def main():

    ball_speed_x = 7
    ball_speed_y = 7

    p1_score = 3
    p2_score = 3
    winner_text =""
    color = WHITE
    #GAME LOOP
    start_time = 60000
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
                

        key_pressed = pygame.key.get_pressed()
        if BALL.bottom >= HEIGHT or BALL.top <= 0:
            ball_speed_y = - ball_speed_y
        
        if BALL.colliderect(PLAYER_1):
            ball_speed_x = -ball_speed_x

        if BALL.colliderect(PLAYER_2):
            ball_speed_x = -ball_speed_x

        if BALL.left <= 0:
            p1_score -= 1
            ball_speed_x = -ball_speed_x
            
        
        if BALL.right >= WIDTH:
            p2_score -= 1
            ball_speed_x = -ball_speed_x
        
        if p1_score == -1:
            winner_text = "Player 2 Wins!"
            draw_winner(winner_text)
            break
           
        if p2_score == -1:
            winner_text = "Player 1 Wins!"
            draw_winner(winner_text)
            break
            
        BALL.y += ball_speed_y
        BALL.x += ball_speed_x

        current_time = pygame.time.get_ticks()
        current_time_sec  = (start_time - current_time)//1000
        if current_time_sec == 10:
            color = RED
            if current_time_sec < 0:
                winner_text = "TIME OUT"
                draw_winner(winner_text)
                pygame.time.delay(5000)
                break
                
        key_pressed = pygame.key.get_pressed()
        draw_win(p1_score,p2_score)
        player1_movement(key_pressed,PLAYER_1)
        player2_movement(key_pressed,PLAYER_2)
        draw_timer(str(current_time_sec),color)
        

    pygame.quit()

if __name__ == "__main__":
    main()
            
        
