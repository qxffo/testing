import pygame
import os
import sys

pygame.init()
WIDTH, HEIGHT = 900, 500
pygame.display.set_caption("footballgame thingy")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))



BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

FPS = 60

FIELD = pygame.image.load(
    os.path.join('data', 'field.jpg'))
  

PLAYER2 = pygame.image.load(os.path.join('data', 'player2.png')) 
PLAYER2 = pygame.transform.scale(PLAYER2, (35, 35))

FOOTBALL = pygame.image.load(os.path.join('data', 'football.png')) 
FOOTBALL = pygame.transform.scale(FOOTBALL, (25, 15))





WIN.blit(FIELD,(33,- 14))
pygame.display.flip()

def draw_window():
  WIN.blit(FIELD,(33,- 14))
  pygame.display.flip()
  pygame.display.update()
  



def main():
  PLAYER = pygame.image.load(os.path.join('data', 'player.png'))
  PLAYER = pygame.transform.scale(PLAYER, (35, 35))
  PLAYER.convert()
  rect = PLAYER.get_rect()
  rect.center = WIDTH//2, HEIGHT//2

  PLAYER2 = pygame.image.load(os.path.join('data', 'player2.png'))
  PLAYER2 = pygame.transform.scale(PLAYER2, (35, 35))
  PLAYER2.convert()
  rect2 = PLAYER2.get_rect()
  rect2.center = WIDTH//2, HEIGHT//2
  

  RED = (255, 0, 0)
  BLACK = 0, 0 ,0
  rect = PLAYER.get_rect()
  rect.center = WIDTH//2, HEIGHT//2


  font = pygame.font.SysFont("Times New Roman", 50)
  text = font.render(" TACKLE!", True, BLACK)
  font2 = pygame.font.SysFont("Times New Roman", 100)
  text2 = font2.render(" TOUCHDOWNNNNNN!", True, BLACK)


  rect.x = 430
  rect.y = 100
  rect2.x = 70
  rect2.y = 100
  o = 70
  b = 100

  touchdown1 = pygame.Rect(- 2, 100, 100, 20)
  touchdown2 = pygame.Rect(-2, 100, 100, 50)

  clock = pygame.time.Clock()
  run = True
  while run:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rect.y-=1
    if keys[pygame.K_DOWN]:
        rect.y+=1
    if keys[pygame.K_RIGHT]:
        rect.x+=1
    if keys[pygame.K_LEFT]:
        rect.x-=1

    if keys[pygame.K_w]:
        rect2.y-=1
        b-=1
    if keys[pygame.K_s]:
        rect2.y+=1
        b+=1
    if keys[pygame.K_d]:
        rect2.x+=1
        o+=1
    if keys[pygame.K_a]:
        rect2.x-=1 
        o-=1   
    obs = pygame.Rect(o, b, 10,10)


    WIN.fill(RED)
    
    WIN.blit(FIELD,(33,- 14))

    WIN.blit(PLAYER, (rect.x, rect.y))

    WIN.blit(FOOTBALL, (rect.x - 5, rect.y + 15))

    WIN.blit(PLAYER2, (rect2.x, rect2.y))



    if rect.colliderect(obs):
      score = pygame.font.SysFont("Times New Roman", 20)
      half = 1
      scorewin = score.render("Round: " + str(half) , True, BLACK)

      WIN.blit(scorewin, (WIDTH/7 - scorewin.get_rect().width/2, HEIGHT/2 - 250))
      pygame.draw.rect(WIN, (RED), rect, 3)
      WIN.blit(text, (WIDTH/3.3 - text.get_rect().width/2, HEIGHT/2 - 200))
      half+=1

      

    if rect.colliderect(touchdown1):
      pygame.draw.rect(WIN, (RED), rect, 3)
      WIN.blit(text2, (WIDTH/3.3 - text2.get_rect().width/2, HEIGHT/2 - 200))
    pygame.display.update()

    if rect.colliderect(touchdown2):
      pygame.draw.rect(WIN, (RED), rect, 3)
      WIN.blit(text2, (WIDTH/3.3 - text2.get_rect().width/2, HEIGHT/2 - 200))
    pygame.display.update()




    pygame.display.flip()    

    clock.tick(FPS)
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              run = False
              pygame.quit()


main()



if __name__ == "__main__":
    main()