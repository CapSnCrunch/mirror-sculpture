import pygame
import random

win_size = 800

class Image:
    def __init__(self, size, location):
        self.size = size
        self.array = [[0 * size] * size]
        self.location = location # Can be 1-4 for images around the sculpture or 5 for the top

    def draw(self):
            for i in range(self.size + 1):
                if i == 0 or i == self.size:
                    line_thickness = 3
                else:
                    line_thickness = 2
                if self.location == 1:
                    pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.025+0.3*i/self.size)*win_size), (0.65*win_size, (0.025+0.3*i/self.size)*win_size), line_thickness)
                    pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.025*win_size), ((0.35+0.3*i/self.size)*win_size, 0.325*win_size), line_thickness)
                if self.location == 2:
                    pygame.draw.line(win, (0,0,0), (0.675*win_size, (0.35+0.3*i/self.size)*win_size), (0.975*win_size, (0.35+0.3*i/self.size)*win_size), line_thickness)
                    pygame.draw.line(win, (0,0,0), ((0.675+0.3*i/self.size)*win_size, 0.35*win_size), ((0.675+0.3*i/self.size)*win_size, 0.65*win_size), line_thickness)
                if self.location == 3:
                    pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.675+0.3*i/self.size)*win_size), (0.65*win_size, (0.675+0.3*i/self.size)*win_size), line_thickness)
                    pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.675*win_size), ((0.35+0.3*i/self.size)*win_size, 0.975*win_size), line_thickness)
                if self.location == 4:
                    pygame.draw.line(win, (0,0,0), (0.025*win_size, (0.35+0.3*i/self.size)*win_size), (0.325*win_size, (0.35+0.3*i/self.size)*win_size), line_thickness)
                    pygame.draw.line(win, (0,0,0), ((0.025+0.3*i/self.size)*win_size, 0.35*win_size), ((0.025+0.3*i/self.size)*win_size, 0.65*win_size), line_thickness)
                if self.location == 5:
                    pygame.draw.line(win, (0,0,0), (0.025*win_size, (0.025+0.3*i/self.size)*win_size), (0.325*win_size, (0.025+0.3*i/self.size)*win_size), line_thickness)
                    pygame.draw.line(win, (0,0,0), ((0.025+0.3*i/self.size)*win_size, 0.025*win_size), ((0.025+0.3*i/self.size)*win_size, 0.325*win_size), line_thickness)

class Sculpture:
    def __init__(self, array):
        # Arrays are a 2D-list of tuples which contain a direction (1-4) and a height (int)
        self.array = array
        self.size = len(array[0])

        pygame.font.init()
        self.font = pygame.font.SysFont('dejavuserif', int(20 - self.size))

    def draw(self):
        # Draw grid
        for i in range(self.size + 1):
            if i == 0 or i == self.size:
                line_thickness = 3
            else:
                line_thickness = 2
            pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.35+0.3*i/self.size)*win_size), (0.65*win_size, (0.35+0.3*i/self.size)*win_size), line_thickness)
            pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.35*win_size), ((0.35+0.3*i/self.size)*win_size, 0.65*win_size), line_thickness)

        # Draw arrows and height values
        for i in range(self.size):
            for j in range(self.size):
                # Arrows
                center = ((0.35+0.3*i/self.size)*win_size + 0.3/(2*self.size)*win_size, (0.35+0.3*j/self.size)*win_size + 0.3/(2*self.size)*win_size)
                if self.array[i][j][0] == 1:
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0], center[1]+0.07*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0]+0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0]-0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                if self.array[i][j][0] == 2:
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]+0.07*win_size/self.size, center[1]), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]-0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]-0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                if self.array[i][j][0] == 3:
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0], center[1]+0.07*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]-0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                if self.array[i][j][0] == 4:
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]+0.07*win_size/self.size, center[1]), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)

                # Height Values
                text = self.font.render(str(self.array[i][j][1]), True, (0,0,0))
                textRect = text.get_rect()
                textRect.center = ((0.35+0.3*i/self.size)*win_size + 0.5/(2*self.size)*win_size, (0.35+0.3*j/self.size)*win_size + 0.5/(2*self.size)*win_size)
                win.blit(text, textRect)

size = 4
array = []
for i in range(size):
    row = []
    for j in range(size):
        row.append((random.randint(1,4), random.randint(1,3)))
    array.append(row)

S = Sculpture(array)

I1 = Image(size, 1)
I2 = Image(size, 2)
I3 = Image(size, 3)
I4 = Image(size, 4)
IM = Image(size, 5)

'''s = Sculpture([[(1, 1), (2, 1)],
               [(4, 1), (3, 1)]])'''

if __name__ == '__main__':
    win = pygame.display.set_mode((win_size, win_size))
    pygame.display.set_caption('Mirror Sculpture')
    win.fill((255,255,255))

    S.draw()
    I1.draw()
    I2.draw()
    I3.draw()
    I4.draw()
    IM.draw()

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()