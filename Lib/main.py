# https://towardsdatascience.com/simple-little-tables-with-matplotlib-9780ef5d0bc4
import random
import string
import numpy as np
import matplotlib.pyplot as plt

class Grid:
    def __init__(self):
        self.gridcode = {}
        for i in range(1,6):
            for j in range(65,70):
                gridname = chr(j) + str(i)
                self.gridcode[gridname]= Grid.randomletterset(self)

    def randomletterset(self):
        finalrandomlettergroup = ""
        for i in range(3):
            randomeletter = random.choice(string.ascii_letters)
            finalrandomlettergroup += randomeletter
        return finalrandomlettergroup.upper()

    def __str__(self):
        print(self.gridcode)

class DisplayChart(Grid):
    def __init__(self):
        super().__init__()
        self.columns = [chr(x) for x in range(65,70)]
        self.rows = [str(x) for x in range(1,6)]
        self.colors = plt.cm.BuPu(np.linspace(0, 0.5, len(self.rows)))
        self.nrows = len(self.rows)
        """This next line of code posed a huge problem in that the matplotlib library required the table to be list of 
        lists.  So, after turning the gridcode into a list, I had to break that list down into the five secitions
        needed in order for the table library to work properly.  I tried using the array() function in numpy
        but it didn't create the output I was looking for"""
        self.cell_text = [list(self.gridcode.values())[x:x+5] for x in range(0, len(list(self.gridcode.values())),5)]

    def display_table(self):
        # Hide axes
        title_text = "Passcode Chart"
        fig_background_color = 'skyblue'
        fig_border = 'steelblue'
        # Get some lists of color specs for row and column headers
        rcolors = plt.cm.BuPu(np.full(self.nrows, 0.1))
        ccolors = plt.cm.BuPu(np.full(len(self.columns), 0.1))
        # Create the figure. Setting a small pad on tight_layout
        # seems to better regulate white space. Sometimes experimenting
        # with an explicit figsize here can produce better outcome.
        plt.figure(linewidth=2,
                   edgecolor=fig_border,
                   facecolor=fig_background_color,
                   tight_layout={'pad': 1},
                   # figsize=(5,3)
                   )
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        # Hide axes border
        plt.box(on=None)
        # Add title
        plt.suptitle(title_text)
        # Force the figure to update, so backends center objects correctly within the figure.
        # Without plt.draw() here, the title will center on the axes and not the figure.
        plt.draw()
        the_table = plt.table(cellText=self.cell_text,
                              rowLabels=self.rows,
                              # rowColours=self.colors,
                              rowColours=rcolors,
                              rowLoc = "center",
                              cellLoc = "center",
                              colLabels=self.columns,
                              colColours = ccolors,
                              loc='center')
        # Scaling is the only influence we have over top and bottom cell padding.
        # Make the rows taller (i.e., make cell y scale larger).

        # the_table.scale(1, 1.5)

        fig = plt.gcf()
        plt.savefig('your passcode table.png',
                    # bbox='tight',
                    edgecolor=fig.get_edgecolor(),
                    facecolor=fig.get_facecolor(),
                    dpi=150
                    )
        plt.show()

class UserConfirmation(Grid):
    def __init__(self,griddata):
        super().__init__()
        self.randomcell1 = random.choice(list(griddata.keys()))
        self.randomcell2 = random.choice(list(griddata.keys()))
        self.randomcell3 = random.choice(list(griddata.keys()))

    def identify_user(self,griddata):
        user_answer_first_cell = input(f"What is in cell {self.randomcell1}? ")
        user_answer_second_cell = input(f"What is in cell {self.randomcell2}? ")
        user_answer_third_cell = input(f"What is in cell {self.randomcell3}? ")
        if user_answer_first_cell.upper() == griddata[self.randomcell1] and user_answer_second_cell.upper() == griddata[self.randomcell2] and user_answer_third_cell.upper() == griddata[self.randomcell3]:
            print("You are you!  Congratulations!")
        else:
            print("You are an imposter!!")

class UserInformation:
    def __init__(self):
        pass

workinggrid = DisplayChart()
print(workinggrid.gridcode)
print(workinggrid.display_table())
user_identification_attempt = UserConfirmation(workinggrid.gridcode)
user_identification_attempt.identify_user(workinggrid.gridcode)


