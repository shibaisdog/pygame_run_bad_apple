import pygame,time
import page.work,page.sound
start = time.time()
pygame.init()
page.work.onload()
print(f"{time.time() - start}s")
SIZE = 7
GRID_SIZE_X = len(page.work.call(0)[0])
GRID_SIZE_Y = len(page.work.call(0))
screen = pygame.display.set_mode((GRID_SIZE_X*SIZE,GRID_SIZE_Y*SIZE))
def draw_grid_border(grid_string):
    for y in range(GRID_SIZE_Y):
        for x in range(GRID_SIZE_X):
            if int(grid_string[y][x]) == 0:
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*SIZE,y*SIZE,SIZE,SIZE))
i = 0
page.sound.play()
clock = pygame.time.Clock()
while True:
    screen.fill((255,255,255))
    draw_grid_border(page.work.call(int(i)))
    pygame.display.flip()
    clock.tick(30)
    i += 1