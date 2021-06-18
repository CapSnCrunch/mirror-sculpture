import pygame
import numpy as np

win_size = 800

# A sculpture is an n-by-n grid of mirrors with some direction and height (denoted respectively with an arrow and integer).
# A valid sculpture is one in which none of the mirrors block each other, that is, for any mirror M, all mirrors in the 
#   direction of that mirror have height strictly less than M's.
# An image is an n-by-n grid with some drawing in each of the grid cells.
# Sculptures include 4 images, 1 along each edge so that the mirrors in the sculpture reflect specific grid cells from 
#   the images direcetly upward.
# A perfect sculpture is one in which all pairs of mirrors M, N do not reflect the same row and column of their corresponding
#   images. (Perfect sculptures have a height of exactly n).

class Image:
    def __init__(self, img, size, location = 1):
        self.img = img
        self.array = []
        self.size = size
        self.location = location # Can be 1-4 for images around the sculpture or 5 for the top

    def draw(self):
        rimg = pygame.surfarray.make_surface(np.rot90(self.img, self.location-1))
        # Draw pieces of the image in the corresponding grid tiles
        if self.location == 1:
            win.blit(rimg, (0.35*win_size, 0.025*win_size))
        if self.location == 2:
            win.blit(rimg, (0.675*win_size, 0.35*win_size))
        if self.location == 3:
            win.blit(rimg, (0.35*win_size, 0.675*win_size))
        if self.location == 4:
            win.blit(rimg, (0.025*win_size, 0.35*win_size))
        # Draw grid offset from center
        for i in range(self.size + 1):
            if i == 0 or i == self.size:
                line_thickness = 2
            else:
                line_thickness = 1
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
    def __init__(self, directions, heights, images):
        # Arrays are a 2D-list of tuples which contain a direction (1-4) and a height (int)
        self.directions = directions
        self.heights = heights
        self.size = len(directions[0])
        self.images = images

        # Assign locations of images based on the order we were provided them
        for i in range(4):
            self.images[i].location = i + 1

        pygame.font.init()
        self.font = pygame.font.SysFont('dejavuserif', int(20 - self.size))

    def draw(self):
        '''Draws the sculpture, its 4 associated images, and the mirror reflection of those images'''
        # Draw centered grid
        for i in range(self.size + 1):
            if i == 0 or i == self.size:
                line_thickness = 2
            else:
                line_thickness = 1
            pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.35+0.3*i/self.size)*win_size), (0.65*win_size, (0.35+0.3*i/self.size)*win_size), line_thickness)
            pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.35*win_size), ((0.35+0.3*i/self.size)*win_size, 0.65*win_size), line_thickness)

        # Draw arrows and height values in grid cells
        for row in range(self.size):
            for col in range(self.size):
                # Arrows
                center = ((0.35+0.3*col/self.size)*win_size + 0.3/(2*self.size)*win_size, (0.35+0.3*row/self.size)*win_size + 0.3/(2*self.size)*win_size)
                if self.directions[row,col] == 1:
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0], center[1]+0.07*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0]+0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0]-0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                if self.directions[row,col] == 2:
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]+0.07*win_size/self.size, center[1]), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                if self.directions[row,col] == 3:
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0], center[1]+0.07*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]-0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                if self.directions[row,col] == 4:
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]+0.07*win_size/self.size, center[1]), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]-0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]-0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                # Height Values
                text = self.font.render(str(self.heights[row][col]), True, (0,0,0))
                textRect = text.get_rect()
                textRect.center = ((0.35+0.3*col/self.size)*win_size + 0.5/(2*self.size)*win_size, (0.35+0.3*row/self.size)*win_size + 0.5/(2*self.size)*win_size)
                win.blit(text, textRect)

        # Draw each of the images
        for img in self.images:
            img.draw()

    def hover(self):
        '''Check if mouse is hovering over a sculpture tile and highlight the corresponding image tile'''
        cursor = pygame.mouse.get_pos()
        if 0.35*win_size < cursor[0] < 0.65*win_size and 0.35*win_size < cursor[1] < 0.65*win_size:
            highlight = [(cursor[0] - 0.35*win_size) // (0.3*win_size/self.size), (cursor[1] - 0.35*win_size) // (0.3*win_size/self.size)]
            pygame.draw.rect(win, (0,0,0), ((0.35+0.3*highlight[0]/self.size)*win_size, (0.35+0.3*highlight[1]/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)

    def valid(self):
        '''Checks if the sculpture is valid, that is, none of the mirrors are being blocked'''
        '''print(self.directions)
        print(self.heights)'''
        for i in range(self.size):
            for j in range(self.size):
                '''print()
                print(i, j)
                print('current spot', self.directions[i][j], self.heights[i][j])'''
                if self.directions[i,j] == 1:
                    if i == 0:
                        continue
                    line_of_sight = self.heights[:i,j]
                if self.directions[i,j] == 2:
                    if j == self.size - 1:
                        continue
                    line_of_sight = self.heights[i,(j+1):]
                if self.directions[i,j] == 3:
                    if i == self.size - 1:
                        continue
                    line_of_sight = self.heights[(i+1):,j]
                if self.directions[i,j] == 4:
                    if j == 0:
                        continue
                    line_of_sight = self.heights[i,:j]

                if line_of_sight.max() >= self.heights[i,j]:
                    return False
        return True

size = 5

directions = np.random.randint(1, 5, size = (size, size))
heights = np.random.randint(1, size+1, size = (size, size))

# True cases to test
'''directions = np.array([[4, 2],
                       [3, 3]])
heights = np.array([[2, 2],
                    [2, 1]])'''
'''directions = np.array([[4, 1],
                       [2, 2]])
heights = np.array([[2, 1],
                    [2, 1]])'''
'''directions = np.array([[4, 1, 1],
                       [4, 1, 2],
                       [3, 1, 2]])
heights = np.array([[1, 1, 1],
                    [1, 2, 1],
                    [1, 3, 1]])'''             

# img = np.random.randint(1,255, size = (int(0.3*win_size), int(0.3*win_size)))
x = np.arange(0, int(0.3*win_size))
y = np.arange(0, int(0.3*win_size))
X, Y = np.meshgrid(x, y)
img = X + Y
img = 255*img/img.max()

S = Sculpture(directions, heights, (Image(img, size), Image(img, size), Image(img, size), Image(img, size)))

if __name__ == '__main__':
    win = pygame.display.set_mode((win_size, win_size))
    pygame.display.set_caption('Mirror Sculpture')

    print(S.valid())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        win.fill((255,255,255))
        S.hover()
        S.draw()
        pygame.display.update()