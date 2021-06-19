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
    def __init__(self, size, img = 255 * np.ones((int(0.3*win_size), int(0.3*win_size))), location = 1):
        self.img = img
        self.array = []
        self.size = size
        self.location = location # Can be 1-4 for images around the sculpture or 5 for the top

    def draw(self):
        rimg = pygame.surfarray.make_surface(np.rot90(self.img, self.location-1))
        # Draw pieces of the image in the corresponding grid tiles
        if self.location == 1:
            win.blit(rimg, (0.35*win_size, 0.025*win_size))
        elif self.location == 2:
            win.blit(rimg, (0.675*win_size, 0.35*win_size))
        elif self.location == 3:
            win.blit(rimg, (0.35*win_size, 0.675*win_size))
        elif self.location == 4:
            win.blit(rimg, (0.025*win_size, 0.35*win_size))
        elif self.location == 5:
            win.blit(rimg, (0.025*win_size, 0.025*win_size))
        # Draw grid offset from center
        for i in range(self.size + 1):
            if i == 0 or i == self.size:
                line_thickness = 2
            else:
                line_thickness = 1
            if self.location == 1:
                pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.025+0.3*i/self.size)*win_size), (0.65*win_size, (0.025+0.3*i/self.size)*win_size), line_thickness)
                pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.025*win_size), ((0.35+0.3*i/self.size)*win_size, 0.325*win_size), line_thickness)
            elif self.location == 2:
                pygame.draw.line(win, (0,0,0), (0.675*win_size, (0.35+0.3*i/self.size)*win_size), (0.975*win_size, (0.35+0.3*i/self.size)*win_size), line_thickness)
                pygame.draw.line(win, (0,0,0), ((0.675+0.3*i/self.size)*win_size, 0.35*win_size), ((0.675+0.3*i/self.size)*win_size, 0.65*win_size), line_thickness)
            elif self.location == 3:
                pygame.draw.line(win, (0,0,0), (0.35*win_size, (0.675+0.3*i/self.size)*win_size), (0.65*win_size, (0.675+0.3*i/self.size)*win_size), line_thickness)
                pygame.draw.line(win, (0,0,0), ((0.35+0.3*i/self.size)*win_size, 0.675*win_size), ((0.35+0.3*i/self.size)*win_size, 0.975*win_size), line_thickness)
            elif self.location == 4:
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
        self.reflection = 255 * np.ones((int(0.3*win_size), int(0.3*win_size)))

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
                elif self.directions[row,col] == 2:
                    pygame.draw.line(win, (0,0,0), (center[0]-0.07*win_size/self.size, center[1]), (center[0]+0.07*win_size/self.size, center[1]), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]-0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0]+0.07*win_size/self.size, center[1]), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                elif self.directions[row,col] == 3:
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]-0.07*win_size/self.size), (center[0], center[1]+0.07*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]-0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                    pygame.draw.line(win, (0,0,0), (center[0], center[1]+0.07*win_size/self.size), (center[0]+0.035*win_size/self.size, center[1]+0.035*win_size/self.size), 2)
                elif self.directions[row,col] == 4:
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

        # Draw reflection
        self.reflect()
        Image(self.size, self.reflection, 5).draw()

    def hover(self):
        '''Check if mouse is hovering over a sculpture tile and highlight the corresponding image tile'''
        cursor = pygame.mouse.get_pos()
        if 0.35*win_size < cursor[0] < 0.65*win_size and 0.35*win_size < cursor[1] < 0.65*win_size:
            # Draw highlight on the sculpture
            row, col = int((cursor[1] - 0.35*win_size) // (0.3*win_size/self.size)), int((cursor[0] - 0.35*win_size) // (0.3*win_size/self.size))
            pygame.draw.rect(win, (0,0,0), ((0.35+0.3*col/self.size)*win_size, (0.35+0.3*row/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)
            
            print(row, col, self.directions[row,col], self.heights[row,col])
            # Draw highlight on the image
            if self.directions[row,col] == 1:
                img_row = col
                img_col = self.size - self.heights[row,col]
                pygame.draw.rect(win, (0,0,0), ((0.35+0.3*img_row/self.size)*win_size, (0.025+0.3*img_col/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)
            elif self.directions[row,col] == 2:
                img_row = self.heights[row,col] - 1
                img_col = row
                pygame.draw.rect(win, (0,0,0), ((0.675+0.3*img_row/self.size)*win_size, (0.35+0.3*img_col/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)
            elif self.directions[row,col] == 3:
                img_row = col
                img_col = self.heights[row,col] - 1
                pygame.draw.rect(win, (0,0,0), ((0.35+0.3*img_row/self.size)*win_size, (0.675+0.3*img_col/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)
            elif self.directions[row,col] == 4:
                img_row = self.size - self.heights[row,col]
                img_col = row
                pygame.draw.rect(win, (0,0,0), ((0.025+0.3*img_row/self.size)*win_size, (0.35+0.3*img_col/self.size)*win_size, 0.3*win_size/self.size, 0.3*win_size/self.size), 3)

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

    def reflect(self):
        '''Gets the reflection of all images on the sculpture'''
        for row in range(3):
            for col in range(3):
                if self.directions[row,col] == 1:
                    img_row = col
                    img_col = self.size - self.heights[row,col]
                elif self.directions[row,col] == 2:
                    img_row = self.heights[row,col] - 1
                    img_col = row
                elif self.directions[row,col] == 3:
                    img_row = self.heights[row,col] - 1
                    img_col = col
                elif self.directions[row,col] == 4:
                    img_row = self.size - self.heights[row,col]
                    img_col = row
                    
                '''a1 = int(row*0.3*win_size/self.size)
                b1 = int((row+1)*0.3*win_size/self.size)
                c1 = int(col*0.3*win_size/self.size)
                d1 = int((col+1)*0.3*win_size/self.size)
                '''
                c1 = int(row*0.3*win_size/self.size)
                d1 = int((row+1)*0.3*win_size/self.size)
                a1 = int(col*0.3*win_size/self.size)
                b1 = int((col+1)*0.3*win_size/self.size)

                a2 = int(img_row*0.3*win_size/self.size)
                c2 = int(img_col*0.3*win_size/self.size)
                dist1 = b1 - a1
                dist2 = d1 - c1

                # Not sure why row and col need to be swapped here
                self.reflection[a1:b1,c1:d1] = np.rot90(self.images[self.directions[row,col]-1].img, self.images[self.directions[row,col]-1].location - 1)[a2:a2+dist1,c2:c2+dist2]
                
                print('Row:',row,'Col:',col,'Image:',self.directions[row,col] - 1,'img_row:',img_row,'img_col',img_col)
                print('a1 b1',a1,b1,'c1 d1',c1,d1)
                print('a2 b2',a2,a2+dist1,'c2 d2',c2,c2+dist2)

                # Unrotated image
                #win.blit(pygame.surfarray.make_surface(self.images[self.directions[row,col] - 1].img), (540, 20))

                # Rotated image
                #reg = self.images[self.directions[row,col] - 1].img
                #rot = np.rot90(self.images[self.directions[row,col] - 1].img, self.images[self.directions[row,col]-1].location - 1)
                #print(reg.shape, rot.shape)
                #win.blit(pygame.surfarray.make_surface(rot), (20, 540))
                #win.blit(pygame.surfarray.make_surface(reg[0:80,]), (540, 540))
                #win.blit(pygame.surfarray.make_surface(rot[0:80,]), (630, 540))

size = 3

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
directions = np.array([[4, 1, 1],
                       [4, 1, 2],
                       [3, 1, 2]])
heights = np.array([[1, 1, 1],
                    [1, 2, 1],
                    [1, 3, 1]])            

# img = np.random.randint(1,255, size = (int(0.3*win_size), int(0.3*win_size)))

x = np.arange(0, int(0.3*win_size))
y = np.arange(0, int(0.3*win_size))
X, Y = np.meshgrid(x, y)
img = np.sin((X/30)**2 + (Y/30)**5)
img = 5*img/img.max()

S = Sculpture(directions, heights, (Image(size, img), Image(size, img), Image(size, img), Image(size, img)))

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
        S.draw()
        S.hover()

        pygame.display.update()