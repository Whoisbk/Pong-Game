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

#BACKGROUND
bg_ground = pygame.Color("grey12")
BORDER = pygame.Rect(WIDTH//2 - 5,0,2.5,HEIGHT)

#FONT
SCORE_FONT = pygame.font.SysFont("comicsans",40)
WINNER_FONT = pygame.font.SysFont("comicsans",100)


#CONSTANTS
FPS = 60
VELOCITY = 5



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


def main():

    ball_speed_x = 7
    ball_speed_y = 7

    p1_score = 3
    p2_score = 3
    winner_text =""
    #GAME LOOP
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        key_pressed = pygame.key.get_pressed()
        player1_movement(key_pressed,PLAYER_1)
        player2_movement(key_pressed,PLAYER_2)
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
        
        if p1_score <= 0:
            winner_text = "Player 2 Wins!"
           
        if p2_score <= 0:
            winner_text = "Player 1 Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break
            
        BALL.y += ball_speed_y
        BALL.x += ball_speed_x
        
        key_pressed = pygame.key.get_pressed()
        player1_movement(key_pressed,PLAYER_1)
        player2_movement(key_pressed,PLAYER_2)
        draw_win(p1_score,p2_score)

    pygame.quite()

if __name__ == "__main__":
    main()
            
        
