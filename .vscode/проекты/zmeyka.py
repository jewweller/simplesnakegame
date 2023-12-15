import pygame
import random
import time

pygame.init()


red= (255,0,0)
green= (0,255,0)
blue = (0,0,255)

dis_l = 400
dis_w = 400

gbz = 40


dis = pygame.display.set_mode((dis_l, dis_w))
pygame.display.set_caption('ZmEyKa')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 60)

def st(score):
    stetchik = font_style.render('ochki = ' + str(score), True, red)
    dis.blit(stetchik, [0, 0])
def uvel(gbz, dlzz):
    for i in dlzz:
        pygame.draw.rect(dis, green, [i[0], i[1], gbz, gbz])

def message(color, msg):
    shr = font_style.render(msg, True, color)
    dis.blit(shr, [dis_w//2-20, dis_l//2-20])
def zmk():
    game_over = False
    game_close = False
    x1 = dis_w // 2
    y1 = dis_l // 2
    x1c = 0
    y1c = 0
    x_ap = round(random.randrange(0, dis_w-40, 40)+20)
    y_ap = round(random.randrange(0, dis_l-40, 40)+20)
    dlz = 1
    dlzz = []
    score = 0



    while not game_over:
        while game_close == True:
            message(red, 'YOU DIED')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        zmk()
                    elif event.key == pygame.K_q:
                        game_over = True
                        game_close = False


        for event in pygame.event.get():
         #print(event)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1c = -40
                    y1c = 0
                elif event.key == pygame.K_RIGHT:
                    x1c = 40
                    y1c = 0
                elif event.key == pygame.K_UP:
                    x1c = 0
                    y1c = -40
                elif event.key == pygame.K_DOWN:
                    x1c = 0
                    y1c = 40
        if x1 >= dis_w or x1 < 0 or y1 >= dis_l or y1 < 0:
                #message(red, 'YOU DIED')
            game_close = True
        dis.fill(blue)
        st(dlz-1)
        x1 += x1c
        y1 += y1c
        pygame.draw.circle(dis, red, [x_ap, y_ap], radius=20)
        gol = []
        gol.append(x1)
        gol.append(y1)
        dlzz.append(gol)
        if len(dlzz) > dlz:
            del dlzz[0]
        for i in dlzz[0:-1]:
            if i == gol:
                game_close = True
        uvel(gbz, dlzz)
        pygame.display.update()
        if x1+20 == x_ap and y1+20 == y_ap:
            x_ap = round(random.randrange(0, dis_w - 40, 40) + 20)
            y_ap = round(random.randrange(0, dis_l - 40, 40) + 20)
            dlz += 1
        pygame.display.update()
        clock.tick(7)


    pygame.quit()
    quit()
zmk()
