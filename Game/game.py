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



#Pega a imagem
image = pygame.image.load('./characters/fagames.png')
# image = pygame.transform.rotate(image,45)  #Rotaciona o personagem para cima
image.convert()

#Desenha um retangulo ao redor
rect = image.get_rect(center=(640,360))  #Posiciona o player no mapa
border_rect = image.get_rect()
pygame.draw.rect(image, color_1, border_rect, 1)

#Definindo o centro e a posição de mouse e teclado
center = width//2, height//2  #Pegando as coordenadas do centro da tela
mouse = pygame.mouse.get_pos()
keys = pygame.key.get_pressed()


img = image  #Armazenando a imagem em uma nova variável
rect = img.get_rect()  #Desenhando um retangulo ao redor da imagem
rect.center = center



# position = pygame.img.get_rect()    ----- Corrigir o erro de fazer uma box para o personagem e tratar como player, pois a imagem não é possível pegar a posição
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
      img = pygame.transform.rotozoom(image, angle, scale)
      #Construir retangulo ao redor da nova imagem
      rect = img.get_rect()
      rect.center = center
    if event.type == keys[pygame.K_w]:
      position.move(up=True)


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
  #pygame.display.flip()

  #clock.tick(60)  # limits FPS to 60

pygame.quit()