# bentham_assessment

An implementation of Schelling's model of segregation.

It is a cellular automata simulation where 'blue' or 'red' houses relocate to random position in the 2D grid depending on the fraction of neighbours with similarly coloured houses. 

To perform the simulation first create a ```Town``` object and set the width and height of the 2D grid.
Then set the ```similarity``` value which sets the cutoff fraction of similarly coloured houses at which a house will relocate.
```
town = Town(w = 100, h = 100, similarity = 0.63)
```
In the Schelling model the houses are initially randomly distributed across the grid.
This can be accomplished by calling:
```
town.init_grid(red_f = 0.43, blue_f = 0.43)
```
The parameters ```red_f``` and ```blue_f``` set the percentage of the total number of grid sites that are initially occupied by red or blue houses. 

Finally the simulation can be run by calling ```town.update()``` for an appropriate number of time steps. (Around ```300000``` for a ```100*100``` grid). 

## Example simulation results.  
![Example simulation results.](https://raw.githubusercontent.com/lennon-phys/bentham_assessment/main/example.png)
