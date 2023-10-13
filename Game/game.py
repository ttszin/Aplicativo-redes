import pygame
import math

# pygame setup
pygame.init()
width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
angle = 0
scale = 1

color_1 = "#de0b0b"
color_n = "#c307ed"

w, h = 600, 440


# class Player(pygame.sprite.Sprite):

#   def __init__(self):
#     super().__init__()
    

#     #Desenhando uma borda ao redor da imagem


# group_player = pygame.sprite.Group()
# group_player.add(Player())

image = pygame.image.load('./characters/fagames.png')
rect = image.get_rect(center=(640,360))  #Posiciona o player no mapa
image = pygame.transform.rotate(image,45)  #Rotaciona o personagem para cima

imagem = image.convert()

border_rect = imagem.get_rect()
pygame.draw.rect(imagem, color_1, border_rect, 180)

center = width // 2, height // 2  #Pegando as coordenadas do centro da tela
mouse = pygame.mouse.get_pos()


img = imagem  #Armazenando a imagem em uma nova variável
rect = img.get_rect()  #Desenhando um retangulo ao redor da imagem
rect.center = center

while running:
  # poll for events
  # pygame.QUIT event means the user clicked X to close your window
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEMOTION:
      mouse = event.pos
      x = mouse[0] - center[0]
      y = mouse[1] - center[1]
  
      d = math.sqrt(x**2 + y**2)
      angle = math.degrees(-math.atan2(y, x))
      scale = abs(5 * d / w)
      img = pygame.transform.rotozoom(imagem, angle, scale)
      #Construir retangulo ao redor da nova imagem
      rect = img.get_rect()
      rect.center = center

    screen.fill(color_n)
    screen.blit(img, rect)


    pygame.draw.rect(screen, color_n, rect, 3)
    pygame.draw.line(screen, color_1, center, mouse, 2)
    pygame.draw.circle(screen, color_1, center, 6, 1)
    pygame.draw.circle(screen, color_n, mouse, 6, 2)
    
    
    pygame.display.update()

  
  # fill the screen with a color to wipe away anything from last frame
  screen.fill("white")

  # RENDER YOUR GAME HERE
  #group_player.draw(screen)

  # flip() the display to put your work on screen
  pygame.display.flip()

  clock.tick(60)  # limits FPS to 60

pygame.quit()
