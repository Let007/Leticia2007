import pygame
from pygame.locals import *

pygame.init()

altura = 700
largura = 400

x = largura / 2 - 100
y = altura / 2 - 100

tela = pygame.display.set_mode((largura, altura))


pygame.display.set_caption("Jogo da Lelê")
relogio = pygame.time.Clock()

image = pygame.image.load('fundo_de_bits_do_fogo_da_pixel_da_arte.jpg')
image_width, image_height = image.get_size()
new_width = largura
new_height = int(image_height * (new_width / image_width))
image_scaled = pygame.transform.scale(image, (new_width, new_height))

obstaculo_largura = 290
obstaculo_altura = 20

obstaculo1_x = largura - obstaculo_largura 
obstaculo1_y = altura / 4 - obstaculo_altura / 2

obstaculo2_x = largura - obstaculo_largura 
obstaculo2_y = altura * 3 / 4 - obstaculo_altura / 2

obstaculo3_x = 0
obstaculo3_y = (obstaculo1_y + obstaculo2_y) / 2

obstaculo4_x = 0
obstaculo4_y = obstaculo2_y + obstaculo_altura + 200

obstaculos = [
            {"x": obstaculo1_x, "y": obstaculo1_y, "largura": obstaculo_largura, "altura": obstaculo_altura},
            {"x": obstaculo2_x, "y": obstaculo2_y, "largura": obstaculo_largura, "altura": obstaculo_altura},
            {"x": obstaculo3_x, "y": obstaculo3_y, "largura": obstaculo_largura, "altura": obstaculo_altura},
            {"x": obstaculo4_x, "y": obstaculo4_y, "largura": obstaculo_largura, "altura": obstaculo_altura}
        ]

velocidade_obstaculo = 2.0
placar = 0
placar_maximo = 0

def verifica_colisao(x, y, obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura):
    if (x + 40 > obstaculo_x and x - 40 < obstaculo_x + obstaculo_largura and
    y + 40 > obstaculo_y and y - 40 < obstaculo_y + obstaculo_altura):
            return True
            return False

def reiniciar_jogo():
    global placar, y, x, obstaculos
    placar = 0
    y = altura / 2
    pos_segura_x = largura

for obstaculo in obstaculos:
   if obstaculo["x"] < pos_segura_x:
    pos_segura_x = obstaculo["x"]
    x = pos_segura_x + obstaculo_largura + 50 

    obstaculos = [
                {"x": largura - obstaculo_largura, "y": altura / 4 - obstaculo_altura / 2, "largura": obstaculo_largura, "altura": obstaculo_altura},
                {"x": largura - obstaculo_largura, "y": altura * 3 / 4 - obstaculo_altura / 2, "largura": obstaculo_largura, "altura": obstaculo_altura},
                {"x": 0, "y": (obstaculo1_y + obstaculo2_y) / 2, "largura": obstaculo_largura, "altura": obstaculo_altura},
                {"x": 0, "y": obstaculo2_y + obstaculo_altura + 200, "largura": obstaculo_largura, "altura": obstaculo_altura}
            ]

while True:
            relogio.tick(20)
            tela.fill((0,0,0))

            for obstaculo in obstaculos:
                obstaculo["y"] += velocidade_obstaculo

                if obstaculo["y"] > altura:
                    obstaculo["y"] = -obstaculo_altura
                    placar += 1
                    placar_maximo = max(placar_maximo, placar)

            tela.blit(image_scaled, (0, altura - new_height - 5))

            for obstaculo in obstaculos:
                pygame.draw.rect(tela, (139, 69, 19), (obstaculo["x"], obstaculo["y"], obstaculo["largura"], obstaculo["altura"]))

            colisao = False
            for obstaculo in obstaculos:
                if verifica_colisao(x, y, obstaculo["x"], obstaculo["y"], obstaculo["largura"], obstaculo["altura"]):
                    colisao = True
                    placar += 1
                    placar_maximo = max(placar_maximo, placar)
                    break

            pygame.draw.circle(tela, (255, 0, 0), (x, y), 40)


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        y -= 30
                    elif event.key == K_DOWN:
                        y += 30
                    elif event.key == K_LEFT:
                        x -= 30
                    elif event.key == K_RIGHT:
                        x += 30
                    elif event.key == K_SPACE:
                        reiniciar_jogo()


            if y > altura:
                y = 0    


            if y + 40 >= altura - new_height - 5: 
               font = pygame.font.Font(None, 36) 
               text = font.render(f"Placar: {placar_maximo}", True, (255, 255, 255))
               tela.blit(text, (10, 10))
               pygame.display.update()
               pygame.time.wait(2000) 
               reiniciar_jogo()

            font = pygame.font.Font(None, 36)
            text = font.render(f"Placar: {placar}", True, (255, 255, 255))
            tela.blit(text, (10, 10))

            pygame.display.update()

            if colisao:
                print("Colisão com obstáculo!")
                font = pygame.font.Font(None, 36)
                text = font.render(f"Placar: {placar_maximo}", True, (255, 255, 255))
                tela.blit(text, (10, 10))
                pygame.display.update()
                pygame.time.wait(2000)
                reiniciar_jogo()