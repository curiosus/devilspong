import sys, pygame

def main():
  pygame.init()
  size = width, height = 1280, 960 
  speed = [2, 2]
  paddlespeed = [2, 0]
  black = 0, 0, 0
  screen = pygame.display.set_mode(size)
  ball = pygame.image.load("ball.gif")
  ballrect = ball.get_rect()

  x = 300
  y = 910
  paddle = pygame.Surface((200, 50))
  paddle.fill((156, 84, 255))
  paddlerect = paddle.get_rect()
  paddlerect = paddlerect.move(x, y)

  running = True
  
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
      speed[0] = -speed[0]

    if ballrect.top < 0:
      speed[1] = -speed[1] 

    if pygame.key.get_pressed() [pygame.K_a] != 0:
        if paddlespeed[0] > 0:
          paddlespeed[0] = -paddlespeed[0]
        paddlerect = paddlerect.move(paddlespeed)
          

    if pygame.key.get_pressed() [pygame.K_d] != 0:
        paddlespeed[0] = abs(paddlespeed[0])
        paddlerect = paddlerect.move(paddlespeed)


    if ballrect.colliderect(paddlerect):
      speed[1] = -speed[1]

    if ballrect.bottom > height:
      pygame.time.wait(10000)
      speed[1] = -speed[1]

 
    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle, paddlerect)
    pygame.display.flip()

if __name__ =="__main__":
  main() 
    
