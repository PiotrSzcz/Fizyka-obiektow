import pygame, sys, pymunk

def init_obiektu_dyn(przestrzen, poz):
    obiekt = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    obiekt.position = poz
    ksztalt = pymunk.Circle(obiekt, wielkosc_okregu)
    przestrzen.add(obiekt,ksztalt)
    return ksztalt

def init_obiektu_stat(przestrzen, poz):
    obiekt = pymunk.Body(1, 100, body_type=pymunk.Body.STATIC)
    obiekt.position = poz
    ksztalt = pymunk.Circle(obiekt, wielkosc_okregu*2)
    przestrzen.add(obiekt,ksztalt)
    return ksztalt

def wizualizacja_obiektu(zbior, wielkosc):
    for obiekt in zbior:
        poz_x = int(obiekt.body.position.x)
        poz_y = int(obiekt.body.position.y)
        pygame.draw.circle(okno, (255,255,255), (poz_x, poz_y), wielkosc)

pygame.init()
wielkosc_okregu = 20
wielkosc_okna_symulacji = 1000
okno = pygame.display.set_mode((wielkosc_okna_symulacji,wielkosc_okna_symulacji))
pygame_clock = pygame.time.Clock()
przestrzen_symulacji = pymunk.Space()
przestrzen_symulacji.gravity = (0, 100)
obiekty_dyn = []
obiekty_stat = []

def main():
    while True:

        pygame_clock.tick(120)
        okno.fill((0,0,0))
        przestrzen_symulacji.step(1/60)
        wizualizacja_obiektu(obiekty_dyn, wielkosc_okregu)
        wizualizacja_obiektu(obiekty_stat, wielkosc_okregu*2)
        pygame.display.update()

        licznik_kul = 0
        for kula in obiekty_dyn:
            if kula.body.position.y > wielkosc_okna_symulacji+wielkosc_okregu/2 or kula.body.position.y < 0-wielkosc_okregu/2:
                obiekty_dyn.pop(licznik_kul)
            licznik_kul += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    obiekty_dyn.append(init_obiektu_dyn(przestrzen_symulacji, pygame.mouse.get_pos()))
                if event.button == 3:
                    obiekty_stat.append(init_obiektu_stat(przestrzen_symulacji, pygame.mouse.get_pos()))
            elif event.type == pygame.MOUSEWHEEL:
                obiekty_dyn.append(init_obiektu_dyn(przestrzen_symulacji, pygame.mouse.get_pos()))

if __name__ == "__main__":
    main()