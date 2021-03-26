import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

CLEAR = 0
RED = 1
BLUE = 2

class Town: 
    def __init__(self, w, h, similarity):
        self.w = w
        self.h = h
        # The cutoff point at which a house relocates if the fraction of similarly
        # coloured neighbouring houses to all neighbouring houses is too low. 
        self.similarity = similarity    
        self.grid = np.zeros((w, h))    # Represents the entire town.  
        
        self.not_clear = []             # Keeps track of which tiles have coloured houses on them.
        self.clear = []                 # Keeps track of which tiles do NOT have coloured houses.

    def init_grid(self, red_f, blue_f):
        sites = self.w * self.h
        
        # Add all of the positions to the list of clear tiles.
        for x in range(self.w):
            for y in range(self.h):
                self.clear.append((x, y))

        # Randomly distribute red and blue houses across the town.
        self.add_fraction(RED, red_f)
        self.add_fraction(BLUE, blue_f)
        
    # Randomly distributes houses across the town until a certain fraction of them are coloured. 
    def add_fraction(self, colour, fraction):
        number = 0
        sites = self.w * self.h
        
        while number < fraction * sites:
            # Place a coloured house on a random site. 
            self.random_place(colour)
            
            number +=1

    # Places a coloured house at a random empty position. 
    def random_place(self, colour):
        
        # Select a random empty tile. 
        i = np.random.randint(len(self.clear))
        x, y = self.clear[i]

        self.clear.pop(i)
        self.not_clear.append((x, y))
        
        self.grid[x][y] = colour

    # Returns the fraction of neighbours with the same colour house. 
    def fraction(self, colour, x, y):
        fraction = 0
        r, b = self.neighbours(x, y)
    
        if r == 0 and b == 0:
            fraction = 0                
        elif colour == RED:
            fraction = r / (r + b)
        elif colour == BLUE:
            fraction = b / (r + b)
            
        return fraction
                    
    # Calculates the number of red and blue neighbours that a house has. 
    # (The function checks all 8 surrounding tiles). 
    def neighbours(self, x, y):
        r = 0
        b = 0
        
        for xOffs in [-1, 0, 1]:
            for yOffs in [-1, 0, 1]:
                xpos = (x + xOffs + self.w) % self.w
                ypos = (y + yOffs + self.h) % self.h
                
                # Ignore the house we are at.
                if(xpos != x or ypos != y):
                    if self.grid[xpos][ypos] == RED:
                        r += 1
                    elif self.grid[xpos][ypos] == BLUE:
                        b += 1
        
        return r, b
                        
    def update(self):
        # Select a random house in the town.
        i = np.random.randint(len(self.not_clear))
        x, y = self.not_clear[i]
        
        # The house relocates to a random empty tile if the fraction of similarly
        # coloured neighbouring houses to all neighbouring houses is too low. 
        if self.fraction(self.grid[x][y], x, y) < self.similarity:  
            colour = self.grid[x][y]

            # Remove the house at (x, y).
            self.grid[x][y] = CLEAR
            self.clear.append((x, y))
            self.not_clear.pop(i)

            # Place a house of the same colour at a random position. 
            self.random_place(colour)
    

town = Town(w = 100, h = 100, similarity = 0.63)
town.init_grid(red_f = 0.43, blue_f = 0.43)

# Simulate the town.
for _ in range(300000):
    town.update()

# Plot the final town. 
fig = plt.figure(figsize=(5,5))
img = plt.imshow(town.grid, interpolation='nearest')
cmap = LinearSegmentedColormap.from_list('cmap', ['lightgrey', 'blue', 'red'])
img.set_cmap(cmap)
plt.axis('off')
plt.show()