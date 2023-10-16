import pygame
import math

# Defina as cores fora da classe
color_1 = (222, 11, 11)  # Vermelho
color_n = (195, 7, 237)  # Roxo

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemPlayer1 = pygame.image.load('./characters/fagames.png')
        #self.ImagemPlayer1 = pygame.transform.scale(self.ImagemPlayer1, (64, 64))

        # Colisoes
        self.rect = self.ImagemPlayer1.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height //2
        
        

    def colocar(self, superficie):
        image = pygame.transform.rotate(self.ImagemPlayer1, angle)  # Rotaciona o personagem
        image = pygame.transform.rotate(image,-33)  #Rotaciona o personagem para cima
        rect = image.get_rect(center=self.rect.center)
        superficie.blit(image, rect)

def CS2():
    pygame.init()
    global width, height, angle
    width = 1280
    height = 720
    angle = 0
    screen = pygame.display.set_mode((width, height))
    running = True

    jogador1 = Player()

    center = width // 2, height // 2
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Atualiza a posição do mouse e calcula o ângulo de rotação
        mouse = pygame.mouse.get_pos()
        x = mouse[0] - center[0]
        y = mouse[1] - center[1]
        d = math.sqrt(x**2 + y**2)
        angle = math.degrees(-math.atan2(y, x))

        screen.fill(color_n)
        jogador1.colocar(screen)

        # Desenhe o retângulo da hitbox
        pygame.draw.rect(screen, "black", jogador1.rect, 3)

        # Desenhe a linha que segue o ponteiro
        pygame.draw.line(screen, color_1, center, mouse, 2)

        # Desenhe os círculos de referência
        pygame.draw.circle(screen, color_1, center, 6, 1)
        pygame.draw.circle(screen, "white", mouse, 6, 2)

        pygame.display.update()

    pygame.quit()

CS2()
