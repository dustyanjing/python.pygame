import pygame

pygame.init()

size=width,height=936,804
speed=[1,1]
GOLD=255,251,0
BLACK=0,0,0
pos=[230,160]
fps=300
fclock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
pygame.display.set_caption('hello')
piture=pygame.image.load(r'C:\Users\qianqian\Desktop\screenshot.png')
f1=pygame.freetype.Font(r"C:\Windows\Fonts\simsun.ttc",size=36)
f1surf,f1rect=f1.render("皮卡丘",fgcolor=GOLD,size=50)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    if pos[0]<0 or pos[0]+f1rect.width>width:
            speed[0]=-speed[0]
    elif pos[1]<0 or pos[1]+f1rect.height>height:
            speed[1]=-speed[1]
    pos[0]=pos[0]+speed[0]
    pos[1]=pos[1]+speed[1]
    f1surf,f1rect=f1.render("皮卡丘",fgcolor=GOLD,size=50)
    screen.blit(pygame.transform.scale(piture,size),(0,0))

    screen.blit(f1surf,(pos[0],pos[1]))
    pygame.display.update()
    fclock.tick(fps)