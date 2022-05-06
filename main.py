import pygame, sys, pymunk, time

def init_obiektu_dyn(przestrzen, poz):
    obiekt = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    obiekt.position = poz
    ksztalt = pymunk.Circle(obiekt, wielkosc_okregu)
    przestrzen.add(obiekt,ksztalt)
    return ksztalt

def wizualizacja_obiektu(zbior):
    for obiekt in zbior:
        poz_x = int(obiekt.body.position.x)
        poz_y = int(obiekt.body.position.y)
        pygame.draw.circle(okno, (255,255,255), (poz_x, poz_y), wielkosc_okregu)

pygame.init()
okno = pygame.display.set_mode((1000,1000))
wielkosc_okregu = 20
pygame_clock = pygame.time.Clock()
przestrzen_symulacji = pymunk.Space()
przestrzen_symulacji.gravity = (0, 100)
obiekty = []

while True:

    pygame_clock.tick(120)
    okno.fill((0,0,0))
    przestrzen_symulacji.step(1/60)
    wizualizacja_obiektu(obiekty)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            obiekty.append(init_obiektu_dyn(przestrzen_symulacji, pygame.mouse.get_pos()))
        if event.type == pygame.MOUSEWHEEL:
            obiekty.append(init_obiektu_dyn(przestrzen_symulacji, pygame.mouse.get_pos()))