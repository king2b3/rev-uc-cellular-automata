## Evolutionary Process
1. Cells initialized in some 2-D space. Each cell is initialized with a range of possible traits (size, smell, speed, etc)
  Size  - A number of cells in the 2-D grid. The bigger the more energy they spend by moving. But, the more area they can cover.
  Sense - The cell's ability to detect food, obstacles, pray, and predators. The more sense an individual has, the more energy they use. 
  Speed - How quickly they can traverse through the 2-D system. Faster individuals use more energy.
 
2. Food, obstacles, and predators are placed randomly in the 2-D space in every generation. 
  Food      - Stored energy. The amount of stored energy is directly related to the size of the food.
  Obstacles - Some of the cells become impassable, and individuals must move around them to advance. Think a log in a pathway.
  Predators - Will chase and attempt to eat the cells. It will have a sense, size, and speed trait. We can look at letting them evolve too.

3. The Cells' goal is to reproduce and/or survive into the next generation, energy is needed to do this.
  If cell_energy > survival_energy_min Then cell_survives
    Mutation % 
    If cell_energy > reproduce_energy min Then cell reproduces
  Else Then the cell dies off.
 
## Gui
This is going to be quite a large tasks, and I'm going to propose way more than we need for it. I think that if we can just implement 1 and 2 we are golden, but I'm going to put the desired full project here. 3 onward are just desires, and not in a particular order.
1. Input and Output. The GUI parses the args for the simulation to the program (mutation rate, initialization types, number of gens, amount of food, etc), then the GUI can show the simulation afterwards. I'm going to propose that we generate the gif then show it, for reasons I'll explain later.
2. Various playback speeds, restart the gif. Hence why we should generate it, then show it. Allow the user to speed up / slow down the gif, restart, pause, play. Although we might be able to do generation in real time, showing the generated gif should be easier.
3. User can see any plot of the output statistics that they would like. They could request to see "Size v Generations" Or maybe "Size and Sense v Generations". Basically call the plotting API
4. GUI shows the average values for each trait next to the output windows during the simulation. IE A user can track the mutations across each generation. Display the birth/death rates. 
5. The user can pause and look at a plot without restarting the playback. IE They can move from plotting to playback at will, moving from playback to plotting will pause the gif. They can resume at will. 

## Plotting / Data analysis
I think we should have a plotting API that we can call to display various plots. 1-2 again are wants for the hacakthon, 3 onwards are just desires again not ordered. I would suggest matplot lib, but we could use matlab if we wanted for this. My goal is to have all the data that would be needed for this in a json after the evolutionary process is done.
1. Can have X number of plots as the dependant variable(s), and 1 independent variable (generations, time steps)
2. The end goal is to let the GUI call this API, but we could also just run a script to generate a bunch of plots and let the user view them either in the GUI or by opening them directly. 
3. Multiple plots can be subplotted for the output. IE the user can call for NxN plots on a single output. 
4. Generate a results pdf that shows the input and outputs of the test all in a report. This is just a desire, and will be more figuring out what is the best way to go this. I have done this with Pandas data-frame -> PDF before. 
